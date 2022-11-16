<template>
  <div class="page">
    <div bmt-12>
    </div>

    <BaseLayout>
      <template v-slot:right>
            <b-card bg-variant="light">
  <div class="container mt-2">
    <h1 class="mb-3">Ask a Question</h1>
    <form @submit.prevent="onSubmit">
      <textarea
        v-model="question_body"
        class="form-control"
        placeholder="What do you want to ask?"
        rows="3"
      ></textarea>
  <br>



 <b-form-file
      v-model="question_image"
      :state="Boolean(file1)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
    <div class="mt-3">Selected file: {{ file1 ? file1.name : '' }}</div>

  

  
      <br>


  <!-- <input type="file" accept="image/*" @change="onChange" />
  <div id="preview">
    <img v-if="item.imageUrl" :src="item.imageUrl" />
  </div>

 -->

  <div v-if="!question_image">
    <h2>Select an image</h2>
    <input type="file" @change="onFileChange">
  </div>
  <div v-else>
    <img :src="question_image" />
    <button @click="removeImage">Remove image</button>
  </div>













      <button
        type="submit"
        class="btn btn-success"
        >Publish
      </button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
          </b-card>
      </template>
    </BaseLayout>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import BaseLayout from "@/components/BaseLayout.vue";
export default {
      components: {
    BaseLayout
  },
  name: "QuestionEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
       file1: null,
       
            item:{
          //...
          image : null,
          imageUrl: null
      },
      question_image:'',
        question_body:'',
 
      error: null
    }
  },
  methods: {

   onChange(e) {
      const file = e.target.files[0]
      this.image = file
      this.item.imageUrl = URL.createObjectURL(this.image)
    
  },
 





onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
    },
    createImage(file) {                                               
    
      var reader = new FileReader();
      var vm = this;

      reader.onload = (e) => {
        vm.question_image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function () {
      this.question_image = '';
    },
    onSubmit() {
      // Tell the REST API to create or update a Question Instance
        const formData = new FormData();
        // formData.append("question_image", this.image);
         formData.append('question_image', this.question_image)

 
      if (!this.question_body) {
        this.error = "You can't send an empty question!";
      } else if (this.question_body.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/questions/";
        let method = "POST"; 
        if (this.slug !== undefined) {
          endpoint += `${ this.slug }/`;
          method = "PUT";
        }     
        apiService(endpoint, method, { content: this.question_body, question_image:this.question_image})
          .then(question_data => {
            this.$router.push({ 
              name: 'question', 
              params: { slug: question_data.slug }
            })          
          })  
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.slug !== undefined) {
      let endpoint = `/api/questions/${ to.params.slug }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.question_body = data.content))
    } else {
      return next();
    }   
  },
  created() {
    document.title = "Editor - QuestionTime";
  }  
}
</script>
