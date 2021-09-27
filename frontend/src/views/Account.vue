<template>
  <div>
    <Navbar/>
    <Messages/>
    <Account/>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import Messages from "./Messages.vue";
import Account from "../components/Account.vue"

export default {
  components: {
    Navbar,
    Account,
    Messages
  }
};
</script>



