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
            <li class="sidebar-item active">
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
            <li class="sidebar-item">
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
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent  bg-primary  navbar-absolute">
        <div class="container-fluid">
          <div class="navbar-wrapper">
            <p class="navbar-brand text-white">Vie Scolaire</p>
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
                  <img :src="photo" class="rounded-circle" width="25" height="25" />
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="panel-header panel-header-sm">
      </div>
      <div class="tabs">
        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item px-5" role="presentation">
            <a class="nav-link px-5" :class="{ active: activeTab === 'absences' }" @click="setActiveTab('absences')" id="absences-tab" data-bs-toggle="tab" role="tab">Mes absences</a>
          </li>
          <li class="nav-item px-5" role="presentation">
            <a class="nav-link px-5" :class="{ active: activeTab === 'retards' }" @click="setActiveTab('retards')" id="retards-tab" data-bs-toggle="tab" role="tab">Mes retards</a>
          </li>
          <li class="nav-item px-5" role="presentation"> <!--v-if="role === 'teacher'" >-->
            <a class="nav-link px-5" :class="{ active: activeTab === 'all' }" @click="setActiveTab('all')" id="all-tab" data-bs-toggle="tab" role="tab">Absences/retards des élèves</a>
          </li>
        </ul>
        <div class="tab-content">
          <!-- Content for each tab -->
          <div v-if="activeTab === 'absences'" class="tab-pane fade show active" id="absences" role="tabpanel">
            <!-- Content for absences -->
            <div class="row">
              <div class="col">
                <div class="card card-chart">
                  <div class="card-body">
                    <table class="table">
                      <thead>
                        <tr>
                          <th class="fs-6">Date</th>
                          <th class="fs-6">Heure de début</th>
                          <th class="fs-6">Heure de fin</th>
                          <th class="fs-6">Temps d'absence</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="absence in absences" :key="absence.id">
                          <td class="fs-7">{{ absence.date }}</td>
                          <td class="fs-7">{{ absence.absence_start_time }}</td>
                          <td class="fs-7">{{ absence.absence_end_time }}</td>
                          <td class="fs-7">{{ calculateDuration(absence.absence_start_time, absence.absence_end_time) }}</td>
                        </tr>
                      </tbody>
                    </table>
                    
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="activeTab === 'retards'" class="tab-pane fade show active" id="retards" role="tabpanel">
            <!-- Content for retards -->
            <div class="row">
              <div class="col">
                <div class="card card-chart">
                  <div class="card-body">
                    <table class="table">
                      <thead>
                        <tr>
                          <th class="fs-6">Durée</th>
                          <th class="fs-6">Date</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="retard in retards" :key="retard.id">
                          <td class="fs-7">{{ retard.late_duration }} minutes</td>
                          <td class="fs-7">{{ retard.date }}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="activeTab === 'all'" class="tab-pane fade show active" id="all" role="tabpanel">
            <!-- Content for all absences/retards -->
            <div class="row">
              <div class="col">
                <div class="card card-chart">
                  <div class="card-header">
                    <form @submit.prevent="searchStudents">
                      <div class="row">
                        <div class="col-md-6 d-flex flex-column align-items-start mt-2">
                          <label for="inputSpecialite" class="form-label">Specialité</label>
                          <input type="text" class="form-control" id="inputSpecialite" v-model="searchFields.specialite">
                        </div>
                        <div class="col-md-6 d-flex flex-column align-items-start mt-2">
                          <label for="inputClass" class="form-label">Classe</label>
                          <input type="text" class="form-control" id="inputClass" v-model="searchFields.classe">
                        </div>
                        <div class="col-md-6 d-flex flex-column align-items-start mt-3">
                          <label for="inputIntervenant" class="form-label">Intervenant</label>
                          <input type="text" class="form-control" id="inputIntervenant" v-model="searchFields.intervenant">
                        </div>
                        <div class="col-md-3 d-flex flex-column align-items-start mt-3">
                          <label for="inputStartTime" class="form-label">Date début cours</label>
                          <input type="time" class="form-control" id="inputStartTime" v-model="searchFields.startTime">
                        </div>
                        <div class="col-md-3 d-flex flex-column align-items-start mt-3">
                          <label for="inputEndTime" class="form-label">Date fin cours</label>
                          <input type="time" class="form-control" id="inputEndTime" v-model="searchFields.endTime">
                        </div>
                      </div>
                        <div class="d-flex flex-column align-items-end justify-content-flex-end">
                          <button type="submit" class="btn">Actualiser la liste des élèves</button>
                        </div>
                    </form>
                  </div>
                  <div class="card-body">
                    <table class="table">
                      <thead>
                        <tr>
                          <th class="fs-6">Nom</th>
                          <th class="fs-6">Prénom</th>
                          <th class="fs-6">Spéciliaté</th>
                          <th class="fs-6">Niveau de class</th>
                          <th class="fs-6">Est Abscent</th>
                          <th class="fs-6">Est en Retard</th>
                          <th class="fs-6">Durée du Retard</th>
                          <th class="fs-6">Date</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="student in filteredStudents" :key="student.id">
                          <td class="fs-7">{{ last_name }}</td>
                          <td class="fs-7">{{ first_name }}</td>
                          <td class="fs-7">{{ searchFieldspecialization }}</td>
                          <td class="fs-7">{{ classe }}</td>
                          <td class="fs-7">
                            <input type="checkbox" v-model="absence.is_abscent" />
                          </td>
                          <td class="fs-7">
                            <input type="checkbox" v-model="retard.is_late" />
                          </td>
                          <td class="fs-7">
                            <select v-model="retard.late_duration">
                              <option :value="null">-- Sélectionner --</option>
                              <option v-for="option in lateDurationOptions" :key="option.value" :value="option.value">
                                {{ option.label }}
                              </option>
                            </select>
                          </td>                          
                          <td class="fs-7">{{ student.date }}</td>
                          <td class="fs-7">
                            <button @click="updatePresence(student)">Mettre à jour</button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <footer class="footer mt-auto py-3 bg-light">
        <div>
          <span class="copyright"> © 2024, Designé et codé par Antoine RICHARD. </span>
        </div>
      </footer>
    </div>
  </div>
