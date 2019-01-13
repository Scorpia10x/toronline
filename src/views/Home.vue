<template lang='pug'>
  .explorer
    img.logo(:src='actualLogo')
    h1.title {{ $parent.title }}
    Search
</template>

<script>

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
  computed: {
    actualLogo() {
      let suffix = this.isTorLink ? '-green' : '';
      return `./onion${suffix}.png`
    }
  },
  mounted() {
    this.$on('link-type-change', type => this.isTorLink = type)
  }
}
</script>

<style lang="scss">;

.explorer {
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
    min-width: 330px;

    @media screen and (max-width: 565px) {
      font-size: 2em;
      text-align: center;
      min-width: 0;
    }
  }
}

</style>
