import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

interface ChartProps {
  data: any[];
  metric: string;
  title: string;
  color: string;
}

const TimeSeriesChart: React.FC<ChartProps> = ({ data, metric, title, color }) => {
  return (
    <div className="bg-white p-4 shadow rounded-lg">
      <h2 className="text-lg font-semibold mb-4">{title}</h2>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data} margin={{ top: 10, right: 20, left: 15, bottom: 0 }}>
          <XAxis dataKey="date" />
          <YAxis/>
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey={metric} stroke={color} name={title} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default TimeSeriesChart;
