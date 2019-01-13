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
      let position = this.query.indexOf('.onion') + 6;
      let array = this.query.split('');
      array.splice(position, 0, '.ws');
      let url = array.join('');
      return 'http://' + url
    }
  }
}
</script>

<style lang="scss">;

iframe {
  background-image: none;
  background-color: white;
  width: 100%;
  height: 100vh;
}

</style>
