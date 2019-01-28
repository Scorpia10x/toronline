<template lang='pug'>
  #app
    transition(name='rotate' mode='out-in')
      router-view(v-if='!isTransition')
      .transition-layer(v-else :style='display')
</template>

<script>

export default {
  data() {
    return {
      title: "Tor Online",
      isTransition: false,
      initialState: true
    }
  },
  computed: {
    display() {
      return {
        'display' : this.initialState ? "none" : "flex"
      }
    }
  },
  mounted() {
    this.isTransition = false;
    this.initialState = false;
    this.$root.$on('transition', state => this.isTransition = state)
  }
}
</script>

<style lang="scss">

// App styles

#app {
  background: url('./assets/texture.jpg');
  background-color: #111111;
  display: grid;
  grid-template: 1fr / 1fr;
  min-height: 100vh;
  font-family: Helvetica, Arial, sans-serif;
  color: #d4d4d4;
}

.rotate-enter-active, .rotate-leave-active {
  transition: transform .3s
}
.rotate-enter, .rotate-leave-to {
  transform: rotateX(90deg)
}

.transition-layer {
  width: 100vw;
  height: 100vh;
  background-color: white;
  place-self: center;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: bright .1s linear both;
  animation-delay: .3s;
}

@keyframes bright {

  from {
    opacity: 0
  }

  to {
    opacity: 1
  }

}


</style>
