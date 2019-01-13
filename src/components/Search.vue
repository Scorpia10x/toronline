<template lang='pug'>
  form.adress(@submit.prevent='explore()'
              method='GET' 
              action='/')
    input.field(v-model='queryStr'
                 type='search' 
                 placeholder='Enter adress of .onion resource' 
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
      if (!this.queryStr.includes('.onion') || this.queryStr.length < 22) return false;

      let pattern = new RegExp(/^(https?:\/\/)?([\da-z\.-]+){16,56}\.onion/);
      let substr = this.queryStr.match(pattern);

      if (!substr) return false;
      
      substr = substr[0]
    
      // For more speed
      if (substr.length <= 30) return pattern.test(substr.slice(0, 30));
      
      // For faster processing of Onion v3 adresses
      else return pattern.test(this.queryStr);
    }
  },
  watch: {
    isTorLink() {
      this.$parent.$emit('link-type-change', this.isTorLink)
    }
  },
  methods: {
    explore(e) {
      if (!this.isTorLink) {
        this.$snotify.info("Please, enter .onion adress into field.", {
          timeout: 3000,
          showProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true
        });
      } else {
        this.$snotify.success("Successfuly.", {
          timeout: 3000,
          showProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
        });
      }
    }
  }
}
</script>

<style scoped lang="scss">

.adress {
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

  .field, .submit {
    height: 100%;
    border: none;
  }

  .field {
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
    opacity: .7;
    background-repeat: no-repeat;
    background-position: center center;
    background-color: transparent;

    &:focus {
      outline: none;
    }

    &:hover {
      cursor: pointer;
    }

  }
}

</style>
