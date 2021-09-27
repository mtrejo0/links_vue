<template>
  <div>
    <h1>Hello {{username}}!</h1>
    <v-btn v-on:click="logout">Logout</v-btn>
    <items v-bind:items="this.items"/>
  </div>
</template>

<script>
import { eventBus } from "../main";
import axios from "axios";
import Items from "./Items.vue";
export default {
  data() {
    return {
      username: this.$cookie.get('username'),
      items: []
    };
  },
  mounted() {
    axios.get(`http://localhost:5000/items/${this.username}`).then((res) => {
      this.items = res.data.data;
    });
  },
  methods: {
    logout: function () {
      this.$cookie.set("username", "");
      eventBus.$emit("signout-success")
    }
  },
  components: {
    Items
  }
}
</script>



