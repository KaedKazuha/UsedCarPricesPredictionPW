// import axios from 'axios';

// export const getCleanedVehicles = async () => {
//   try {
//     const response = await axios.get('/api/vehicles');  // Adjust the endpoint if needed
//     return response.data;  // Ensure your API returns an array of cleaned vehicle objects
//   } catch (error) {
//     console.error('Error fetching cleaned vehicles:', error);
//     return [];
//   }
// };
import axios from 'axios';

const API_BASE_URL = "/api";

// Function to fetch cleaned vehicles (existing function)
export const getVehicles = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/vehicles`);
    return response.data;
  } catch (error) {
    console.error('Error fetching cleaned vehicles:', error);
    throw error;
  }
};

// New function to predict car price based on user input
export const predictCarPrice = async (carDetails) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/predict`, carDetails);
    return response.data.predicted_price;
  } catch (error) {
    console.error('Error predicting car price:', error);
    throw error;
  }
};
