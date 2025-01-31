import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api/";

const api = axios.create({
  baseURL: BASE_URL,
  withCredentials: true,
});

export const get_user_profile = async (username) => {
  try {
    console.log(`Fetching data for ${username}`);
    const response = await api.get(`user_data/${username}/`);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error("API request failed:", error);
    throw error;
  }
};
