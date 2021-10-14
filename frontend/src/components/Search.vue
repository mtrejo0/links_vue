<template>
  <div>
    <div class="item-wrapper">
      <vue-tags-input
        placeholder="Search Tags!"
        v-model="tag"
        :tags="tags"
        :autocomplete-items="this.filteredItems"
        @tags-changed="updateSearchTags"
      />
      <br/>
      <div>
        <input list="names" class="name-input" v-model="name" placeholder="Seach Names!" @change="updateSearchName">
        <datalist id="names">
          <option v-for="(item, i) in this.items" v-bind:key="i" :value="item.name">
          </option>
        </datalist>
      </div>
      <br>
      <div class="radio">
        <p>Sort By: </p>
        <div class="radio-item">
          <input type="radio" id="name" value="name" v-model="sortBy">
          <label for="name">Name</label>
        </div>
        <div class="radio-item">
        <input type="radio" id="date" value="date" v-model="sortBy">
        <label for="date">Date</label>
        </div>
        <div class="radio-item">
        <input type="radio" id="time" value="time" v-model="sortBy">
        <label for="time">Time</label>
        </div>
        <div class="radio-item">
        <input type="radio" id="random" value="random" v-model="sortBy">
        <label for="random">Random</label>
        </div>
      </div>
      <div class="radio">
        <p>Order: </p>
        <div class="radio-item">
          <input type="radio" id="ascending" value="ascending" v-model="orderBy">
          <label for="ascending">Low-High</label>
        </div>
        <div class="radio-item">
          <input type="radio" id="descending" value="descending" v-model="orderBy">
          <label for="descending">High-Low</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { eventBus } from "../main";
import VueTagsInput from '@johmun/vue-tags-input';

export default {
  props: {
    items: Array
  },
  data() {
    return {
      tag: "",
      tags: [],
      name: "",
      sortBy: "date",
      orderBy: "ascending"
    };
  },
  components: {
    VueTagsInput
  },
  watch: {
    sortBy: {
      handler: function(val) {
        eventBus.$emit("update_sort_by", val);
      }
    },
    orderBy: {
      handler: function(val) {
        eventBus.$emit("update_order_by", val);
      }
    }
  }, 
  computed: {
    filteredItems() {
      if (this.tag == "") {
        return this.uniqueTags
      }
      return this.uniqueTags.filter(tag => {
        return tag.toLowerCase().indexOf(this.tag.toLowerCase()) !== -1;
      });
    },
    uniqueTags: function() {
      return Array.from(
      new Set(
        this.items.reduce((tags, item) => {
          return tags.concat(item.tags);
        }, [])
      )
    )},
  },
  
  methods: {
    
    updateSearchTags: function (newTags) {
      this.tags = newTags
      eventBus.$emit("update_search_tags", newTags.map(each => each.text));
    },
    updateSearchName: function () {
      eventBus.$emit("update_search_name", this.name);
    }
  }
};
</script>

<style scoped>
  .name-input {
    border: 1px rgb(200, 200, 200) solid;
    width: 450px;
    padding: 4px 8px;
  }

  .radio {
    display: flex;
    align-items: center;
  }
  .radio-item {
    margin: 8px;
  }
</style>



