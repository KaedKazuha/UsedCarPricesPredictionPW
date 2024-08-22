import React, { useState } from 'react';
import { predictCarPrice } from '../services/api';

const PredictForm = () => {
  const [carDetails, setCarDetails] = useState({
    year: '',
    mileage: '',
    fuel_type: '',
    engine_capacity: '',
    transmission: '',
    location: '',
    make: '',
    model: '',
  });
  const [predictedPrice, setPredictedPrice] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCarDetails({ ...carDetails, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const price = await predictCarPrice(carDetails);
      setPredictedPrice(price);
    } catch (error) {
      console.error('Error predicting car price:', error);
    }
  };

  return (
    <div className="max-w-lg mx-auto p-4 bg-white shadow-lg rounded-lg">
      <h2 className="text-2xl font-bold mb-4 text-center">Predict Car Price</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input className="w-full p-2 border border-gray-300 rounded" type="number" name="year" placeholder="Year" value={carDetails.year} onChange={handleChange} required />
        <input className="w-full p-2 border border-gray-300 rounded" type="number" name="mileage" placeholder="Mileage" value={carDetails.mileage} onChange={handleChange} required />
        <input className="w-full p-2 border border-gray-300 rounded" type="text" name="fuel_type" placeholder="Fuel Type" value={carDetails.fuel_type} onChange={handleChange} required />
        <input className="w-full p-2 border border-gray-300 rounded" type="number" name="engine_capacity" placeholder="Engine Capacity" value={carDetails.engine_capacity} onChange={handleChange} required />
        <input className="w-full p-2 border border-gray-300 rounded" type="text" name="transmission" placeholder="Transmission" value={carDetails.transmission} onChange={handleChange} required />
        <input className="w-full p-2 border border-gray-300 rounded" type="text" name="location" placeholder="Location" value={carDetails.location} onChange={handleChange} required />
        <input className="w-full p-2 border border-gray-300 rounded" type="text" name="make" placeholder="Make" value={carDetails.make} onChange={handleChange} required />
        <input className="w-full p-2 border border-gray-300 rounded" type="text" name="model" placeholder="Model" value={carDetails.model} onChange={handleChange} required />
        <button className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700">Predict Price</button>
      </form>
      {predictedPrice !== null && (
        <div className="mt-4 p-4 bg-green-100 text-green-800 rounded">
          <h3 className="text-xl font-bold">Predicted Price: PKR {predictedPrice}</h3>
        </div>
      )}
    </div>
  );
};

export default PredictForm;