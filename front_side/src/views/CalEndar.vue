<template>
  <div>
    <vue-cal
      :events="events"
      :hide-view-selector="true"
      default-view="week"
      :style="calendarStyle"
      :locale="locale" 
      active-view="week" 
      :disable-views="['years', 'year', 'month', 'day']"
      :time-from="8 * 60"
      :time-to="18 * 60"
    >
      <template v-slot:event="{ event }">
        <div
          class="vuecal__event"
          :style="{ backgroundColor: event.backgroundColor }"
        >
          <div class="vuecal__event-title" v-html="event.title"></div>
          <div class="vuecal__event-time">
            {{ formatTime(event.start) }} - {{ formatTime(event.end) }}
          </div>
          <div class="vuecal__event-content">{{ event.content }}</div>
        </div>
      </template>
    </vue-cal>
  </div>
</template>

<script>
import axios from 'axios';
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';

export default {
  components: {
    VueCal
  },
  props: ['role'],
  data() {
    return {
      events: [],
      locale: 'fr',
      userId: null,
      calendarStyle: {
        // 'border-radius': '8px',
        'padding': '10px',
        'width': '100%',
        'height': '200px' // Ajustez la hauteur en fonction de vos besoins
      }
    };
  },
  methods: {
    fetchEvents() {
      if (!this.role || !this.userId) {
        console.error("Role ou userId non définis");
        return;
      }

      const url = '/cours/';

      axios.get(url, {
        params: {
          role: this.role,
          user_id: this.userId
        }
      })
      .then(response => {
        console.log("Données reçues:", response.data);

        this.events = response.data.map(course => ({
          start: `${course.Date} ${course.StartTime}`,
          end: `${course.Date} ${course.EndTime}`,
          title: `${course.Subject} - <br> ${course.Teacher.LastName} ${course.Teacher.FirstName}`,
          content: `Salle: ${course.Place}`,
          backgroundColor: `${course.Color}` // Assurez-vous que la propriété est correcte
        }));

        console.log("Événements transformés:", this.events);
      })
      .catch(error => {
        console.error("Erreur lors de la récupération des événements:", error.response || error);
      });
    },
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
      return null;
    },
    onDateClick(date) {
      console.log("Date cliquée:", date);
    },
    formatTime(dateTime) {
      const date = new Date(dateTime);
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    }
  },
  mounted() {
    this.userId = this.getCookie('UserId');
    if (this.userId) {
      this.fetchEvents();
    } else {
      console.error("userId non trouvé dans les cookies");
    }
  }
};
</script>

<style>
.vuecal__event {
  position: absolute;
  top: 0; /* Positionnement vertical pour ajuster les événements */
  left: 0; /* Positionnement horizontal pour ajuster les événements */
  width: 100%;
  padding: 10px;
  border-radius: 3px;
  border: 1px solid rgba(255, 255, 255, 0.3); /* Bordure pour plus de visibilité */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Ombre optionnelle */
  box-sizing: border-box; /* Pour que le padding n'affecte pas la largeur totale */
  display: flex;
  flex-direction: column;
  height: 100%;
}

.vuecal__event-title {
  font-weight: bold;
}

.vuecal__event-time {
  font-size: 14px;
}

.vuecal__event-content {
  font-size: 12px;
}
</style>
