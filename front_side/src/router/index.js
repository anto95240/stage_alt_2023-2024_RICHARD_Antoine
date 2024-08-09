import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import LoginPage from '../views/LoginPage.vue';
import RegisterPage from '../views/RegisterPage.vue';
import DashboardPage from '../views/DashboardPage.vue';
import LogOut from '../views/LogOut.vue'
import AccountPage from '../views/AccountPage.vue';
import CoursPage from '../views/CoursPage.vue';
import NotePage from '../views/NotePage.vue';
import DocumentPage from '../views/DocumentPage.vue';
import VieScolaire from '../views/VieScolaire.vue';
import NotificationPage from '../views/NotificationPage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/:role/login',
    name: 'LoginPage',
    component: LoginPage,
    props: true
  },
  {
    path: '/:role/register',
    name: 'RegisterPage',
    component: RegisterPage,
    props: true
  },
  {
    path: '/:role/dashboard',
    name: 'DashboardPage',
    component: DashboardPage,
    props: true,
  },
  {
    path: '/:role/account',
    name: 'AccountPage',
    component: AccountPage,
    props: true
  },
  {
    path: '/:role/cours',
    name: 'CoursPage',
    component: CoursPage,
    props: true
  },
  {
    path: '/:role/note',
    name: 'NotePage',
    component: NotePage,
    props: true
  },
  {
    path: '/:role/vie-scolaire',
    name: 'VieScolaire',
    component: VieScolaire,
    props: true
  },
  {
    path: '/:role/document',
    name: 'DocumentPage',
    component: DocumentPage,
    props: true
  },
  {
    path: '/:role/notification',
    name: 'NotificationPage',
    component: NotificationPage,
    props: true
  },
  {
    path: '/:role/logout',
    name: 'LogOut',
    component: LogOut,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});


export default router;
