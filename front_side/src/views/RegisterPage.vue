<template>
  <div class="container bg-lightgreen rounded-4 d-flex p-0 w-50 mx-auto">
    <div class="rounded-4 bg-white bienvenue d-flex flex-column">
      <h3 class="mx-auto">Espace {{ role }}</h3>
      <button type="button" class="btn btnRegister text-white w-75 m-auto rounded-3" @click="navigateToLogin">Se connecter</button>
    </div>
    <div class="d-flex flex-column w-50 gap-5 mt-5 pb-5">
      <h3>INSCRIPTION</h3>
      <form class="row g-3" @submit.prevent="submitForm">
        <div v-if="errors.wrong_credentials" class="mb-3 d-flex flex-column align-items-start text-start">
          <small class="text-danger">{{ errors.wrong_credentials }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputFirstName" class="form-label">Prénom</label>
          <input type="text" class="form-control" id="inputFirstName" name="first_name" v-model="first_name" />
          <small v-if="errors.first_name" class="text-danger">{{ errors.first_name }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputLastName" class="form-label">Nom</label>
          <input type="text" class="form-control" id="inputLastName" name="last_name" v-model="last_name" />
          <small v-if="errors.last_name" class="text-danger">{{ errors.last_name }}</small>
        </div>
        <div class="col-12 d-flex flex-column align-items-start">
          <label for="inputAddress" class="form-label">Adresse</label>
          <input type="text" class="form-control" id="inputAddress" name="address" v-model="address" />
          <small v-if="errors.address" class="text-danger">{{ errors.address }}</small>
        </div>
        <div class="col-12 d-flex flex-column align-items-start">
          <label for="inputEmail4" class="form-label">Email</label>
          <input type="email" class="form-control" id="inputEmail4" name="email" v-model="email" />
          <small v-if="errors.email" class="text-danger">{{ errors.email }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputPassword1" class="form-label">Mot de Passe</label>
          <input type="password" class="form-control" id="inputPassword1" name="password1" v-model="password1" />
          <small v-if="errors.password1" class="text-danger">{{ errors.password1 }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputPassword2" class="form-label">Confirmer Mot de Passe</label>
          <input type="password" class="form-control" id="inputPassword2" name="password2" v-model="password2">
          <small v-if="errors.password2" class="text-danger">{{ errors.password2 }}</small>
        </div>
        <div class="notification is-danger" v-if="Object.keys(errors).length">
          <p v-for="(error, index) in Object.values(errors)" :key="index">{{ error }}</p>
        </div>
        <div class="col-12">
          <button type="submit" class="btn btnRegister text-white w-100 rounded-3">Créer un compte</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  props: ['role'],
  data() {
    return {
      first_name: '',
      last_name: '',
      address: '',
      email: '',
      password1: '',
      password2: '',
      errors: {
        first_name: '',
        last_name: '',
        address: '',
        email: '',
        password1: '',
        password2: '',
        wrong_credentials: '',
      },
    };
  },
  mounted() {
    document.title = 'Register | EduCool' 
  },
  methods: {
    navigateToDashboard() {
      this.$router.push({
        name: 'DashboardPage',
        params: {
          role: this.role,
        }
      });
    },
    navigateToLogin() {
      this.$router.push({ name: 'LoginPage', params: { role: this.role } });
    },
    submitForm() {

      this.errors = {};

      if (!this.first_name) {
        this.errors.first_name = "Le prénom est requis.";
      }
      if (!this.last_name) {
        this.errors.last_name = "Le nom est requis.";
      }
      if (!this.address) {
        this.errors.address = "L'adresse est requise.";
      }
      if (!this.email) {
        this.errors.email = "L'email est requis.";
      }
      if (!this.password1) {
        this.errors.password1 = "Le mot de passe est requis.";
      }
      if (!this.password2) {
        this.errors.password2 = "La confirmation du mot de passe est requise.";
      }
      if (this.password1 !== this.password2) {
        this.errors.password2 = "Les mots de passe ne correspondent pas.";
      }

      if (Object.keys(this.errors).length > 0) {
        return;
      }

      const formData = {
        first_name: this.first_name,
        last_name: this.last_name,
        address: this.address,
        email: this.email,
        password1: this.password1,
        password2: this.password2
      };


      axios.post(`/${this.role}/register/`, formData, {
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
          if (error.response && error.response.data && error.response.data.message) {
            this.errors.wrong_credentials = error.response.data.message;
          } else {
            this.errors.wrong_credentials = "Une erreur est survenue lors de la connexion.";
          }
        });
    }
  }
};
</script>

<style>
.container {
  margin-top: 6rem;
}

.bg-lightgreen { 
  background-color: #61E294;
}

.btnRegister:hover{
    background-color: #1fa3b5;
}

.btnRegister {
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
