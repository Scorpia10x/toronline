<template lang='pug'>
    iframe(:src='url'
           frameborder='0'
           )
</template>

<script>

import regexes from '../utils/regexes';

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
      let url = 'http://' + array.join('');
      return regexes.onionLinkPattern.test(url) ? url : false;
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
