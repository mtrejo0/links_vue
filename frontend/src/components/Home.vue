<template>
  <div>
    <add-item/>
    <items v-bind:items="this.items"/>
  </div>
</template>

<script>
import axios from "axios";
import Items from "./Items.vue";
import AddItem from './AddItem.vue';
import { eventBus } from "../main";

export default {
  data() {
    return {
      name: "",
      link: "",
      description: "",
      timeCommitment: "",
      tag: "",
      tags: [],
      items: [],
      username: this.$cookie.get('username')
    };
  },

  components: {
    Items,
    AddItem
  },
  
  mounted() {
    axios.get("http://localhost:5000/items").then((res) => {
      this.items = res.data.data;
    });

    eventBus.$on("add_item", (data) => {
      this.items = this.items.concat(data)
    });

  },
};
</script>

<style scoped>
  .inputs {
    width: 50%;
    margin: 16px;
  }
</style>



