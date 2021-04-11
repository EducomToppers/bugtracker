import Vue from 'vue';
import App from './App.vue';
import Axios from 'axios';

import VueRouter from 'vue-router';

import Home from './components/Home.vue';
import Login from './components/Login.vue';

Vue.use(VueRouter);

Vue.config.productionTip = false;

const csrftoken = document.cookie.split('=')[1];

Axios.defaults.baseURL = 'http://localhost:8000';
Axios.defaults.withCredentials = true;
Axios.defaults.headers.common['X-CSRFToken'] = csrftoken

const router = new VueRouter({
  routes: [
    // dynamic segments start with a colon
    { path: '/', component: Home },
    { path: '/accounts/login/', component: Login }
  ]
});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
