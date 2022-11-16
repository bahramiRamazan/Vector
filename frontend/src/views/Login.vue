<template>
  <div class="page">
    <div bmt-12>
    </div>

    <BaseLayout>
      <template v-slot:right>
            <b-card bg-variant="light">
  <div id="login-view">
    <h1>Login</h1>
    <form @submit.prevent="submit">
      <input v-model="inputs.username" type="text" id="username" placeholder="username">
      <input v-model="inputs.password" type="password" id="password" placeholder="password">
    </form>
    <button @click="login(inputs)" id="login-button">
      login
    </button>
      <button @click="auth()" id="login-button">
      log
    </button>
    <div>
 
      <router-link to="/register">create account</router-link> |
      <router-link to="/password_reset">reset password</router-link>
        <li class="nav-item">
            <a class="btn btn-sm btn-outline-info" href="/login/google-oauth2/">
              GoolgeLogin
            </a>
          </li>
<!--   
      <a href="{% url "social:begin" "google-oauth2" %}">Google+</a> -->
    </div>
  </div>
         </b-card>
      </template>
    </BaseLayout>
  </div>
</template>
<script>
import BaseLayout from "@/components/BaseLayout.vue";
export default {
      components: {
    BaseLayout
  },
  data() {

    return {
      inputs: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    login({ username, password }) {
      this.$store.dispatch('auth/login', { username, password })
        .then(() => this.$router.push('/'));
    },
    auth() {
      this.$store.dispatch('auth/googlelogin', )
        .then(() => this.$router.push('/'));
    },
  },
};
</script>

<style>
form input {
  display: block
}
</style>
