<template>
  <div>
    <div class="inputs item-wrapper">
      <div class="flex">
        <v-text-field
          label="Name"
          v-model="name"
          class="input"
        ></v-text-field>
        <v-text-field
          label="Description"
          v-model="description"
          class="input"
        ></v-text-field>
      </div>
      <div class="flex">
        <v-text-field
          label="Link"
          v-model="link"
          class="input"
        ></v-text-field>
        <v-text-field
          label="Time Commitment (min)"
          v-model="timeCommitment"
          type="number"
          min="0"
          step="10"
          class="input"
        ></v-text-field>
      </div>
      <div class="flex">
        <vue-tags-input
          v-model="tag"
          :tags="tags"
          :autocomplete-items="uniqueTags"
          @tags-changed="newTags => tags = newTags"
          class="tags"
        />
        <v-btn v-on:click="addItem">Add Item</v-btn>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main";
import VueTagsInput from '@johmun/vue-tags-input';

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
  computed: {
    uniqueTags: function() {
      return Array.from(
      new Set(
        this.items.reduce((tags, item) => {
          return tags.concat(item.tags);
        }, [])
      )
    )},
  },
  components: {
    VueTagsInput
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
        time: this.timeCommitment
      }
    axios.post("http://localhost:5000/items", { item: newItem }).then((res) => {
      this.items = this.items.concat(res.data.item)
      eventBus.$emit("add_item", res.data.item);
      this.name = ""
      this.link = ""
      this.description = ""
      this.time = ""
      this.tag = ""
      this.tags = []
    });
    }
  }
};
</script>

<style scoped>
  .inputs {
    margin: 16px;
  }
  .input {
    margin: 8px;
  }
  .tags {
    width: 450px;
    margin-right: 32px;
  }
</style>



