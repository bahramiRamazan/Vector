import auth from '../api/auth';
import session from '../api/session';
import { apiService } from "@/common/api.service.js";
// import { apiService } from "@/common/api.service.js";
import {
  LOGIN_BEGIN,
  LOGIN_FAILURE,
  LOGIN_SUCCESS,
  SET_PREFERENCE,
  LOGOUT,
  REMOVE_TOKEN,
  SET_TOKEN,
} from './types';

const TOKEN_STORAGE_KEY = 'TOKEN_STORAGE_KEY';
const isProduction = process.env.NODE_ENV === 'production';

const initialState = {
  authenticating: false,
  error: false,
  token: null,
  language_prefered:"",
  flag:true,
  
};

const getters = {
    isAuthenticated: state => !!state.token,
    authStatus: state => state.status,
    language_prefered: state=>state.language_prefered,
    flag:state=>state.flag,

};



const actions = {
    login({ commit }, { username, password }) {
              commit(LOGIN_BEGIN);
               return auth.login(username, password)
                    .then(({ data }) => commit(SET_TOKEN, data.key))
                    .then(() => commit(LOGIN_SUCCESS))
                    .catch(() => commit(LOGIN_FAILURE));
  },


  logout({ commit }) {
      return auth.logout()
          .then(() => commit(LOGOUT))
          .finally(() => commit(REMOVE_TOKEN));
  },

  initialize({ commit }) {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY);

        if (isProduction && token) {
          commit(REMOVE_TOKEN);
          
        }

        if (!isProduction && token) {
          commit(SET_TOKEN, token);
        
          
        }
  },


  googlelogin({ commit }) {
          var name="csrftoken";
          var cookieValue = null;
          if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
              var cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
              }
            }
          }
      var CSRF_TOKEN = cookieValue;
  
      console.log(CSRF_TOKEN)
          

          const token = CSRF_TOKEN;

          if (isProduction && token) {
            console.log("not");
            commit(REMOVE_TOKEN);
          }

          if (!isProduction && token) {
            commit(SET_TOKEN, token);
            console.log("notyes");
          }
  },

  set_preference({ commit }, {lang}) {
    console.log("this is to test");
    console.log(lang);
    commit(SET_PREFERENCE, lang);

  },

  set_preference2({ commit }) {
    

      
    let endpoint = `/api/preference/${this.language_prefered}/change/`;
    apiService(endpoint, "get").then(data => {
        if (data) {
      // this.language_prefered=data.language_prefered;

      commit(SET_PREFERENCE, data.language_prefered);
  
      
      
        } 

      })

}




};



const mutations = {

  [SET_PREFERENCE](state, lang) {
    console.log("test");
   state.language_prefered=lang;
   if(lang=="english"){
   state.flag=false;}
   else {state.flag=true;}
    },
  

  [LOGIN_BEGIN](state) {
    state.authenticating = true;
    state.error = false;
  },

  [LOGIN_FAILURE](state) {
    state.authenticating = false;
    state.error = true;
  },

  [LOGIN_SUCCESS](state) {
    state.authenticating = false;
    state.error = false;
  },

  [LOGOUT](state) {
    state.authenticating = false;
    state.error = false;
  },

  [SET_TOKEN](state, token) {
    if (!isProduction) localStorage.setItem(TOKEN_STORAGE_KEY, token);
    session.defaults.headers.Authorization = `Token ${token}`;
    state.token = token;
  },
  
  [REMOVE_TOKEN](state) {
    localStorage.removeItem(TOKEN_STORAGE_KEY);
    delete session.defaults.headers.Authorization;
    state.token = null;
   
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
