<template>
  <div class="container bg-lightgreen rounded-4 d-flex p-0 w-50">
    <div class="rounded-4 bg-white bienvenue d-flex flex-column">
      <h3 class="mx-auto">Espace {{ role }}</h3>
      <template v-if="role !== 'admin'">
        <button type="button" class="btn text-white w-75 m-auto rounded-3" @click="navigateToRegister">Créer un compte</button>
      </template>
    </div>
    <div class="d-flex flex-column w-50 gap-5 mt-5 pb-5">
      <h3>CONNEXION</h3>
      <form class="row g-3" @submit.prevent="submitForm">
        <div v-if="errors.wrong_credentials" class="mb-3 d-flex flex-column align-items-start text-start">
          <small class="text-danger">{{ errors.wrong_credentials }}</small>
        </div>
        <div class="mb-3 d-flex flex-column align-items-start text-start">
          <label for="exampleFormControlInput1" class="form-label">Email</label>
          <input type="email" class="form-control" id="exampleFormControlInput1" name="Email" v-model="Email">
          <small v-if="errors.Email" class="text-danger">{{ errors.Email }}</small>
        </div>
        <div class="mb-3 d-flex flex-column align-items-start text-start">
          <label for="inputPassword5" class="form-label">Mot de Passe</label>
          <input type="password" id="inputPassword5" class="form-control" aria-describedby="PasswordHelpBlock" name="password" v-model="password">
          <small v-if="errors.password" class="text-danger">{{ errors.password }}</small>
        </div>
        <div class="col-12">
          <button type="submit" class="btn text-white w-100 rounded-3">Se connecter</button>
        </div>
      </form>
    </div>        
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  name: 'LoginPage',
  props: ['role'],
  data() {
    return {
      Email: "",
      password: "",
      errors: {
        Email: "",
        password: "",
        wrong_credentials: "",
      }
    }
  },
  methods: {
    submitForm() {
      this.errors = {
        Email: "",
        password: "",
        wrong_credentials: ""
      };

      if (!this.Email) {
        this.errors.Email = "L'email est requis.";
        return;
      }
      if (!this.password) {
        this.errors.password = "Le mot de passe est requis.";
        return;
      }

      axios.post(`/${this.role}-login/`, {
        Email: this.Email,
        password: this.password
      })
      .then(response => {
        if (response.data.success) {
          const user = response.data.user;
          const FirstName = user.FirstName;
          const LastName = user.LastName;

          // Stockage des tokens JWT dans les cookies
          const access_token = response.data.access;
          const refresh_token = response.data.refresh;

          // Exemple de stockage des tokens dans les cookies avec une durée de vie
          const now = new Date();
          const accessTokenExpires = new Date(now.getTime() + 3600 * 1000); // Expiration dans 1 heure
          Cookies.set('access_token', access_token, { expires: accessTokenExpires, path: '/' });

          const refreshTokenExpires = new Date(now.getTime() + 7 * 24 * 3600 * 1000); // Expiration dans 7 jours
          Cookies.set('refresh_token', refresh_token, { expires: refreshTokenExpires, path: '/' });

          // Stockage d'autres informations dans les cookies si nécessaire
          Cookies.set('role', this.role, { path: '/' });
          Cookies.set('FirstName', FirstName, { path: '/' });
          Cookies.set('LastName', LastName, { path: '/' });


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
