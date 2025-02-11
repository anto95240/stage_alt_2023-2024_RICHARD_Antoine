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
      :time-to="19 * 60"
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
        'padding': '10px',
        'width': '100%',
        'height': '200px'
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
        this.events = response.data.map(course => ({
          start: `${course.date} ${course.start_time}`,
          end: `${course.date} ${course.end_time}`,
          title: `${course.subject} - <br> ${course.teacher.last_name} ${course.teacher.first_name}`,
          content: `Salle: ${course.place}`,
          backgroundColor: `${course.color}`
        }));

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
.vuecal {
  --vuecal-event-color: #ff5722;
}

.vuecal-header {
  background-color: #f5f5f5;
}

.vuecal-day {
  font-size: 14px;
  color: #333;
}

.custom-header {
  font-weight: bold;
  text-align: center;
  padding: 5px;
  background-color: #f5f5f5;
}

.custom-event {
  padding: 5px;
  border-radius: 4px;
  color: white;
}

.vuecal__heading .weekday-label {
  color: rgb(56, 119, 34) !important;
}

.vuecal__no-event {
  display: none;
}

.vuecal__title {
  color: black;
}

.vuecal__no-event::before {
  content: '';
}
</style>
