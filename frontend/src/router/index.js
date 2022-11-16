import Vue from "vue";


import Router from "vue-router";
import Home from "../views/Home.vue";
import Search from "../views/Search.vue";
import AnswerEditor from "../views/AnswerEditor.vue";


import Question from "../views/Question.vue";
import QuestionEditor from "../views/QuestionEditor.vue";
import Porsan from "../views/Porsan.vue";
import Login from '../views/Login';
import About from '../views/About';




import Lost from '../views/Lost';
import PasswordReset from '../views/PasswordReset';
import PasswordResetConfirm from '../views/PasswordResetConfirm';
import Register from '../views/Register';
import VerifyEmail from '../views/VerifyEmail';


import store from '../store';



const requireAuthenticated = (to, from, next) => {

  store.dispatch('auth/initialize')
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next('/login');
      } else {
        next();
      }
    });

    


  store.dispatch('auth/googlelogin')
  .then(() => {
    if (!store.getters['auth/isAuthenticated']) {
      next('/login');
    } else {
      next();
    }
  });


  store.dispatch('auth/set_preference2')
  .then(() => {
   console.log("ok");
  });






};

const requireUnauthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (store.getters['auth/isAuthenticated']) {
        next('/home');
      } else {
        next();
      }
    });
};

const redirectLogout = (to, from, next) => {
  store.dispatch('auth/logout')
    .then(() => next('/login'));
};



Vue.use(Router);
export default new Router({
  mode: "history",
   saveScrollPosition: true,

  // base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "search",
      component: Search
    },
    {
      path: "/home",
      name: "home",
      component: Home,

      
    },

    {
      // with props: true, the slug parameter gets passed as a prop to the component
      path: "/question/:slug",
      name: "question",
      component: Question,
      props: true
    },
    {
      // the ? sign makes the slug parameter optional
      path: "/ask/:slug?",
      name: "question-editor",
      component: QuestionEditor,
      props: true,
      // beforeEnter: requireAuthenticated,

    },
    {
      path: "/answer/:id",
      name: "answer-editor",
      component: AnswerEditor,
      props: true,
      beforeEnter: requireAuthenticated,
    },
    {
      path: '/about',
      component: About,
      beforeEnter: requireAuthenticated,
    },
    {
      path: "/porsan",
      name: "porsan",
      component: Porsan,
      props: false
    },
    {
      path: "/login",
      name: "login",
      component: Login,
      beforeEnter: requireUnauthenticated,
    },
 
    {
      path: '/register',
      component: Register,
    },
  
    {
      path: '/password_reset',
      component: PasswordReset,
    },
  
    {
      path: '/register',
      component: Register,
    },
    {
      path: '/register/:key',
      component: VerifyEmail,
    },

    {
      path: '/logout',
      beforeEnter: redirectLogout,
    },
    {
      path: '/password_reset',
      component: PasswordReset,
    },
    {
      path: '/password_reset/:uid/:token',
      component: PasswordResetConfirm,
    },
    {
      path: '/logout',
      beforeEnter: redirectLogout,
    },
    {
      path: '/password_reset/:uid/:token',
      component: PasswordResetConfirm,
    },
    {
      path: '*',
      component: Lost,
    },
  ]
});




