import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const PriceTrendGraph = ({ trendData, make, model }) => {
    return (
        <div className="overflow-x-auto">
            <h3 className="text-xl font-semibold mb-4 text-center">
                Price By Model {make} {model}
            </h3>
            <ResponsiveContainer width="100%" height={400}>
                <LineChart
                    data={trendData}
                    margin={{
                        top: 20, right: 30, left: 20, bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="year" />
                    <YAxis />
                    <Tooltip />
                    <Line type="monotone" dataKey="price" stroke="#8884d8" />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
};

export default PriceTrendGraph;
