<template>
  <Home />
</template>

<style lang="scss">
body{
  margin: 0;
  padding: 0;
  //box-sizing: border-box;
  overflow-y: auto;
  overflow-x: hidden;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
<script>
import Home from "@/views/Home";
export default {
  components: {Home}
}
</script>