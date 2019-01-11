<template lang='pug'>
  .home
    h1.title Torland's Gate
    Search
</template>

<script>
// @ is an alias to /src
import Search from '@/components/Search.vue'

export default {
  name: 'home',
  components: {
    Search
  }
}
</script>

<style lang="scss">

.home {

  margin-top: -60px;
  display: flex;
  flex-direction: column;
  align-items: center;

  @media screen and (max-width: 400px) {
    width: 100%;
  }

  .title {
    margin-top: 0;
    font-size: 3em;
    user-select: none;

    @media screen and (max-width: 400px) {
      font-size: 2em;
    }
  }

}

</style>
