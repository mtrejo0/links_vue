<template>
  <div>
    <v-toolbar color="light-blue accent-4" dense dark>
      <v-toolbar-title>Grassroots</v-toolbar-title>
      <v-spacer></v-spacer>
      <router-link to="/">
        <button
          v-bind:class="{ selected: $route.name == 'home' }"
          class="button"
        >
          Home
        </button>
      </router-link>
      <router-link to="/account">
        <button
          v-bind:class="{ selected: $route.name == 'account' }"
          class="button"
        >
          Account
        </button>
      </router-link>
    </v-toolbar>
  </div>
</template>
<script>
export default {
  name: "NavBar"
};
</script>

<style scoped>
.selected {
  background: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border: 2px black solid;
}
</style>


