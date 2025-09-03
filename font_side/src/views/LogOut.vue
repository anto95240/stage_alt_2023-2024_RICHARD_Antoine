<template>
    <div class="container bg-lightgreen rounded-4 d-flex p-0 w-50 justify-content-center">
      <div class="d-flex flex-column w-50 gap-5 mt-5 pb-5">
        <h3>Vous avez été déconnecter</h3>
        <button class="btn btnDeco rounded-3" @click="navigateToHome">Se connecter</button>
      </div>        
    </div>
  </template>

<script>
  export default {
    name: 'LogOut',
    props: ['role'],
    mounted() {
      document.title = 'Logout | EduCool'
    },
    methods: {
      navigateToHome() {
        this.$router.push({ name: 'HomePage', params: { role: this.role } });
      }
    }
  }
</script>

<style>
.container {
  margin-top: 12rem;
}

.bg-lightgreen { 
  background-color: #61E294;
}

.btnDeco:hover{
    background-color: #1fa3b5;
}

.btnDeco{
    background-color: #00B2CA;
    box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
}

.bienvenue {
  width: 35%;
  box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.25);
  margin-right: 10%;
  padding-top: 5rem !important;
}

.form-control {
  width: 200%;
}
</style>