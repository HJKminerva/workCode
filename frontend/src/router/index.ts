import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes:[
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/test.vue'), // 懒加载
    },
    {
      path: '/test02',
      name: 'test02',
      component: () => import('../views/test02.vue'), // 懒加载
    },
    {
      path: '/aitest',
      name: 'aitest',
      component: () => import('../views/aitest.vue'), // 懒加载
    },
    {
      path:'/about',
      name:'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'), // 懒加载
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'), // 懒加载
    }
  ]
});

export default router;


