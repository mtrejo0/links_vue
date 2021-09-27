<template>
  <v-app>
    <div id="app">
      <!-- Set name or it defaults to '/' in router.js -->
      <router-view />
    </div>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
:root {
  font-family: Arial, Helvetica, sans-serif;
  --main-color: blue;
}

a:visited {
  color: var(--main-color);
}

.header {
  color: var(--main-color);
  text-align: center;
}

.component {
  align-items: center;
  margin-bottom: 5%;
}

.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin: 32px;
}

.form-container > * {
  margin: 0.5rem;
  margin-bottom: 50px;
}

.form-container input {
  font-size: 1.2em;
  padding: 6px;
}

.button {
  max-height: 3em;
  font-size: 1.1em;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  border-radius: 5px 5px 5px 5px;
  padding: 0.35em 0.75em;
  color: rgb(255, 255, 255);
  border: none;
  display: inline-block;
  cursor: pointer;
  margin: 8px;
}

.center {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.margin-auto {
  margin: 0 auto;
}

.next {
  display: flex;
  justify-content: center;
  flex-direction: row;
}
.next-center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}

.item-wrapper {
  padding: 32px;
  border-radius: 32px;
  box-shadow: 0px 0px 12px 6px #eee;
  margin: 16px 12px;
}


.flex {
  display: flex;
}

* {
  box-sizing: border-box;
}

body {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.success-message {
  color: green;
}

.error-message {
  color: red;
}

.loading {
  margin: 32px auto;
}
</style>
