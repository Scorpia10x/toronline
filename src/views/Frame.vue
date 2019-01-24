<template lang='pug'>
    iframe(v-if='!!url'
           :src='url'
           frameborder='0'
           )
    p(v-else class='notice') Please enter correct .onion adress.
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
  data() {
    return {
      proxy: 'ws'
    }
  },
  computed: {
    url() {
      let position = this.query.indexOf('.onion') + 6;
      let array = this.query.split('');

      if (!this.query.includes(`.${this.proxy}`)) {
        array.splice(position, 0, `.${this.proxy}`);
      }
      
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

.notice {
  color: black;
}

</style>
