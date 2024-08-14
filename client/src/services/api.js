import axios from 'axios';

export const getCleanedVehicles = async () => {
  try {
    const response = await axios.get('/api/vehicles');  // Adjust the endpoint if needed
    return response.data;  // Ensure your API returns an array of cleaned vehicle objects
  } catch (error) {
    console.error('Error fetching cleaned vehicles:', error);
    return [];
  }
};
// import axios from 'axios';

// const API_BASE_URL = "/api";

// export const getVehicles = async () => {
//   try {
//     const response = await axios.get(`${API_BASE_URL}/vehicles`);
//     return response.data;
//   } catch (error) {
//     console.error('Error fetching cleaned vehicles:', error);
//     throw error;
//   }
// };
