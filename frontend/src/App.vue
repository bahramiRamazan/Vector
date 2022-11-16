<template>
          <div v-bind:class="{ circle: flag, square: !flag }"
                 >
  
<b-nav class="navbar cst  navbar-expand-md fixed-top mb-3">
  <b-navbar-brand href="#">
    </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
         <b-collapse id="nav-collapse" is-nav>
             
            <div class="navbar-nav txt ml-auto">
             <router-link 
              :to="{ name:'home' }" 
              class="btn  btn-sm btn-outline"> <div class="porsan"><h4>  <b-icon icon="question-square" aria-hidden="true"></b-icon> {{home[language_prefered]}}</h4></div>
             </router-link>
            </div>
<!-- 
             <div class="navbar-nav txt ml-auto">
            <router-link  class="btn  btn-sm btn-outline" to="/register">
            ثبت
            </router-link> |
            </div> -->

           <div class="navbar-nav txt ml-auto">
            <router-link 
              :to="{ name:'porsan' }" 
              class="btn  btn-sm btn-outline"> <b-icon icon="card-text" aria-hidden="true"></b-icon> {{about[language_prefered]}}
            </router-link>
            </div>


            <div class="navbar-nav txt ml-auto">
            <router-link 
              :to="{ name:'search' }" 
              class="btn  btn-sm btn-outline"> <div class="porsan"><b-icon icon="search" aria-hidden="true"></b-icon>{{search[language_prefered]}} </div>
            </router-link>
            </div>
    
 

             <div class="navbar-nav txt ml-auto">
              <router-link class="btn  btn-sm btn-outline" to="/about">
              <b-icon icon="envelope" aria-hidden="true"></b-icon>
              {{contact[language_prefered]}}
              </router-link>
            </div>

           <div class="navbar-nav txt ml-auto">
            <router-link 
              :to="{ name: 'question-editor' }" 
              class="btn  btn-sm btn-outline"> <div class="porsan"><b-icon icon="vector-pen" aria-hidden="true"></b-icon>&nbsp;&nbsp;{{ask[language_prefered]}}</div>
            </router-link>
            </div>


<!--       
          <li class="nav-item">
            <a class="btn btn-sm btn-outline-info" href="/accounts/logout/"
              >Logout
            </a>
          </li> -->

            <div class="bnavbar-nav col-md-4 ">                   
            </div>
            
  
<div class="navbar-nav txt ml-auto">
      <b-dropdown variant="danger" >
        <template #button-content>
          <b-icon icon="gear-fill" aria-hidden="true"></b-icon> {{settings[language_prefered]}}
        </template>
        <b-dropdown-item-button>
          <b-icon icon="lock-fill" aria-hidden="true"></b-icon>
          Change Password <span class="sr-only">(Click to unlock)</span>
        </b-dropdown-item-button>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-group header="Choose options" class="small">
          <b-dropdown-item-button v-on:click="changelanguage('dari')"  > 
            <b-icon icon="blank" aria-hidden="true"></b-icon>
            Dari <span class="sr-only">(Not selected)</span>
          </b-dropdown-item-button>
          <b-dropdown-item-button v-on:click="changelanguage('pashtu')" >
            <b-icon  icon="check" aria-hidden="true"></b-icon>
            Pashtu <span class="sr-only">(Selected)</span>
          </b-dropdown-item-button  >
          <b-dropdown-item-button v-on:click="changelanguage('english')" >
            <b-icon icon="blank" aria-hidden="true"></b-icon>
            English <span class="sr-only">(Not selected)</span>
          </b-dropdown-item-button>
        </b-dropdown-group>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item-button>

          <li class="nav-item">
     
            <router-link class="btn  btn-sm btn-outline" to="/login">
                ورود
          </router-link>
        </li>
        </b-dropdown-item-button>


                <b-dropdown-item-button>

          <li class="nav-item">
            <router-link class="btn  btn-sm btn-outline" to="/logout">
                خروج
          </router-link>
         
        </li>
        </b-dropdown-item-button>


        
        <b-dropdown-item-button>Some other action</b-dropdown-item-button>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item-button variant="danger">
          <b-icon icon="trash-fill" aria-hidden="true"></b-icon>
          Delete
        </b-dropdown-item-button>
      </b-dropdown>
    </div>
  </b-collapse>
  </b-nav>



     <div class="cmt ">
       </div>


    <router-view />


    

  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import { mapActions } from 'vuex';
