<template lang='pug'>
  form.explorer(method='GET' action='/')
    input.search(v-model='queryStr' 
                 type='search' 
                 placeholder='Enter request or .onion adress' 
                 name='r'
                 autofocus)
    .onion-link(v-show='isTorLink')
    input.submit(type='submit' value='' :style='goIcon')
</template>

<script>

export default {
  name: 'Search',
  data() {
    return {
      queryStr: ''
    }
  },
  computed: {
    queryType() {
      let urlPattern = new RegExp(/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-\?]*)*\/?/);
      return urlPattern.test(this.queryStr) ? 'visit' : 'search'
    },
    isTorLink() {
      if (this.queryType != 'visit') return false;
      let onionPattern = new RegExp(/([\da-z\.-]+){16,}\.onion/);
      return onionPattern.test(this.queryStr)
    },
    goIcon() {
      return {
        backgroundImage: `url("./${this.queryType}.svg")`
      }
    }
  }
}
</script>

<style scoped lang="scss">

.explorer {

  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid grey;
  width: 400px;
  background-color: white;

  @media screen and (max-width: 565px) {
    width: 90%;
  }

  @media screen and (max-width: 400px) {
    width: 70%;
  }

  .search, .submit, .onion-link {
    height: 40px;
    border: none;
  }

  .search {
    width: 100%;
    padding-left: 14px;
    background-color: transparent;

    &:focus {
      outline: none;
    }
  }

  .onion-link, .submit {
    padding: 0 7px;
    margin: 0 10px;
    background-size: contain !important;
  }

  .onion-link {
    background: url('../assets/onion.svg') no-repeat center;
  }

  .submit {
    width: fit-content;
    height: fit-content;
    outline: none;
    right: 10px;
    opacity: .7;
    background-repeat: no-repeat;
    background-position: center center;
    background-color: transparent;

    &:hover {
      cursor: pointer;
    }

  }

}

</style>
