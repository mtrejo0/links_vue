<template>
  <div>
    <div class="item-wrapper">
      Search
      <vue-tags-input
        v-model="tag"
        :tags="tags"
        :autocomplete-items="filteredItems"
        @tags-changed="updateSearch"
      />
    </div>
  </div>
</template>

<script>
import { eventBus } from "../main";
import VueTagsInput from '@johmun/vue-tags-input';

export default {
  props: {
    uniqueTags: Array,
    items: Array
  },
  data() {
    return {
      tag: "",
      tags: []
    };
  },
  components: {
    VueTagsInput
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
  },
  
  methods: {
    updateSearch: function (newTags) {
      this.tags = newTags
      eventBus.$emit("update_search", newTags.map(each => each.text));
    }
  }
};
</script>



