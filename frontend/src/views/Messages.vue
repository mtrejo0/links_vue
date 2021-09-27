<template>
  <div class="center wrapper">
    <div>
      <div v-for="message in messages" v-bind:key="message" class="item-wrapper success-message message">
      <p>{{ message }}</p>
    </div>
    <div v-for="error in errors" v-bind:key="error" class="item-wrapper error-message message">
      <p>{{ error }}</p>
    </div>
    </div>
  </div>
</template>
<script>
import { eventBus } from "../main";

export default {
  data() {
    return {
      errors: [],
      messages: [],
    };
  },
  methods: {
    removeMessage() {
      setTimeout(() => {
        this.messages.shift()
      }, 3000);
    },
    removeError() {
      setTimeout(() => {
        this.errors.shift()
      }, 3000);
    },
  },
  created() {
    eventBus.$on("message", (message) => {
      this.messages.push(message);
      this.removeMessage();
    });
    eventBus.$on("error", (error) => {
      this.errors.push(error);
      this.removeError();
    });
  },
};
</script>


<style scoped>
.wrapper {
  position: fixed;
  top: 0%;
  right: 0%;
}
.message {
  background: white;
}
</style>
