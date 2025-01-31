<template>
  <div>{{ userData }}</div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { get_user_profile } from "../api/endpoint";

// Create a reactive reference to store user data
const userData = ref(null);

// Function to fetch user data based on username
const get_user = (username) => {
  if (!username) {
    console.error("Username is required");
    return;
  }

  get_user_profile(username)
    .then((res) => {
      userData.value = res;
      console.log(userData.value);
    })
    .catch((error) => {
      console.error("Error fetching user profile:", error);
    });
};

onMounted(() => {
  // Replace with the actual username you want
  get_user(); // Pass username to the function
});
</script>

<style lang="scss" scoped></style>
