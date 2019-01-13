<template lang='pug'>
  form.explorer(method='GET' action='/')
    input.search(v-model='queryStr'
                 type='search' 
                 placeholder='Enter request or .onion adress' 
                 name='r'
                 autocomplete='off'
                 autofocus)
    input.submit(type='submit' 
                 value='' 
                 style='background-image: url("./visit.svg")')
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
    isTorLink() {
      let urlPattern = new RegExp(/^(https?:\/\/)?([\da-z\.-]+){16,}\.onion([\/\w \.-\?]*)*\/?/);
      return urlPattern.test(this.queryStr)
    }
  },
  watch: {
    isTorLink() {
      this.$parent.$emit('link-type-change', this.isTorLink)
    }
  }
}
</script>

<style scoped lang="scss">

.explorer {

  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid lightgrey;
  background-color: transparent;
  height: 40px;
  grid-area: search;
  align-self: end;

  @media screen and (max-width: 565px) {
    width: 80vw;
  }

  .search, .submit {
    height: 40px;
    border: none;
  }

  .search {
    width: 100%;
    background-color: transparent;
    color: whitesmoke;

    &:focus {
      outline: none;
    }
  }

  .submit {
    padding: 0 7px;
    margin-left: 10px;
    background-size: contain !important;
    width: fit-content;
    height: fit-content;
    outline: none;
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
