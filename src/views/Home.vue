<template lang='pug'>
  .home
    img.logo(v-if='!isTorLink' src='../assets/onion.png')
    img.logo(v-else src='../assets/onion-green.png')
    h1.title {{ $parent.title }}
    Search
</template>

<script>
// @ is an alias to /src
import Search from '@/components/Search.vue'

export default {
  name: 'home',
  components: {
    Search
  },
  data() {
    return {
      isTorLink: null
    }
  },
  mounted() {
    this.$on('link-type-change', type => this.isTorLink = type)
  }
}
</script>

<style lang="scss">;

.home {
  display: grid;
  grid: "logo title"
        "logo search";
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 40px;

  @media screen and (max-width: 565px) {
    width: 100%;
    grid: "logo"
          "title"
          "search";
    grid-template-rows: repeat(3, fit-content);
    grid-row-gap: 30px;
    place-content: center;
    justify-items: center;
    margin-top: -100px;
  }

  .logo {
    grid-area: logo;
    filter: brightness(3);
    user-select: none;
    width: 73px;
  }

  .title {
    margin: 0;
    font-size: 3em;
    user-select: none;
    text-align: left;
    grid-area: title;
    align-self: end;

    @media screen and (max-width: 575px) {
      font-size: 2em;
      text-align: center;
    }
  }

}

</style>