import { apiService } from "@/common/api.service.js";
import store from './store';
// import SET_PREFERENCE from './store';

export default {
props: {


  },
  data() {

    return {
      path: this.$route && this.$route.path,
      fontSize: 10,

  
      
       name: 'Vue.js',
       styleObject: { },
       home:{
         english:"Home",
         dari:"خانه",
         pashtu:"کور"
       },
        contact:{
         english:"Contact",
         dari:"ارتباط",
         pashtu:"الیکه"
       },
       search:{
         english:"Search",
         dari:"جستجو",
         pashtu:"لتول"
       },
      ask:{
         english:"Ask",
         dari:"پرسید",
         pashtu:"پوختنه"
       },
      about:{
         english:"About",
         dari:"درباره",
         pashtu:" دپاره"
       },
      settings:{
         english:"Settings",
         dari:"تنظیمات",
         pashtu:"دکمه گان"
       }

 
    };
  },
  watch: {
    $route(route) {
      this.path = route.path;
      
    },
    
   
  },

  

      methods: {

      async get_preference() {
        // this.language_prefered="undefined";
    
      let endpoint = `/api/preference/${this.language_prefered}/change/`;
      apiService(endpoint, "get").then(data => {
          if (data) {
        // this.language_prefered=data.language_prefered;

        if (this.language_prefered=="dari")
        {
                       this.language_set("dari");
              
        }
      
      if (this.language_prefered=="pashtu" )
      {
          
                this.language_set("pashtu");
      }
      
      if (this.language_prefered=="english" )
      {
           
                this.language_set("english");


      }
    
        
        
          } 

        })
  
    },


    changelanguage: function (language) {

              let endpoint = `/api/preference/${language}/change/`;
              apiService(endpoint, "post").then(data => {
                  if (data) {
                  
              
              if (data.language_prefered=="dari")
              {
                this.language_set("dari");
               
                // location.reload();
              }
              
              if (data.language_prefered=="pashtu" ){
               
                this.language_set("pashtu");}
                // location.reload();}
              
              if (data.language_prefered=="english" ){
                
                this.language_set("english");}
                // location.reload();
          } 
        })
    },

 language_set: function (language) {


          store.dispatch('auth/set_preference', {
            lang: language
          }).then(() => {
        console.log("success")
          });
 }




    },
   computed: 
   {
     ...mapGetters('auth', ['isAuthenticated', 'language_prefered','flag']),
   
   ...mapActions({
      set_preference: 'set_preference2' // map `this.add()` to `this.$store.dispatch('increment')`
    })
   
   },

    created() {
    this.get_preference();
     store.dispatch('auth/set_preference2')
  .then(() => {
  console.log("ok");
  
  });
 
  },
    beforeMount () {
      this.get_preference();

    }
};

</script>
<style scoped>


.page {
  padding: 20px;
}
.cst{
    background-color: rgb(226, 135, 67)

}
.searchbox{
    background-color:rgb(197, 197, 207);
    padding-bottom: 1px;
    padding-right: 0px;
    border-color:  rgb(88, 145, 219);
  
}
.searchbox::placeholder {
  color: rgb(106, 106, 110); 
text-align:center;
letter-spacing: 1px;
 font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
 padding-left:50px;
 padding-right:50px;
 font-size: 0.9em;
font-family: 'Helvetica', FontAwesome, sans-serif;

}
  
.btnhome{
      /* padding-left: 1px; */
  
}
.scolor{
  background-color: rgb(8, 112, 231);
  border:salmon;
  shape-outside: ellipse();
}
.scolord{
  font-size: 1.9em;

  font-family: 'Times New Roman', Times, serif,Bold;
  color:rgb(5, 238, 25);
}
.porsan{
  
  /* padding-right: 15px; */
}

.cmt {
  margin-top: 10%;

}

.circle {

 direction: rtl;
}
.square {

 direction: ltr;
}

</style>