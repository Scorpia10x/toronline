<template lang='pug'>
  #app
    router-view
</template>

<script>

export default {
  data() {
    return {
      title: "Tor Online"
    }
  }
}
</script>

<style lang="scss">

#app {
  background: url('./assets/texture.jpg');
  background-color: #111111;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #d4d4d4;
}

</style>
