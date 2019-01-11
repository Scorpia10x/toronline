<template lang='pug'>
  .home
    h1.title
      span.tor-color {{ $parent.title.slice(0, 3) }}
      .
        {{ $parent.title.slice(3) }}
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

    .tor-color {
      color: darkviolet;
    }

  }

}

</style>
