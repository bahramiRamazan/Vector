<template>
  <div class="page">

    <div bmt-12>
  </div>
      <BaseLayout>
      <template v-slot:right>
   <b-card bg-variant="light">

       <b-form-group
      label-cols-lg="3"
      label="ثبت نام"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
    >
  <div id="register-view">

    <template v-if="registrationLoading">
      loading...
    </template>
    <template v-else-if="!registrationCompleted">


      <b-form-group 
      label-cols-lg="3"
      label="نام کاربری"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
      
      
      @submit.prevent="submit">
        <b-form-input v-model="inputs.username" type="text" id="username" placeholder="نام کاربری"></b-form-input>
        </b-form-group> 
      <br>
      <b-form-group 
      label-cols-lg="3"
      label=" پسورد"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
      
      
      @submit.prevent="submit">
        <b-form-input v-model="inputs.password1" type="password" id="password1" placeholder="پسورد"></b-form-input>
       </b-form-group> 

       <br>
       <b-form-group 
      label-cols-lg="3"
      label=" پسورد تکرار"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
       
       @submit.prevent="submit">
        <b-form-input v-model="inputs.password2" type="password" id="password2"
          placeholder="confirm password"></b-form-input>
        </b-form-group> 
       <br>

       <b-form-group 
      label-cols-lg="3"
      label="  آدرس ایمیل"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
       
       @submit.prevent="submit">
        <b-form-input v-model="inputs.email" type="email" id="email" placeholder="آدرس ایمیل"></b-form-input>
   </b-form-group> 


         <b-form-group 
      label-cols-lg="3"
      label="   mobil"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
       
       @submit.prevent="submit">
        <b-form-input v-model="inputs.mobil" type="text" id="mobil" placeholder="mobile "></b-form-input>
   </b-form-group> 

         <b-form-group 
      label-cols-lg="3"
      label="   language_prefered"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
       
       @submit.prevent="submit">
        <b-form-input v-model="inputs.language_prefered" type="text" id="language_prefered" placeholder="language_prefered"></b-form-input>
   </b-form-group> 


     

         <br>
      
      <b-button  @click="createAccount(inputs)">
        create account
    </b-button>
      <span class="error" v-show="registrationError">
        An error occured while processing your request.
      </span>
      <div>
        Already have an account?
        <router-link to="/login">login</router-link> |
        <router-link to="/password_reset">reset password</router-link>
      </div>
    </template>
    <template v-else>
      <div>
        Registration complete. You should receive an email shortly with instructions on how to
        activate your account.
      </div>
      <div>
        <router-link to="/login">return to login page</router-link>
      </div>
    </template>
  </div>
    </b-form-group>
    </b-card>
      </template>
    </BaseLayout>
  </div>
</template>

<script>
import BaseLayout from "@/components/BaseLayout.vue";
import { mapActions, mapState } from 'vuex';

export default {
    name: "about",
  components: {
    BaseLayout
  },
  data() {
    return {
      inputs: {
        username: '',
        password1: '',
        password2: '',
        email: '',
        mobil:'',
        language_prefered:'',
    
      },
    };
  },
  computed: mapState('signup', [
    'registrationCompleted',
    'registrationError',
    'registrationLoading',
  ]),
  methods: mapActions('signup', [
    'createAccount',
    'clearRegistrationStatus',
  ]),
  beforeRouteLeave(to, from, next) {
    this.clearRegistrationStatus();
    next();
  },
};
</script>

<style>
form input {
  display: block
}

.error {
  color: crimson;
  font-size: 12px;
}
</style>
