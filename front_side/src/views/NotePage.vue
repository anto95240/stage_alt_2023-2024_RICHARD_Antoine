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
            <li class="sidebar-item active">
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
            <p class="navbar-brand text-white">note</p>
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
      <div class="content">
        <div class="row">
          <div class="col-lg-6 col-md-6 mx-auto">
            <div class="card card-chart">
              <div class="card-body">
                <div class="chart-area" v-for="subject in uniqueSubjects" :key="subject">
                  <div class="d-flex justify-content-between p-3">
                    <h5>{{ subject }}</h5>
                    <h5>{{ getAverageForSubject(subject) }}</h5>
                  </div>
                  <div class="d-flex justify-content-end pe-5 note" v-for="note in getNotesForSubject(subject)" :key="note.id" @click="showNoteDetails(note)">
                    <p>{{ note.note }} / {{  note.total_score }}</p>
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <div class="stats">
                  <div class="d-flex justify-content-between">
                    <h5>Moyenne Etudiant</h5>
                    <h5>{{ overallAverage.toFixed(2) }}</h5>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="selectedNote" class="modal" @click.self="selectedNote = null">
            <div class="modal-content">
              <span class="close" @click="selectedNote = null">&times;</span>
              <h2>Détails de la Note</h2>
              <p>Matière: {{ selectedNote.subject }}</p>
              <p>Note: {{ selectedNote.note }}</p>
              <p>Noté sur: {{ selectedNote.total_score }}</p>
              <p>Coefficient: {{ selectedNote.coefficient }}</p>
              <p>Enseignant: {{ selectedNote.teacher }}</p>
              <p>Étiquette: {{ selectedNote.label }}</p>
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
    name: 'NotePage',
    props: ['role'],
    data() {
      return {
        isSidebarExpanded: false,
        firstName: '',
        lastName: '',
        notes: [],
        averagePerSubject: [],
        overallAverage: 0,
        selectedNote: null,
        userInfo: null,
        userid: Cookies.get('UserId'),
        photo: 'https://i.pravatar.cc/150?img=3', // Default profile image
        profileImageFile: null,
      };
    },
    computed: {
      uniqueSubjects() {
        return [...new Set(this.notes.map(note => note.subject))];
      }
    },
    mounted() {
      this.getUserFromCookies();
      this.fetchNotes();
    },
    methods: {
      getUserFromCookies() {
        this.firstName = Cookies.get('FirstName') || '';
        this.lastName = Cookies.get('LastName') || '';
      },
      fetchNotes() {
        const studentId = Cookies.get('UserId'); 
        axios.get('/notes/', { params: { student_id: studentId } }, { withCredentials: true })
          .then(response => {
            const { notes, average_per_subject, overall_average } = response.data;
            this.notes = notes; 
            this.averagePerSubject = average_per_subject.map(item => ({
              subject: item.subject,
              average: parseFloat(item.average)
            }));
            this.overallAverage = Number(overall_average) || 0;
          })
          .catch(error => {
            console.error('Une erreur est survenue lors de la récupération des notes.', error);
          });
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
      showNoteDetails(note) {
        this.selectedNote = note;
      },
      getAverageForSubject(subject) {
        // Trouver la moyenne pour la matière
        const avg = this.averagePerSubject.find(item => item.subject === subject)?.average;
        // Vérifier si avg est un nombre avant d'appeler toFixed
        return typeof avg === 'number' ? avg.toFixed(2) : 'N/A';
      },
      getNotesForSubject(subject) {
        return this.notes.filter(note => note.subject === subject);
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

.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.note{
  cursor:pointer
}
</style>