import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from 'vue';
import axios from 'axios';

import App from './App.vue'
import router from './router'
import store from './store';

const app = createApp(App);

axios.defaults.baseURL = 'http://localhost:8000/pages/';

app.use(router);
app.use(store);
app.mount("#app");