</template>
    
<script>
  import Cookies from 'js-cookie';
  import axios from 'axios';
  
  export default {
    name: 'VieScolaire',
    props: ['role'],
    data() {
      return {
        isSidebarExpanded: false,
        firstName: '',
        lastName: '',
        activeTab: 'absences',
        absences: [],
        retards: [],
        userInfo: null,
        userid: Cookies.get('UserId'),
        photo: 'https://i.pravatar.cc/150?img=3',
        profileImageFile: null,
        searchFields: {
          specialite: '',
          classe: '',
          intervenant: '',
          startTime: '',
          endTime: ''
        },
        students: []
      };
    },
    mounted() {
      this.getUserFromCookies();
      this.fetchPresences();
      this.fetchUserInfo();
    },
    methods: {
      formatDate(date) {
        // Formatte la date au format souhaité (par exemple, 'DD-MM-YYYY')
        return new Date(date).toLocaleDateString();
      },
      calculateDuration(startTime, endTime) {
        // On convertit les heures pour être un objets Date
        const [startHours, startMinutes] = startTime.split(':').map(Number);
        const [endHours, endMinutes] = endTime.split(':').map(Number);

        const startDate = new Date();
        startDate.setHours(startHours, startMinutes, 0, 0);

        const endDate = new Date();
        endDate.setHours(endHours, endMinutes, 0, 0);

        // On calcul la différence en minutes
        const diffMs = endDate - startDate;
        const diffMins = Math.floor(diffMs / 60000); // 60000 ms dans une minute

        // Puis on convertit en heures et minutes
        const hours = Math.floor(diffMins / 60);
        const minutes = diffMins % 60;

        return `${hours}h ${minutes}m`;
      },
      getUserFromCookies() {
        this.firstName = Cookies.get('FirstName') || '';
        this.lastName = Cookies.get('LastName') || '';
      },
      fetchUserInfo() {
        axios.get(`/user-info/${this.userid}/`)
          .then(response => {
            this.userInfo = response.data;
            this.first_name = this.userInfo.first_name;
            this.last_name = this.userInfo.last_name;
            this.specialization = this.userInfo.specialization;
            this.classe = this.userInfo.classe;
            this.photo = this.userInfo.photo ? `data:image/jpeg;base64,${this.userInfo.photo}` : this.photo;
          })
          .catch(error => {
            console.error('Erreur lors de la récupération des informations utilisateur.', error);
          });
      },
      fetchPresences() {
        const studentId = Cookies.get('StudentId');

        axios.get('/presences/', { params: { student_id: studentId } })
          .then(response => {
            this.absences = response.data.filter(p => p.is_abscent);
            this.retards = response.data.filter(p => p.is_late);
          })
          .catch(error => {
            console.error('Erreur lors de la récupération des présences:', error);
          });
      },
      setActiveTab(tab) {
        this.activeTab = tab;
      },
      navigateToNotification() {
        this.$router.push({ name: 'NotificationPage', params: { role: this.role } });
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
      toggleSidebar() {
      this.isSidebarExpanded = !this.isSidebarExpanded;
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

.color{
  color: #749fcc !important;
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


.tabs {
  margin-top: 1%;
  cursor: pointer;
  margin-left: 8%;
  
}

.nav-tabs {
  border-bottom: 1px solid #dee2e6;
}

.nav-tabs .nav-item {
  margin-bottom: -1px;
}

.nav-tabs .nav-link {
  border: 1px solid transparent;
  border-radius: .25rem;
  margin-right: .2rem;
  padding: .5rem 1rem;
}

.nav-tabs .nav-link.active {
  color: #495057;
  background-color: #ffffff;
  border-color: #dee2e6 #dee2e6 #fff;
}

.tab-content {
  padding: 1rem;
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-top: 0;
  border-radius: .25rem;
}

.tab-pane {
  display: none;
}

.tab-pane.active {
  display: block;
}
</style>