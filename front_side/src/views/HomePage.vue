<template>
  <div class="container bg-lightgreen rounded-4 d-flex p-0 w-50">
    <div class="rounded-4 bg-white bienvenue">
      <h3>Bienvenue</h3>
    </div>
    <div class="d-flex flex-column w-25 gap-5 mt-5 pb-5">
      <button type="button" class="btn text-white rounded-3" @click="navigateToLogin('student')">Étudiant</button>
      <button type="button" class="btn text-white rounded-3" @click="navigateToLogin('teacher')">Intervenant</button>
    </div>        
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    navigateToLogin(role) {
      this.$router.push({ name: 'LoginPage', params: { role } });
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

.btn:hover{
    background-color: #1fa3b5;
}

.btn{
    background-color: #00B2CA;
    box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
}

.bienvenue {
  width: 50%;
  box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.25);
  text-align: center;
  padding-top: 5rem !important;
}
</style>
