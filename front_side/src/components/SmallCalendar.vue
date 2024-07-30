<template>
  <div>
    <vue-cal
      :events="events"
      :hide-view-selector="true"
      default-view="week"
      :style="calendarStyle"
      :locale="locale"
    >
      <!-- Slot pour personnaliser les en-têtes des colonnes -->
      <template v-slot:header="{ day, date }">
        <div class="custom-header">
          {{ getCustomHeader(day, date) }}
        </div>
      </template>

      <!-- Slot pour personnaliser les événements -->
      <template v-slot:event="event">
        <div class="custom-event" :style="{ backgroundColor: event.event.backgroundColor }">
          {{ event.event.title }}
        </div>
      </template>
    </vue-cal>
  </div>
</template>

<script>
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';

export default {
  components: {
    VueCal
  },
  data() {
    return {
      events: [
          {
          start: '2024-07-25T10:00:00',
          end: '2024-07-25T12:00:00',
          title: 'Meeting with John',
          backgroundColor: '#ff5722',
          },
      ], 
      locale: 'fr', // Langue du calendrier
      calendarStyle: {
        // 'border-radius': '8px',
        'padding': '10px',
        'width': '100%',
        'height': '200px' // Ajustez la hauteur en fonction de vos besoins
      }
    };
  },
  methods: {
      getCustomHeader(day, date) {
        // Map full names of days to abbreviations
        const days = {
          'Monday': 'Lu',
          'Tuesday': 'Ma',
          'Wednesday': 'Me',
          'Thursday': 'Je',
          'Friday': 'Ve',
          'Saturday': 'Sa',
          'Sunday': 'Di'
        };

        // Format the header as "Lu 22" for example
        return `${days[day] || day} ${date.getDate()}`;
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
  /* border-bottom: 1px solid #ddd; */
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

/* .vuecal__title-bar {
  background: linear-gradient(to left, #0c2646 0%, #204065 60%, #2a5788 100%);
} */

.vuecal__no-event::before {
  content: '';
}

.vuecal-day {
  font-size: 14px;
  color: #333;
}
</style>
