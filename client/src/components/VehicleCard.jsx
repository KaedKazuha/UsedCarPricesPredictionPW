import React from 'react';

const VehicleCard = ({ vehicle }) => (
    <div className="border border-gray-300 p-4 rounded-lg shadow-sm">
        <h3 className="text-lg font-semibold">{vehicle.make} {vehicle.model} ({vehicle.year})</h3>
        <p>Price: {vehicle.price_display}</p>
        <p>Mileage: {vehicle.mileage}</p>
        <p>Fuel Type: {vehicle.fuel_type}</p>
        <p>Engine Capacity: {vehicle.engine_capacity} cc</p>
        <p>Transmission: {vehicle.transmission}</p>
        <p>Location: {vehicle.location}</p>
    </div>
);

export default VehicleCard;
