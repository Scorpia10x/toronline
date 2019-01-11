<template lang='pug'>
  form.explorer
    input.search(type='search' placeholder='Enter request or .onion adress')
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
  border: 1px solid grey;
  width: 400px;

  @media screen and (max-width: 565px) {
    width: 90%;
  }

  @media screen and (max-width: 400px) {
    width: 70%;
  }

  .search, .submit {
    height: 40px;
    border: none;
  }

  .search {
    width: 100%;
    padding-left: 14px;
    background: transparent;

    &:focus {
      outline: none;
    }
  }

  .submit {
    width: fit-content;
    height: fit-content;
    outline: none;
    padding: 7px;
    margin: 0 10px;
    right: 10px;
    opacity: .7;
    background: url('../assets/search.svg');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 100%;
    background-color: transparent;
  }

}

</style>
