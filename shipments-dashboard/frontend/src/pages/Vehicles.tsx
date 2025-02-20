import React, { useEffect, useState } from "react";
import { fetchVehicleEfficiency } from "@/services/api";

const Vehicles = () => {
  const [vehicles, setVehicles] = useState([]);
  const [page, setPage] = useState(1);

  useEffect(() => {
    const loadData = async () => {
      const data = await fetchVehicleEfficiency((page-1)*10);
      if (data) setVehicles(data);
    };
    loadData();
  }, [page]);

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Vehicles</h1>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse border border-gray-300">
          <thead>
            <tr className="bg-gray-100">
              <th className="border p-2">Vehicle ID</th>
              <th className="border p-2">Total Mileage (km)</th>
              <th className="border p-2">Total Fuel Used (L)</th>
              <th className="border p-2">Fuel Efficiency (km/L)</th>
            </tr>
          </thead>
          <tbody>
            {vehicles.map((vehicle) => (
              <tr key={vehicle.vehicle_id} className="hover:bg-gray-50">
                <td className="border p-2">{vehicle.vehicle_id}</td>
                <td className="border p-2">{vehicle.total_mileage}</td>
                <td className="border p-2">{vehicle.total_fuel_used}</td>
                <td className="border p-2">{vehicle.fuel_efficiency}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-4 flex justify-between">
        <button
          onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
          disabled={page === 1}
          className={`px-4 py-2 rounded ${page === 1 ? "bg-gray-300" : "bg-blue-500 text-white hover:bg-blue-600"}`}
        >
          Previous
        </button>
        <span className="px-4 py-2">Page {page}</span>
        <button
          onClick={() => setPage((prev) => prev + 1)}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default Vehicles;
