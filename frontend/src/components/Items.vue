<template>
  <div>
    <search v-bind:uniqueTags="uniqueTags" v-bind:items="this.items"/>
    <div>
      <Item v-for="(item , i) in displayItems" v-bind:key="i" v-bind:item="item"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main";
import Item from "./Item.vue";
import Search from './Search.vue';

export default {
  props: {
    items: Array
  },
  data() {
    return {
      name: "",
      link: "",
      description: "",
      tag: "",
      tags: [],
      searchTags: []
    };
  },
  components: {
    Item,
    Search
  },
  computed: {
    uniqueTags: function() {
      return Array.from(
      new Set(
        this.items.reduce((tags, item) => {
          return tags.concat(item.tags);
        }, [])
      )
    )
    },
    displayItems: function() {
      if (this.searchTags.length == 0) {
        return this.items
      }
      return this.items.filter(each => each.tags.some( tag => this.searchTags.includes(tag)))
     }
  },
  mounted() {
    eventBus.$on("delete_item", (data) => {
      this.items = this.items.filter((item) => item.id !== data.id)
    });

    eventBus.$on("update_search", (data) => {
      this.searchTags = data
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



