<template lang='pug'>
  form.explorer
    input.search(type='search' placeholder='Enter .onion adress or search request' autofocus)
    input.submit(type='submit' value='')
</template>

<script>
export default {
  name: 'Search'
}
</script>

<style scoped lang="scss">

.explorer {

  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid lightgrey;

  @media screen and (max-width: 400px) {
    width: 90%;
  }

  .search, .submit {
    height: 40px;
    border: none;
  }

  .search {
    width: 400px;
    padding-left: 10px;

    &:focus {
      outline: none;
    }
  }

  .submit {
    width: fit-content;
    height: fit-content;
    outline: none;
    padding: 5px;
    margin: 0 10px;
    right: 10px;
    opacity: .7;
    background: url('../assets/search.svg') no-repeat center center;
    background-color: transparent;
  }

}

</style>
