<template>
  <b-container fluid>

  
     <b-row class="text-center">
      <b-col>
        <div class="d-block d-sm-none d-none d-sm-block d-md-block d-lg-none">
          <slot name="section-dropdown"></slot>
        </div>
        <slot name="left"></slot>
      </b-col>
      <b-col cols="8">
        <slot name="right"></slot>
      </b-col>
      <b-col>
<div>
  <b-alert show variant="success">
    <h4 class="alert-heading">Well done!</h4>
    <p>
      Aww yeah, you successfully read this important alert message.
    </p>

  </b-alert>
</div>


        
      </b-col>
    </b-row>


       <b-row class="text-center">
      <b-col>
        <div class="d-block d-sm-none d-none d-sm-block d-md-block d-lg-none">
          <slot name="section-dropdown"></slot>
        </div>
        <slot name="leftbottom">left bottom</slot>
      </b-col>
      <b-col cols="8">
        <slot name="rightbottom"></slot>
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