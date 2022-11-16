<template>
  <div class="page">

    <div bmt-12>
  </div>

    
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
        <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="آدرس ایمیل:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
        style="text-align: justify;"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required
          
        ></b-form-input>
      </b-form-group>

      <b-form-group  style="text-align: justify;" id="input-group-2" label="Your Name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.name"
          placeholder="Enter name"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group style="text-align: justify;"  id="input-group-3" label="Food:" label-for="input-3">
        <b-form-select
          id="input-3"
          v-model="form.food"
          :options="foods"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }">
        <b-form-checkbox-group
          v-model="form.checked"
          id="checkboxes-4"
          :aria-describedby="ariaDescribedby"
        >
          <b-form-checkbox value="me">Check me out</b-form-checkbox>
          <b-form-checkbox value="that">Check that out</b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>

       
      </template>
    </BaseLayout>
  </div>
</template>

<script>
// @ is an alias to /src
import BaseLayout from "@/components/BaseLayout.vue";
import { requestsMixin } from "@/mixins/requestsMixin";
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
      
 form: {
          email: '',
          name: '',
          food: null,
          checked: []
        },
        foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        show: true



    };
  },
  beforeMount() {
    this.getAllArticles();
  },
  methods: {
    async getAllArticles() {
      const response = await this.getArticles(this.selectedSection);
      this.articles = response.data.results;
    },
    setSection() {
      this.getAllArticles();
    },
          onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },


 onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.food = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }








  }
};
</script>
<style scoped>
#section-dropdown {
  margin-bottom: 10px;
}
</style>