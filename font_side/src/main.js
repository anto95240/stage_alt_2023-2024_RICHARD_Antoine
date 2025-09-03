// main.js
import { createApp } from 'vue';
import router from './router';
import App from './App.vue';
import store from './store';
import axios from 'axios';

// Configure axios default base URL
axios.defaults.baseURL = 'http://localhost:8000/';
// axios.defaults.withCredentials = true;


createApp(App).use(store).use(router, axios).mount('#app');
