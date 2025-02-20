import React, { useEffect, useState } from "react";
import TimeSeriesChart from "@/components/TimeSeriesChart";
import { fetchDailySummary } from "@/services/api";
import { fetchTimeSeriesSummary } from "@/services/api";

const Dashboard = () => {
  const today = new Date().toISOString().split("T")[0];
  const [summary, setSummary] = useState(null);
  const [selectedDate, setSelectedDate] = useState(today);
  const [pendingDate, setPendingDate] = useState(today);
  const [range, setRange] = useState(7);
  const [timeSeriesData, setTimeSeriesData] = useState([]);


  useEffect(() => {
    const loadData = async () => {
      if (!selectedDate) return;
      const data = await fetchDailySummary(selectedDate);
      if (data) setSummary(data);
    };
    loadData();
  }, [selectedDate]);

  useEffect(() => {
    const loadTimeSeries = async () => {
      const data = await fetchTimeSeriesSummary(range);
      setTimeSeriesData(data.data);
    };

    loadTimeSeries();
  }, [range]);

  const handleDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPendingDate(event.target.value);
  };

  const confirmDate = () => {
    if (pendingDate) setSelectedDate(pendingDate);
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      <div className="mb-4 flex space-x-2 items-center">
        <label htmlFor="date" className="text-gray-600">Select Date:</label>
        <input
          type="date"
          id="date"
          value={pendingDate}
          onChange={handleDateChange}
          className="border p-2 rounded"
        />
        <button
          onClick={confirmDate}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          View Data
        </button>
      </div>

      {summary ? (
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="bg-white p-4 shadow rounded-lg">
            <p className="text-gray-600">Total Shipments</p>
            <h2 className="text-2xl font-semibold">{summary.num_shipments || 0}</h2>
          </div>
          <div className="bg-white p-4 shadow rounded-lg">
            <p className="text-gray-600">Total Vehicles Used</p>
            <h2 className="text-2xl font-semibold">{summary.total_vehicles_used || 0}</h2>
          </div>
          <div className="bg-white p-4 shadow rounded-lg">
            <p className="text-gray-600">Total Mileage</p>
            <h2 className="text-2xl font-semibold">{summary.total_mileage || 0}</h2>
          </div>
          <div className="bg-white p-4 shadow rounded-lg">
            <p className="text-gray-600">Total Fuel Used</p>
            <h2 className="text-2xl font-semibold">{summary.total_fuel_used || 0}</h2>
          </div>
        </div>
      ) : (
        <p className="text-red-500">Failed to load data.</p>
      )}

      <div className="mb-4 flex space-x-2">
        <label className="text-gray-600">Select Range:</label>
        <select
          value={range}
          onChange={(e) => setRange(Number(e.target.value))}
          className="border p-2 rounded"
        >
          <option value={7}>Last 7 Days</option>
          <option value={30}>Last 30 Days</option>
        </select>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <TimeSeriesChart data={timeSeriesData} metric="num_shipments" title="Total Shipments" color="#8884d8" />
        <TimeSeriesChart data={timeSeriesData} metric="total_vehicles_used" title="Total Vehicles Used" color="#82ca9d" />
        <TimeSeriesChart data={timeSeriesData} metric="total_mileage" title="Total Mileage (km)" color="#ff0000" />
        <TimeSeriesChart data={timeSeriesData} metric="total_fuel_used" title="Total Fuel Used (L)" color="#ff7300" />
      </div>
    </div>
  );
};

export default Dashboard;
