<template>
  <div>
    <Navbar/>
    <Messages/>
    <Home/>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import Messages from "./Messages.vue";
import Home from "../components/Home.vue"

export default {
  components: {
    Navbar,
    Home,
    Messages
  }
};
</script>



