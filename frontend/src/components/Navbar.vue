<template>
  
<nav class="navbar cst  navbar-expand-md fixed-top mb-3">
    <div class="container-fluid  ">
       
        <button type="button" class="navbar-toggler bt" data-toggle="collapse" data-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">

            <div class="navbar-nav col-md-3  ">
            <router-link 
              :to="{ name: 'porsan' }" 
              class="btn btn-sm txt"
              >Register
            </router-link>
 
                      <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/"
              >Logout
            </a>
          </li>
    
            </div>
            <div class="navbar-nav col-md-6 ">
        
            <div class="input-group">                    
                <input type="text" size="sm" class="form-control " placeholder="پرسان را جستجو کنید">
                <div class="input-group-append">
                    <button type="button" variant="success" class="btn btn-secondary"><i class="fa fa-search"></i></button>
                </div>
            </div>
    
         </div>
         <div class="navbar-nav txt ml-auto">
            <router-link 
              :to="{ name: 'question-editor' }" 
              class="btn btn-lg btn-danger porsan"
              >بپرسید
            </router-link>
            </div>
            <div class="navbar-nav txt ml-auto">
            <router-link 
              :to="{ name: 'home' }" 
              class="btn btn-sm porsan"
              >پرسان
            </router-link>
              
 
            </div>
        </div>
    </div>    
</nav>



</template>
    <!-- JS files: jQuery first, then Popper.js, then Bootstrap JS -->

<style scoped>
.cst{
    background-color: rgb(7, 125, 146);
    color: rgb(33, 36, 212);
    
}
.txt{
    color: rgb(255, 255, 255);
    font-family: 'Times New Roman', Times, serif,Bold;
    
    
}
.porsan{
    color: rgb(255, 255, 255);
    font-family: "Arabic Typesetting", serif, Bold;
    font-size:20px;
    
    
}


</style>