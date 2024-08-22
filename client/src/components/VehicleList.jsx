import React, { useEffect, useState } from 'react';
import { getVehicles } from '../services/api';

const VehicleList = () => {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    const fetchVehicles = async () => {
      const data = await getVehicles();
      setVehicles(data);
    };

    fetchVehicles();
  }, []);

  return (
    <div>
      <h2>Vehicle List</h2>
      <ul>
        {vehicles.map((vehicle, index) => (
          <li key={index}>
            <p>
              {vehicle.make} {vehicle.model} ({vehicle.year})
            </p>
            <p>Price: {vehicle.price_display}</p>
            <p>Mileage: {vehicle.mileage} km</p>
            <p>Fuel Type: {vehicle.fuel_type}</p>
            <p>Engine Capacity: {vehicle.engine_capacity} cc</p>
            <p>Transmission: {vehicle.transmission}</p>
            <p>Location: {vehicle.location}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VehicleList;