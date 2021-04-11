<template>
  <div id="app">
    <Navbar/>
    <div class="view">
      <router-view/>
    </div>
  </div>
</template>
<script>
  import Navbar from './components/Navbar.vue';
  export default {
    components: {
      Navbar,
    },
  }
</script>
<style>
  html, body {
    height: 100%;
    width: 100%;
  }
  #app {
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  .view {
    margin-top: 100px;
  }
</style>
