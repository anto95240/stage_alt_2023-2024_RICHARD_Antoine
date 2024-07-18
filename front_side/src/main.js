// main.js
import { createApp } from 'vue';
import router from './router';
import App from './App.vue';
import store from './store';
import axios from 'axios';
import VueCookies from 'vue-cookies';

axios.defaults.baseURL = 'http://127.0.0.1:8000/';

createApp(App).use(store).use(router, axios).use(VueCookies).mount('#app')
