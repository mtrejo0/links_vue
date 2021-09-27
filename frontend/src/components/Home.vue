<template>
  <div>
    <div class="inputs item-wrapper">
      <v-text-field
      label="Name"
      v-model="name"
      ></v-text-field>
      <v-text-field
      label="Link"
      v-model="link"
      ></v-text-field>
      <v-text-field
      label="Description"
      v-model="description"
      ></v-text-field>
      <vue-tags-input
        v-model="tag"
        :tags="tags"
        :autocomplete-items="uniqueTags"
        @tags-changed="newTags => tags = newTags"
      />
      <br/>
      <v-btn v-on:click="addItem">Save</v-btn>
    </div>
    <items v-bind:items="this.items"/>
  </div>
</template>

<script>
import axios from "axios";
import Items from "./Items.vue";
import VueTagsInput from '@johmun/vue-tags-input';

export default {
  data() {
    return {
      name: "",
      link: "",
      description: "",
      tag: "",
      tags: [],
      items: [],
      username: this.$cookie.get('username')
    };
  },
  

  components: {
    Items,
    VueTagsInput
  },
  
  mounted() {
    axios.get("http://localhost:5000/items").then((res) => {
      this.items = res.data.data;
    });

  },
  methods: {
    addItem: function () {
    if (!this.name) {
      return;
    }

    let newItem = {
        name: this.name,
        tags: this.tags.map(each => each.text),
        link: this.link,
        description: this.description,
        username: this.username,
      }
    axios.post("http://localhost:5000/items", { item: newItem }).then((res) => {
      this.items = this.items.concat(res.data.item),
      this.name = ""
      this.link = ""
      this.description = ""
      this.tag = ""
      this.tags = []
    });
    }
  }
};
</script>

<style scoped>
  .inputs {
    width: 50%;
    margin: 16px;
  }
</style>



