<template>
  <div>
    <search v-bind:items="this.displayItems"/>
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
      searchTags: [],
      searchName: "",
      orderBy: "ascending",
      sortBy: "date"
    };
  },
  components: {
    Item,
    Search
  },
  computed: {
    
    displayItems: function() {
      let items = [...this.items]
      if (this.searchName.length > 0) {
        items = items.filter(each => each.name.toLowerCase().includes(this.searchName.toLowerCase()))
      }
      if (this.searchTags.length > 0) {
        items = items.filter(each => each.tags.some( tag => this.searchTags.includes(tag)))
      }
      switch(this.sortBy){
        case 'name':
          items.sort( (a,b) => this.compareStrings(a,b)) 
          break;
        case 'time':
          items.sort( (a,b) => this.compareStrings(a,b) )
          items = items.filter( each => each.time.length > 0)
          break;
        case 'date':
          items.sort( (a,b) => a.timestamp - b.timestamp )
          break;
        case 'random':
          this.shuffleArray(items)
          break;
      }
      if (this.orderBy == 'descending'){
        items = items.reverse()
      }
      return items
     }
     
  },
  mounted() {
    eventBus.$on("delete_item", (data) => {
      this.items = this.items.filter((item) => item.id !== data.id)
    });
    eventBus.$on("update_search_tags", (data) => {
      this.searchTags = data
    });
    eventBus.$on("update_search_name", (data) => {
      this.searchName = data
    });
    eventBus.$on("update_sort_by", (data) => {
      this.sortBy = data
    });
    eventBus.$on("update_order_by", (data) => {
      this.orderBy = data
    });
  },
  methods: {
    shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    },
    compareStrings: function(a, b) {
      var nameA = a.name.toUpperCase(); 
      var nameB = b.name.toUpperCase(); 
      if (nameA < nameB) {
        return -1;
      }
      if (nameA > nameB) {
        return 1;
      }

      // names must be equal
      return 0;
    },
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



