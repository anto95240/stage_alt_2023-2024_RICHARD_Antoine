<template>
  <div class="wrapper">
    <aside :class="{ expand: isSidebarExpanded }" id="sidebar">
      <div class="d-flex">
        <button class="toggle-btn" type="button" @click="toggleSidebar">
          <i class="fa-solid fa-grip"></i>
        </button>
        <div class="sidebar-logo">
          <a href="#"></a>
        </div>
      </div>
      <ul class="sidebar-nav">
        <li class="sidebar-item">
          <a @click="navigateToHome" class="sidebar-link">
            <i class="fa-solid fa-house"></i>
            <span>Accueil</span>
          </a>
        </li>
        <hr>
        <li class="sidebar-item">
          <a @click="navigateToCours" class="sidebar-link gap-2">
            <i class="fa-solid fa-calendar-days"></i>
            <span class="ms-1">Cours</span>
          </a>
        </li>
        <li class="sidebar-item">
          <a @click="navigateToNote" class="sidebar-link gap-2">
            <i class="fas fa-clipboard-check"></i>
            <span class="ms-2">Note</span>
          </a>
        </li>
        <li class="sidebar-item">
          <a @click="navigateToVieScolaire" class="sidebar-link gap-2">
            <i class="fa-solid fa-graduation-cap"></i>
            <span>Vie scolaire</span>
          </a>
        </li>
        <li class="sidebar-item">
          <a @click="navigateToDocument" class="sidebar-link">
            <i class="fa-solid fa-user-shield"></i>
            <span class="ms-1">Administration</span>
          </a>
        </li>
        <hr>
        <li class="sidebar-item active">
          <a @click="navigateToAccount" class="sidebar-link">
            <i class="fa-solid fa-address-card"></i>
            <span class="ms-1">Mon Compte</span>
          </a>
        </li>
      </ul>
      <div class="sidebar-footer">
        <a @click="logout" class="sidebar-link">
          <i class="fa-solid fa-right-from-bracket fa-rotate-180 fa-xl"></i>
          <span class="ms-1">Déconnexion</span>
        </a>
      </div>
    </aside>
    <div class="main-panel" id="main-panel">
      <!--Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent  bg-primary  navbar-absolute">
        <div class="container-fluid">
          <div class="navbar-wrapper">
            <p class="navbar-brand text-white">Mon Compte</p>
          </div>
          <div class="collapse navbar-collapse justify-content-between" style="margin-left: 35%;">
            <p>Espace {{ role }} - {{ lastName }} {{ firstName }}</p>
            <ul class="navbar-nav ms-5">
              <li class="nav-item dropdown">
                <a class="nav-link" @click="navigateToNotification" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="fa-solid fa-bell fa-2xl"></i>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" @click="navigateToAccount">
                  <!-- <i class="fa-solid fa-circle-user fa-2xl"></i> -->
                  <img :src="Photo" class="rounded-circle" width="25" height="25" />
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="panel-header panel-header-sm">
      </div>
      <div class="content">
        <div class="row">
          <div class="col-lg-10 col-md-6 mx-auto">
            <div class="card">
              <div class="card-body">
                <div class="chart-area">
                  <form class="row g-3" @submit.prevent="submitForm">
                    <div v-if="errors.wrong_credentials" class="mb-3 d-flex flex-column align-items-start text-start">
                      <small class="text-danger">{{ errors.wrong_credentials }}</small>
                    </div>
                    <!-- <div class="dropdown">
                      <img class="rounded-circle" :src="profileImageUrl" alt="Circle image" width="100" height="100" />
                      <input type="file" class="form-control" id="inputGroupFile01" @change="onFileChange">
                    </div> -->
                    <div class="dropdown">
                      <img class="rounded-circle" :src="Photo" alt="Circle image" width="120" height="120" />
                      <button type="button" @click="triggerFileInput" class="btn px-1 py-1 my-auto" style="width: 2%;">
                        <i class="fa-regular fa-image"></i>
                      </button>
                      <input type="file" ref="fileInput" class="d-none" name="Photo" @change="onFileChange" />
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
                    <div class="col-md-12 d-flex flex-column align-items-start">
                      <label for="inputAge" class="form-label">Date de naissance</label>
                      <input type="text" class="form-control" id="inputAge" name="Age" v-model="Age" />
                      <small v-if="errors.Age" class="text-danger">{{ errors.Age }}</small>
                    </div>
                    <div class="col-md-6 d-flex flex-column align-items-start">
                      <label for="inputSpecialization" class="form-label">Spetialisation</label>
                      <input type="text" class="form-control" id="inputSpecialization" name="Specialization" v-model="Specialization" :disabled="true">
                      <small v-if="errors.Specialization" class="text-danger">{{ errors.Specialization }}</small>
                    </div>
                    <div class="col-md-6 d-flex flex-column align-items-start">
                      <label for="inputClass" class="form-label">Classe</label>
                      <input type="text" class="form-control" id="inputClass" name="Class" v-model="Class" :disabled="true">
                      <small v-if="errors.Class" class="text-danger">{{ errors.Class }}</small>
                    </div>
                    <div class="col-12 d-flex flex-column align-items-start">
                      <label for="inputPassword" class="form-label">Nouveau Mot de passe</label>
                      <input type="password" class="form-control" id="inputPassword" name="Password" v-model="Password" />
                      <small v-if="errors.Password" class="text-danger">{{ errors.Password }}</small>
                    </div>
                    <div class="col-12">
                      <button type="submit" class="btn btn-primary">Mettre à Jour</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios';
  import Cookies from 'js-cookie';
  export default {
    name: 'AccountPage',
    props: ['role'],
    data() {
      return {
        FirstName: '',
        LastName: '',
        Address: '',
        Email: '',
        Age: '',
        Specialization: '',
        Class: '',
        Password: '',
        errors: {},
        isSidebarExpanded: false,
        firstName: '',
        lastName: '',
        userInfo: null,
        userid: Cookies.get('UserId'),
        Photo: 'https://i.pravatar.cc/150?img=3', // Default profile image
        profileImageFile: null,
      };
    },
    mounted() {
      this.getUserFromCookies();
      this.fetchUserInfo();
    },
    methods: {
      fetchUserInfo() {
        axios.get(`/user-info/${this.userid}/`)
          .then(response => {
            console.log('User info fetched:', response.data);
            this.userInfo = response.data;
            this.FirstName = this.userInfo.FirstName;
            this.LastName = this.userInfo.LastName;
            this.Address = this.userInfo.Address;
            this.Email = this.userInfo.Email;
            this.Photo = this.userInfo.Photo ? `data:image/jpeg;base64,${this.userInfo.Photo}` : this.Photo;
            this.Age = this.userInfo.Age;
            this.Specialization = this.userInfo.Specialization;
            this.Class = this.userInfo.Class;
          })
          .catch(error => {
            console.error('Erreur lors de la récupération des informations utilisateur.', error);
          });
      },
      triggerFileInput() {
        this.$refs.fileInput.click();
      },
      onFileChange(event) {
        const file = event.target.files[0];
        if (file && file.type.startsWith('image/')) {
          this.profileImageFile = file;
          const reader = new FileReader();
          reader.onload = (e) => {
            this.Photo = e.target.result;
          };
          reader.readAsDataURL(file);
        } else {
          alert('Veuillez sélectionner un fichier image.');
        }
      },
      submitForm() {
        const formData = new FormData();
        formData.append('FirstName', this.FirstName);
        formData.append('LastName', this.LastName);
        formData.append('Address', this.Address);
        formData.append('Email', this.Email);
        formData.append('Age', this.Age);
        // formData.append('Specialization', this.Specialization);
        formData.append('Password', this.Password);
        if (this.profileImageFile) {
          formData.append('Photo', this.profileImageFile);
        }

        axios.put(`/user-update/${this.userid}/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
          .then(response => {
            console.log('Success:', response.data);
            this.fetchUserInfo();
          })
          .catch(error => {
            console.error('Error:', error.response);
          });
      },    
      getUserFromCookies() {
        this.firstName = Cookies.get('FirstName') || '';
        this.lastName = Cookies.get('LastName') || '';
      },
      navigateToNote() {
        this.$router.push({ name: 'NotePage', params: { role: this.role } });
      },
      navigateToHome() {
        this.$router.push({ name: 'DashboardPage', params: { role: this.role } });
      },
      navigateToCours() {
        this.$router.push({ name: 'CoursPage', params: { role: this.role } });
      },
      navigateToDocument() {
        this.$router.push({ name: 'DocumentPage', params: { role: this.role } });
      },
      navigateToVieScolaire() {
        this.$router.push({ name: 'VieScolaire', params: { role: this.role } });
      },
      navigateToAccount() {
        this.$router.push({ name: 'AccountPage', params: { role: this.role } });
      },
      navigateToNotification() {
        this.$router.push({ name: 'NotificationPage', params: { role: this.role } });
      },
      logout() {
        axios.post('/logout/', {}, { withCredentials: true })
          .then(response => {
            if (response.data.success) {
              this.$router.push({ name: 'LogOut' });
            }
          })
          .catch(error => {
            console.error('Une erreur est survenue lors de la déconnexion.', error);
          });
      },
      toggleSidebar() {
        this.isSidebarExpanded = !this.isSidebarExpanded;
      }
    }
  };
</script>
  
<style>
#app {
  font-family: 'Poppins', sans-serif !important;
  text-align: left !important;
  color: #2c3e50;
  margin-top: 0px !important;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

::after,
::before {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

a {
  text-decoration: none !important;
}

li {
  list-style: none !important;
}

h1 {
  font-weight: 600;
  font-size: 1.5rem;
}

template {
  font-family: 'Poppins', sans-serif;
  background-color: #E8F0FE; /* Adjusted background color for body */
  color: #343a40;
}

.wrapper {
  display: flex;
}

.main {
  min-height: 100vh;
  width: 100%;
  overflow: hidden;
  transition: all 0.35s ease-in-out;
  background-color: #E8F0FE; /* Adjusted background color for main */
}

#sidebar {
  width: 70px;
  min-width: 70px;
  z-index: 1000;
  transition: all .25s ease-in-out;
  background-color: #2E4C6D; 
  display: flex;
  flex-direction: column;
  background: linear-gradient(180deg, #0d5055 0%, #1C6A47 100%); 
  box-shadow: 3px 0 10px rgba(0, 0, 0, 0.2);
}

#sidebar.expand {
  width: 260px;
  min-width: 260px;
}

.toggle-btn {
  background-color: transparent;
  cursor: pointer;
  border: 0;
  padding: 1rem 1.5rem;
}

.toggle-btn i {
  font-size: 1.5rem;
  color: #fff;
}

.sidebar-logo {
  margin: auto 0;
}

.sidebar-logo a {
  color: #fff;
  font-size: 1.15rem;
  font-weight: 600;
}

#sidebar:not(.expand) .sidebar-logo,
#sidebar:not(.expand) a.sidebar-link span {
  display: none;
}

.sidebar-nav {
  padding: 2rem 0;
  flex: 1 1 auto;
}

a.sidebar-link {
  padding: .625rem 1.625rem;
  color: #ffffff;
  display: block;
  font-size: 0.9rem;
  white-space: nowrap;
  border-left: 3px solid transparent;
  cursor: pointer;
}

.sidebar-link i {
  font-size: 1.1rem;
  margin-right: .75rem;
}

.sidebar-item a:hover, .sidebar-footer a:hover {
  background-color: rgba(46, 76, 109, 0.236); 
  border-left: 3px solid #36e7ba;
  color: #36e7ba;
}

.sidebar-item.active{
  background-color: rgba(46, 76, 109, 0.236); 
  border-left: 3px solid #36e7ba;
}

.sidebar-item {
  position: relative;
}

#sidebar:not(.expand) .sidebar-item .sidebar-dropdown {
  position: absolute;
  top: 0;
  left: 70px;
  background-color: transparent;
  padding: 0;
  min-width: 15rem;
  display: none;
}

#sidebar:not(.expand) .sidebar-item:hover .has-dropdown+.sidebar-dropdown {
  display: block;
  max-height: 15em;
  width: 100%;
  opacity: 1;
}

#sidebar.expand .sidebar-link[data-bs-toggle="collapse"]::after {
  border: solid;
  border-width: 0 .075rem .075rem 0;
  content: "";
  display: inline-block;
  padding: 2px;
  position: absolute;
  right: 1.5rem;
  top: 1.4rem;
  transform: rotate(-135deg);
  transition: all .2s ease-out;
}

#sidebar.expand .sidebar-link[data-bs-toggle="collapse"].collapsed::after {
  transform: rotate(45deg);
  transition: all .2s ease-out;
}

.main-panel {
  width: calc(100%) !important;
  background-color: #E8F0FE; 
}

.main-panel>.content {
  background-color: #FFFFFF !important; 
  padding: 2rem;
  border-radius: 0.5rem;
  min-height: 0 !important;
  margin-top: -70px !important;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.card-header a:hover, .card-header a:focus{
  text-decoration: underline !important;
  color: black !important;
  cursor: pointer;
}

.planning:hover, .planning:focus{
  text-decoration: underline !important;
  color: rgb(255, 255, 255) !important;
  cursor: pointer;
}
</style>