<template>
  <h1>Jobs</h1>
  <div class="job" v-for="job in jobs" :key="job.id">
    <h2>
      <router-link :to="{ name: 'jobDetails', params: { id: job.id } }">{{
        job.title
      }}</router-link>
    </h2>
  </div>
</template>

<script setup>
const jobs = [
  { title: "Ninja UX Designer", id: 1, details: "lorem" },
  { title: "Ninja Web Developer", id: 2, details: "lorem" },
  { title: "Ninja Vue Developer", id: 3, details: "lorem" },
];
</script>

<style>
.job h2 {
  background: #f4f4f4;
  padding: 20px;
  border-radius: 10px;
  margin: 10px auto;
  max-width: 600px;
  cursor: pointer;
  color: #444;
}
.job h2:hover {
  background: #ddd;
}
.job a {
  text-decoration: none;
}
</style>
