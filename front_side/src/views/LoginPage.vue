<template>
  <div class="container bg-lightgreen rounded-4 d-flex p-0 w-50">
    <div class="rounded-4 bg-white bienvenue d-flex flex-column">
      <h3 class="mx-auto">Espace {{ role }}</h3>
      <button type="button" class="btn btnLogin text-white w-75 m-auto rounded-3" @click="navigateToRegister">Créer un compte</button>
    </div>
    <div class="d-flex flex-column w-50 gap-5 mt-5 pb-5">
      <h3>CONNEXION</h3>
      <form class="row g-3" @submit.prevent="submitForm">
        <div v-if="errors.wrong_credentials" class="mb-3 d-flex flex-column align-items-start text-start">
          <small class="text-danger">{{ errors.wrong_credentials }}</small>
        </div>
        <div class="mb-3 d-flex flex-column align-items-start text-start">
          <label for="exampleFormControlInput1" class="form-label">Email</label>
          <input type="email" class="form-control" id="exampleFormControlInput1" name="email" v-model="email">
          <small v-if="errors.email" class="text-danger">{{ errors.email }}</small>
        </div>
        <div class="mb-3 d-flex flex-column align-items-start text-start">
          <label for="inputPassword5" class="form-label">Mot de Passe</label>
          <input type="password" id="inputPassword5" class="form-control" aria-describedby="PasswordHelpBlock" name="password" v-model="password">
          <small v-if="errors.password" class="text-danger">{{ errors.password }}</small>
        </div>
        <div class="col-12">
          <button type="submit" class="btn btnLogin text-white w-100 rounded-3">Se connecter</button>
        </div>
      </form>
    </div>        
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  props: ['role'],
  data() {
    return {
      email: "",
      password: "",
      errors: {
        email: "",
        password: "",
        wrong_credentials: "",
      }
    }
  },
  methods: {
    submitForm() {
      this.errors = {
        email: "",
        password: "",
        wrong_credentials: ""
      };

      if (!this.email) {
        this.errors.email = "L'email est requis.";
        return;
      }
      if (!this.password) {
        this.errors.password = "Le mot de passe est requis.";
        return;
      }

      axios.post(`/login/`, {
        email: this.email,
        password: this.password
      }, {
        withCredentials: true
      })
      .then(response => {
        if (response.data.success) {

          this.navigateToDashboard();
        } else {
          this.errors.wrong_credentials = "email ou mot de passe incorrect.";
        }
      })
      .catch(error => {
        console.error('Une erreur est survenue lors de la connexion.', error);
        this.errors.wrong_credentials = "Une erreur est survenue lors de la connexion.";
      });
    },
    navigateToDashboard() {
      this.$router.push({
        name: 'DashboardPage',
        params: {
          role: this.role,
        }
      });
    },
    navigateToRegister() {
      this.$router.push({
        name: 'RegisterPage',
        params: {
          role: this.role
        }
      });
    }
  }
};
</script>

<style>
.container {
  margin-top: 12rem;
}

.bg-lightgreen { 
  background-color: #61E294;
}

.btnLogin:hover{
    background-color: #1fa3b5;
}

.btnLogin{
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
  width: 100% !important;
  background-color: white;
  padding: 12px;
}
</style>
