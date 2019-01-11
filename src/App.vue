<template lang='pug'>
  #app
    router-view
</template>

<script>
export default {
  data() {
    return {

    }
  }
}
</script>

<style lang="scss">

body {
  margin: 0;
}

#app {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
