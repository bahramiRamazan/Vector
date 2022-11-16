<template>
  <div class="page">
  
    <BaseLayout>
      <template v-slot:left>
        <b-nav vertical pills>
          <b-nav-item
            v-for="s in sections"
            :key="s"
            :active="s == selectedSection"
            @click="selectedSection = s; getAllArticles()"
          >{{s}}</b-nav-item>
        </b-nav>
      </template>
      <template v-slot:section-dropdown>
        <b-form-select
          v-model="selectedSection"
          :options="sections"
          @change="getAllArticles()"
          id="section-dropdown"
        ></b-form-select>
      </template>

      
      <template v-slot:right>
     <div class="container ">


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
  <br>

      
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
    </BaseLayout>
  </div>
</template>
<script>
// @ is an alias to /src
import BaseLayout from "@/components/BaseLayout.vue";
import { requestsMixin } from "@/mixins/requestsMixin";
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  components: {
    BaseLayout
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
            questions: [],
      next: null,
      loadingQuestions: false
    };
  },
  beforeMount() {
    this.getAllArticles();
        this.getQuestions()
    document.title = "AlefYa";
  },
  methods: {
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

    getpreference() {
      // make a GET Request to the questions list endpoint and populate the questions array
  
    }, 
    created() {
    this.getQuestions()
    document.title = "AlefYa";
  }
  }
};
</script>
<style scoped>
#section-dropdown {
  margin-bottom: 10px;
}
.question{
  /* direction: rtl; text-align: justify;  */
      font-family: "Iran Yekan";
    /* font-size: 10px; */
    color:black;
    font-size:1.1rem;

}
.questions-cnt{
  /* float:left; */
  border:0cm;
  font-size:0.8rem;
}
</style>