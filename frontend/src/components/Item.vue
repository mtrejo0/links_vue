<template>
  <div class="item-wrapper item">
    <div>
        <strong>
            <div v-if="item.link">
                <a :href="item.link" target="_blank" rel="noreferrer">
                {{item.name}}
            </a>
            </div>
            <div v-else>{{item.name}}</div>
        </strong>
        <div v-if="item.tags.length">
            <strong>Tags: </strong> {{item.tags.join(", ")}}
        </div>
        <div v-if="item.description">
            <strong>Description: </strong>  {{item.description}}
        </div>
        <div v-if="item.time">
            <strong>Time commitment: </strong> {{item.time}} min
        </div>
        
    </div>
    <div>
        <v-btn v-if="this.username.length > 0 && item.username == this.username" v-on:click="deleteItem()">
            Delete
        </v-btn>
        <div v-if="item.timestamp">
            {{new Date(item.timestamp * 1000).toLocaleDateString("en-US")}}
            {{new Date(item.timestamp * 1000).toLocaleTimeString("en-US")}}
        </div>
        <div v-if="item.username">
            By: {{item.username}}
        </div>
    </div>
    
  </div>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main";

export default {
    props: {
        item: Object
    },
    data() {
        return {
            username: this.$cookie.get('username'),
        }
    },
    methods: {
    deleteItem: function () {
        axios
        .delete("http://localhost:5000/items/" + this.item.id)
        .then(() => {
            eventBus.$emit("delete_item", { id: this.item.id });
        });
    },
  },

}
</script>

<style scoped>
    .item {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
</style>
