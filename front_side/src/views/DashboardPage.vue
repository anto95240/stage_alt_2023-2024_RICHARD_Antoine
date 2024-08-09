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
            <li class="sidebar-item active">
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
            <p class="navbar-brand text-white">Dashboard</p>
          </div>
          <div class="collapse navbar-collapse justify-content-between" style="margin-left: 35%;">
            <p>Espace {{ role }} - {{ lastName }} {{ firstName }}</p>
            <ul class="navbar-nav ms-5">
              <li class="nav-item dropdown">
                <a class="nav-link" @click="navigateToNotification" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="fa-solid fa-bell fa-2xl"></i>
                </a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link" @click="navigateToAccount">
                  <img :src="photo" class="rounded-circle" width="25" height="25" />
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="panel-header panel-header-lg">
        <a class="d-flex gap-2 text-dark planning w-25" style="height: 14%;" @click="navigateToCours">
          <h1 class="text-white ms-5">Planning</h1>
          <h1 class="text-white ms-3">></h1>
        </a>        
        <CourseSmallCalendar :role="role" />                 
      </div>
      <div class="content">
        <div class="row">
          <div class="col-lg-4 col-md-6">
            <div class="card card-chart">
              <div class="card-header">
                  <a class="d-flex gap-2 text-dark w-50" @click="navigateToNote">
                      <p class="card-title">Mes dernières notes</p>
                      <p class="card-title">></p> 
                  </a> 
              </div>
              <div class="card-body">
                <div class="chart-area">
                  <li v-for="note in notes" :key="note.id">
                    <div class="d-flex gap-5 p-2 m-2 border rounded-3 justify-content-between">
                      <strong>{{ note.subject }}</strong>
                      <p class="mb-0">{{ note.note }} / {{  note.total_score }}</p>
                    </div>
                  </li>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="card card-chart">
              <div class="card-header">
                  <a class="d-flex gap-2 text-dark w-75" @click="navigateToVieScolaire">
                      <p class="card-title">Mes dernières absences</p>
                      <p class="card-title">></p> 
                  </a>
              </div>
              <div class="card-body">
                <div class="chart-area">
                  <li v-for="absence in absences" :key="absence.id">
                    <div class="d-flex gap-5 p-2 m-2 border rounded-3 justify-content-between">
                      <div class="d-flex flex-column">
                        <strong>{{ absence.date }}</strong>
                        <p class="mb-0"> de {{ absence.absence_start_time}} à {{ absence.absence_end_time }}</p>
                      </div>
                      <p>{{ calculateDuration(absence.absence_start_time, absence.absence_end_time) }}</p>
                    </div>
                  </li>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="card card-chart">
              <div class="card-header">
                  <a class="d-flex gap-2 text-dark w-75" @click="navigateToVieScolaire">
                      <p class="card-title">Mes derniers retards</p>
                      <p class="card-title">></p> 
                  </a>
              </div>
              <div class="card-body">
                <div class="chart-area">
                  <li v-for="retard in retards" :key="retard.id">
                    <div class="d-flex gap-5 p-2 m-2 border rounded-3 justify-content-between">
                      <strong>{{ retard.late_duration }} minutes</strong>
                      <p class="mb-0">{{ retard.date }}</p>
                    </div>
                  </li>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="card card-chart">
              <div class="card-header">
                  <a class="d-flex gap-2 text-dark w-50" @click="navigateToDocument">
                      <p class="card-title">Mes documents</p>
                      <p class="card-title">></p> 
                  </a>
              </div>
              <div class="card-body">
                <div class="chart-area">
                  <li v-for="document in documents" :key="document.id">
                    <div class="d-flex gap-5 p-2 m-2 border rounded-3 justify-content-between">
                      <strong>{{ document.name }}</strong>
                      <a :href="document.file_path">Télécharger</a>
                    </div>
                  </li>
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
import 'vue-cal/dist/vuecal.css';
import CourseSmallCalendar from '../components/SmallCalendar.vue';
import axios from 'axios';
  
export default {
  name: 'DashboardPage',
  components: {
    CourseSmallCalendar
  },
  props: ['role'],
  data() {
    return {
      isSidebarExpanded: false,
      documents: [],
      absences: [],
      retards: [],
      notes: [],
      firstName: '',
      lastName: '',
      userInfo: null,
      userid: Cookies.get('UserId'),
      photo: 'https://i.pravatar.cc/150?img=3',
      profileImageFile: null,
    };
  },
  mounted() {
    this.getUserFromCookies();
    this.fetchDocuments();
    this.fetchPresences();
    this.fetchNotes();
  },
  methods: {
    getUserFromCookies() {
      this.firstName = Cookies.get('FirstName') || '';
      this.lastName = Cookies.get('LastName') || '';
    },
    fetchUserInfo() {
      axios.get(`/user-info/${this.userid}/`)
        .then(response => {
          this.userInfo = response.data;
          this.photo = this.userInfo.photo ? `data:image/jpeg;base64,${this.userInfo.photo}` : this.photo;
        })
        .catch(error => {
          console.error('Erreur lors de la récupération des informations utilisateur.', error);
        });
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
    toggleSidebar() {
    this.isSidebarExpanded = !this.isSidebarExpanded;
    },
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
    fetchPresences() {
      const studentId = Cookies.get('StudentId');

      axios.get('/presences/', { params: { student_id: studentId } })
        .then(response => {
          this.absences = response.data.filter(p => p.is_abscent).slice(-5);
          this.retards = response.data.filter(p => p.is_late).slice(-5);
        })
        .catch(error => {
          console.error('Erreur lors de la récupération des présences:', error);
        });
    },
    fetchDocuments() {
      axios.get('/documents/')
        .then(response => {
          this.documents = response.data.slice(-5);
        })
        .catch(error => {
          console.error("There was an error fetching the documents!", error);
        });
    },
    fetchNotes() {
      const studentId = Cookies.get('UserId');
      axios.get('/notes/', { params: { student_id: studentId } }, { withCredentials: true })
        .then(response => {
          this.notes = response.data.notes.slice(-5);
        })
        .catch(error => {
          console.error("There was an error fetching the notes!", error);
        });
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
  height: 100%;
  position: fixed;
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
  margin-left: 4.5%;
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

.navbar>.container, .navbar>.container-fluid, .navbar>.container-lg, .navbar>.container-md, .navbar>.container-sm, .navbar>.container-xl, .navbar>.container-xxl {
    display: flex;
    flex-wrap: inherit;
    align-items: center;
    justify-content: space-between;
    margin-left: 5%;
}

.panel-header {
    margin-left: 4.5%;
}
</style>