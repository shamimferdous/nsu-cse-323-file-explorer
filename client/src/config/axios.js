import axios from "axios";

let baseUrl;
if (process.env.NODE_ENV === "development") {
    baseUrl = "http://localhost:8000/api";
} else if (process.env.NODE_ENV === "production") {
    baseUrl = "http://localhost:8000/api";
} else {
    baseUrl = "http://localhost:8000/api";
}

//creating an axios instance with auth setup
const axiosInstance = axios.create({
    baseURL: baseUrl,
    timeout: 400000,
});

axiosInstance.interceptors.request.use((config) => {

    return config;
});

//defining the interceptor which will automate the process of refresh and access token
axiosInstance.interceptors.response.use(
    function (response) {
        // Simply returning the response
        return response;
    },
    function (error) {
        return Promise.reject(error);
    }
);

export default axiosInstance;
