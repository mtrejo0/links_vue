<template>
  <div>
    <div class="item-wrapper">
      <h1>Hello {{username}}!</h1>
      <p>You have [{{this.items.length}}] items</p>
      <p>Your tags: {{this.uniqueTags()}}</p>
      <v-btn v-on:click="logout">Logout</v-btn>
    </div>
    <add-item/>
    <items v-bind:items="this.items"/>
  </div>
</template>

<script>
import { eventBus } from "../main";
import axios from "axios";
import Items from "./Items.vue";
import AddItem from './AddItem.vue';

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
    eventBus.$on("add_item", (data) => {
      this.items = this.items.concat(data)
    });
  },
  methods: {
    uniqueTags: function() {
      return Array.from(
      new Set(
        this.items.reduce((tags, item) => {
          return tags.concat(item.tags);
        }, [])
      )
    )},
    logout: function () {
      this.$cookie.set("username", "");
      eventBus.$emit("signout-success")
    }
  },
  components: {
    Items,
    AddItem
  }
}
</script>



