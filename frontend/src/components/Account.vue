<template>
  <div>
    <sign-in v-if="!isSignedIn"/>
    <profile v-else/>
  </div>
</template>

<script>
import SignIn from "./SignIn.vue";
import Profile from "./Profile.vue"
import { eventBus } from "../main";

export default {
  data() {
    return {
      isSignedIn: this.$cookie.get('username')
    };
  },
  components: {
    SignIn,
    Profile
  },
  created: function() {
    eventBus.$on("signin-success", () => {
      this.isSignedIn = this.$cookie.get('username');
    });

    eventBus.$on("signout-success", () => {
      this.isSignedIn = null;
    });

  },
}
</script>



