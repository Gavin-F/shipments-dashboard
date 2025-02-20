import React, { useState, useEffect } from "react";
import { fetchTopExpensiveRoutes, fetchRouteSummary } from "@/services/api";
import { Modal } from "@/components/modal";

const Shipments = () => {
  const [topRoutes, setTopRoutes] = useState([]);
  const [selectedRoute, setSelectedRoute] = useState(null);
  const [origin, setOrigin] = useState("");
  const [destination, setDestination] = useState("");

  useEffect(() => {
    const loadData = async () => {
      const expensiveRoutes = await fetchTopExpensiveRoutes();
      if (expensiveRoutes) setTopRoutes(expensiveRoutes);
    };
    loadData();
  }, []);

  const handleSearch = async () => {
    if (!origin || !destination) return;
    const routeData = await fetchRouteSummary(origin, destination);
    setSelectedRoute(routeData);
  };

  const handleRouteClick = async (origin: string, destination: string) => {
    const routeData = await fetchRouteSummary(origin, destination);
    setSelectedRoute(routeData);
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Shipments</h1>

      <div className="mb-6 flex gap-2">
        <input
          type="text"
          placeholder="Origin"
          value={origin}
          onChange={(e) => setOrigin(e.target.value)}
          className="border p-2 rounded w-1/3"
        />
        <input
          type="text"
          placeholder="Destination"
          value={destination}
          onChange={(e) => setDestination(e.target.value)}
          className="border p-2 rounded w-1/3"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Search
        </button>
      </div>


      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {topRoutes.map((route, index) => (
          <div
              key={index}
              className="bg-white p-4 shadow rounded-lg cursor-pointer hover:bg-gray-100 transition"
              onClick={() => handleRouteClick(route.origin, route.destination)}
          >
              <h3 className="text-lg font-semibold">{route.origin} → {route.destination}</h3>
              <p className="text-gray-600">Total Cost: ${route.total_cost.toFixed(2)}</p>
          </div>
          ))}
      </div>

      {selectedRoute && (
        <Modal isOpen={!!selectedRoute} onClose={() => setSelectedRoute(null)}>
          <h2 className="text-2xl font-semibold mb-4">Route Details</h2>
          <p><strong>Origin:</strong> {selectedRoute.origin}</p>
          <p><strong>Destination:</strong> {selectedRoute.destination}</p>
          <p><strong>Avg Delivery Time:</strong> {selectedRoute.average_delivery_time} days</p>
          <p><strong>Total Cost:</strong> ${selectedRoute.total_cost}</p>
          <p><strong>Number of Deliveries:</strong> {selectedRoute.num_deliveries}</p>
        </Modal>
      )}
    </div>
  );
};

export default Shipments;
