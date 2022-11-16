<template>
  <b-container fluid>

  
     <b-row class="text-center">
      <b-col  class="">
    
        <div class="d-block d-sm-none d-none d-sm-block d-md-block d-lg-none ">
          <slot name="section-dropdown"></slot>
        </div>
        <div class=" d-none d-lg-block d-xl-none d-xl-block">
        <slot name="left"></slot>
      </div>
      </b-col>
     
      <b-col  class="col-12 col-lg-8" >
        <slot name="right"></slot>
      </b-col>
      <b-col>سلات سمت راست</b-col>
    </b-row>
</b-container>
</template>
<script>
export default {
  name: "BaseLayout"
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>