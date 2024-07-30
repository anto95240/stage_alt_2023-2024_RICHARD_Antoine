<template>
  <div class="container bg-lightgreen rounded-4 d-flex p-0 w-50 mx-auto">
    <div class="rounded-4 bg-white bienvenue d-flex flex-column">
      <h3 class="mx-auto">Espace {{ role }}</h3>
      <template v-if="role !== 'admin'">
        <button type="button" class="btn text-white w-75 m-auto rounded-3" @click="navigateToLogin">Se connecter</button>
      </template>
    </div>
    <div class="d-flex flex-column w-50 gap-5 mt-5 pb-5">
      <h3>INSCRIPTION</h3>
      <form class="row g-3" @submit.prevent="submitForm">
        <div v-if="errors.wrong_credentials" class="mb-3 d-flex flex-column align-items-start text-start">
          <small class="text-danger">{{ errors.wrong_credentials }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputFirstName" class="form-label">Prénom</label>
          <input type="text" class="form-control" id="inputFirstName" name="FirstName" v-model="FirstName" />
          <small v-if="errors.FirstName" class="text-danger">{{ errors.FirstName }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputLastName" class="form-label">Nom</label>
          <input type="text" class="form-control" id="inputLastName" name="LastName" v-model="LastName" />
          <small v-if="errors.LastName" class="text-danger">{{ errors.LastName }}</small>
        </div>
        <div class="col-12 d-flex flex-column align-items-start">
          <label for="inputAddress" class="form-label">Adresse</label>
          <input type="text" class="form-control" id="inputAddress" name="Address" v-model="Address" />
          <small v-if="errors.Address" class="text-danger">{{ errors.Address }}</small>
        </div>
        <div class="col-12 d-flex flex-column align-items-start">
          <label for="inputEmail4" class="form-label">Email</label>
          <input type="email" class="form-control" id="inputEmail4" name="Email" v-model="Email" />
          <small v-if="errors.Email" class="text-danger">{{ errors.Email }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputPassword1" class="form-label">Mot de Passe</label>
          <input type="password" class="form-control" id="inputPassword1" name="Password1" v-model="Password1" />
          <small v-if="errors.Password1" class="text-danger">{{ errors.Password1 }}</small>
        </div>
        <div class="col-md-6 d-flex flex-column align-items-start">
          <label for="inputPassword2" class="form-label">Confirmer Mot de Passe</label>
          <input type="password" class="form-control" id="inputPassword2" name="Password2" v-model="Password2">
          <small v-if="errors.Password2" class="text-danger">{{ errors.Password2 }}</small>
        </div>
        <div class="notification is-danger" v-if="Object.keys(errors).length">
          <p v-for="(error, index) in Object.values(errors)" :key="index">{{ error }}</p>
        </div>
        <div class="col-12">
          <button type="submit" class="btn text-white w-100 rounded-3">Créer un compte</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// import Cookies from 'js-cookie';

export default {
  name: 'RegisterPage',
  props: ['role'],
  data() {
    return {
      FirstName: '',
      LastName: '',
      Address: '',
      Email: '',
      Password1: '',
      Password2: '',
      errors: {
        FirstName: '',
        LastName: '',
        Address: '',
        Email: '',
        Password1: '',
        Password2: '',
        wrong_credentials: '',
      },
    };
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

      this.errors = {
      };

      // Validation des champs
      if (!this.FirstName) {
        this.errors.FirstName = "Le prénom est requis.";
      }
      if (!this.LastName) {
        this.errors.LastName = "Le nom est requis.";
      }
      if (!this.Address) {
        this.errors.Address = "L'adresse est requise.";
      }
      if (!this.Email) {
        this.errors.Email = "L'email est requis.";
      }
      if (!this.Password1) {
        this.errors.Password1 = "Le mot de passe est requis.";
      }
      if (!this.Password2) {
        this.errors.Password2 = "La confirmation du mot de passe est requise.";
      }
      if (this.Password1 !== this.Password2) {
        this.errors.Password2 = "Les mots de passe ne correspondent pas.";
      }

      // Arrêter si des erreurs sont présentes
      if (Object.keys(this.errors).length > 0) {
        return;
      }

      // Préparer les données pour l'envoi à l'API
      const formData = {
        FirstName: this.FirstName,
        LastName: this.LastName,
        Address: this.Address,
        Email: this.Email,
        Password1: this.Password1,
        Password2: this.Password2
      };


      axios.post(`/register/`, formData)
        .then(response => {

          if (response.data.success) {

            this.navigateToDashboard();
          } else {
            this.errors.wrong_credentials = "Email ou mot de passe incorrect.";
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

.btn:hover{
    background-color: #1fa3b5;
}

.btn{
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
