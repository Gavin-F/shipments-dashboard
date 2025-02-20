export const API_BASE_URL = "http://localhost:8000";

export const fetchDailySummary = async (date: string) => {
  try {
    const response = await fetch(`${API_BASE_URL}/analysis/daily-summary?summary_date=${date}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching daily summary data:", error);
    return null;
  }
};

export const fetchTopExpensiveRoutes = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/shipments/analysis/top-expensive-routes`);
    if (!response.ok) throw new Error("Failed to fetch top expensive routes");
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error("Error fetching top expensive routes:", error);
    return [];
  }
};

export const fetchRouteSummary = async (origin: string, destination: string) => {
  console.log(origin + " -> " + destination)
  try {
    const response = await fetch(`${API_BASE_URL}/shipments/analysis/route-summary?origin=${origin}&destination=${destination}`);
    if (!response.ok) throw new Error("Failed to fetch route summary");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching route summary:", error);
    return null;
  }
};

export const fetchVehicleEfficiency = async (offset: number) => {
  try {
    const response = await fetch(`${API_BASE_URL}/vehicles/analysis/efficiency?offset=${offset}`);
    if (!response.ok) throw new Error("Failed to fetch vehicle efficiency");
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error("Error fetching vehicle efficiency:", error);
    return [];
  }
};

export const fetchTimeSeriesSummary = async (range: number = 7) => {
  try {
    const response = await fetch(`${API_BASE_URL}/analysis/timeseries?range=${range}`);
    if (!response.ok) throw new Error("Failed to fetch time series summary");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching time series summary:", error);
    return { data: [] };
  }
};


