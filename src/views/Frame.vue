<template lang='pug'>
  iframe(:src='url'
         frameborder='0'
         )
</template>

<script>

export default {
  name: 'frame',
  props: {
    query: {
      type: String,
      required: true
    }
  },
  computed: {
    url() {
      return 'http://' + this.query + '.ws'
    }
  }
}
</script>

<style lang="scss">;

iframe {
  width: 100%;
  height: 100vh;
}

</style>
