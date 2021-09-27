<template>
  <div>
    <div class="inputs item-wrapper">
      <v-text-field
      label="Username"
      v-model="username"
      ></v-text-field>
      <v-text-field
      label="Password"
      v-model="password"
      ></v-text-field>
      
      <br/>
      <div class="next">
        <v-btn v-on:click="login">Login</v-btn>
        <v-btn v-on:click="signup">Sign Up</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import { eventBus } from "../main";
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  components: {
  },
  methods: {
    signup: function () {
      const bodyContent = {
        username: this.username,
        password: this.password,
      };
      axios
        .post("http://localhost:5000/users", bodyContent)
        .then((res) => {
          eventBus.$emit("message", res.data.message);
        })
        .catch((err) => {
          eventBus.$emit("error", err.response.data.error);
        })
    },
    login: function () {
      const bodyContent = {
        username: this.username,
        password: this.password,
      };
      axios
        .post("http://localhost:5000/users/login", bodyContent)
        .then((res) => {
          this.$cookie.set("username", res.data.user.username);
          eventBus.$emit("message", res.data.message);
          eventBus.$emit("signin-success");
        })
        .catch((err) => {
          eventBus.$emit("error", err.response.data.error);
        })
    },
  }
};
</script>



