<template lang='pug'>
  #app
    router-view
    vue-snotify
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

// App styles

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

// Notifications: theme import and overwrite
@import "~vue-snotify/styles/dark";

.snotify {

  &-rightBottom {
    bottom: 20px;
    right: 20px;
  }

  &-icon {
    opacity: .6;
    right: 20px;
  }

  &Toast {
    background-color: rgba(0, 0, 0, .6);

    &__progressBar {
      background-color: rgba(0, 0, 0, .6);
    }

    &__body {
      text-align: left;
      line-height: 1.5;
    }

    &__inner {
      padding: 15px 75px 15px 25px;
    }
  }

}

</style>
