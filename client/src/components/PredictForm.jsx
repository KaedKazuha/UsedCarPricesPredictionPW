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
    <div>
      <h2>Predict Car Price</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" name="year" placeholder="Year" value={carDetails.year} onChange={handleChange} required />
        <input type="number" name="mileage" placeholder="Mileage" value={carDetails.mileage} onChange={handleChange} required />
        <input type="text" name="fuel_type" placeholder="Fuel Type" value={carDetails.fuel_type} onChange={handleChange} required />
        <input type="number" name="engine_capacity" placeholder="Engine Capacity" value={carDetails.engine_capacity} onChange={handleChange} required />
        <input type="text" name="transmission" placeholder="Transmission" value={carDetails.transmission} onChange={handleChange} required />
        <input type="text" name="location" placeholder="Location" value={carDetails.location} onChange={handleChange} required />
        <input type="text" name="make" placeholder="Make" value={carDetails.make} onChange={handleChange} required />
        <input type="text" name="model" placeholder="Model" value={carDetails.model} onChange={handleChange} required />
        <button type="submit">Predict Price</button>
      </form>
      {predictedPrice !== null && (
        <div>
          <h3>Predicted Price: PKR {predictedPrice}</h3>
        </div>
      )}
    </div>
  );
};

export default PredictForm;
