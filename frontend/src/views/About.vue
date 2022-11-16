<template>
  <div class="page">
    <h1 class="text-center">Search</h1>
    <SearchLayout>
      <template v-slot:top>
        <ValidationObserver ref="observer" v-slot="{  }">
          <b-form @submit.prevent="onSubmit" novalidate id="form">
            <b-form-group label="keyword" label-for="keyword">
              <ValidationProvider name="keyword" rules="required" v-slot="{ errors }">
                <b-form-input
                  :state="errors.length == 0"
                  v-model="form.keyword"
                  type="text"
                  required
                  placeholder="Keyword"
                  name="keyword"
                ></b-form-input>
                <b-form-invalid-feedback :state="errors.length == 0">Keyword is required</b-form-invalid-feedback>
              </ValidationProvider>
            </b-form-group>
            <b-button type="submit" variant="primary">Search</b-button>
          </b-form>
        </ValidationObserver>
      </template>
<template v-slot:bottom>
         <div class="container ">
           <br>
    
      <div v-for="question in questions"
           :key="question.pk">
      

      <b-card
          header-tag="header"
          header-bg-variant="dark"

          footer-tag="footer"
           footer-bg-variant="success"
          footer-border-variant="dark"
          title="سوال نمونه"
          style="text-align: justify;"
        >
       <b-card-text>
          <router-link
            :to="{ name: 'question', params: { slug: question.slug } }"
            class="question-link question d-flex justify-content-between"
            >{{ question.content }}
          </router-link>
        </b-card-text>
    <b-card-footer variant="success" >
      <span class="question-author ">{{ question.author }}
        <b-avatar size="sm" variant="info">
        </b-avatar>
        </span>
        <b-avatar size="sm" variant="success" >{{ question.answers_count }}</b-avatar>
    </b-card-footer>
  </b-card>

      
      </div>
      <div class="my-4 ">
        <p v-show="loadingQuestions">...loading...</p>
        <button
          v-show="next"
          @click="getQuestions"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>

</div>

      </template>
    </SearchLayout>
  </div>
</template>
<script>
// @ is an alias to /src
// @ is an alias to /src
import SearchLayout from "@/components/SearchLayout.vue";
import { requestsMixin } from "@/mixins/requestsMixin";
import { apiService } from "@/common/api.service.js";
export default {
  name: "about",
  components: {
    SearchLayout
  },
  mixins: [requestsMixin],
  data() {
    return {
      sections: `arts, automobiles, books, business, fashion,
      food, health, home, insider, magazine, movies, national,
      nyregion, obituaries, opinion, politics, realestate, science,
      sports, sundayreview, technology, theater,
      tmagazine, travel, upshot, world`
        .split(",")
        .map(s => s.trim()),
      selectedSection: "arts",
      articles: [],
    
      form: {},
            questions: [],
      next: null,
      loadingQuestions: false
    };
  },
  beforeMount() {

  },
  methods: {


    async onSubmit() {
         const isValid = await this.$refs.observer.validate();
      if (!isValid) {
        return;
      }
     
  else {
    
 
      // let endpoint = `/api/questions/${this.slug}/answers/`;this.form.keyword
      // let endpoint = `/api/questions/keyword:${this.form.keyword}/search/`;
      let endpoint = `/api/questions/search/${this.form.keyword}/`;
      // let endpoint = `/api/get-token/`;

           if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
        .then(data => {
    
          this.questions.push(...data.results)
          this.loadingQuestions = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })

      }
    },
  





    async getAllArticles() {
      // const response = await this.getArticles(this.selectedSection);
      // this.articles = response.data.results;
    },
    setSection() {
      // this.getAllArticles();
    },
        getQuestions() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results)
          this.loadingQuestions = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },  
    created() {
  
  }
  }
};
</script>
<style scoped>
</style>