import axios from 'axios';

const API_BASE_URL = "/api";

export const getVehicles = async ({ page = 1, make = '', model = '' }) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/vehicles`, {
      params: { page, make, model }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching vehicles:', error);
    throw error;
  }
};

export const searchVehicleByMakeModel = async (make, model, page = 1, limit = 10) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/vehicles/search`, {
      params: { make, model, page, limit }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching vehicles:', error);
    throw error;
  }
};

export const predictCarPrice = async (carDetails) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/predict`, carDetails);
    return response.data.predicted_price;
  } catch (error) {
    console.error('Error predicting car price:', error);
    throw error;
  }
};
