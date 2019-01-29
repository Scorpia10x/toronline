<template lang='pug'>
  form.adress(@submit.prevent='explore()'
              method='GET' 
              action='/')
    input.field(v-model='query'
                :class='invalidValue ? "invalid" : ""'
                @input='invalidValue = false'
                type='search' 
                placeholder='Enter adress of .onion resource' 
                autocomplete='off'
                autofocus)
    input.submit(type='submit' 
                 value='')
</template>

<script>

export default {
  name: 'Search',
  props: {
    proxyList: {
      required: true
    }
  },
  data() {
    return {
      invalidValue: false,
      query: '',
      proxy: null
    }
  },
  computed: {
    isTorLink() {
      return this.query.includes('.onion') &&
             !this.query.length < 22 &&
             /^(https?:\/\/)?([\da-z\.-]+){16,56}\.onion(\/.*)?$/.test(this.query)
    }
  },
  watch: {
    isTorLink() {
      this.$parent.$emit('link-type-change', this.isTorLink)
    },
    proxyList() {
      this.proxy = this.proxyList[0].name
    }
  },
  methods: {
    explore() {
      if (this.isTorLink) {

        if (this.query.slice(0, 7) != 'http://')
          this.query = `http://${this.query}`;

        if (!this.query.includes(this.proxy))
          this.query = this.query.replace(/\.onion/, `.onion.${this.proxy}`);

        this.$root.$emit('transition', true);
        
        window.location.href = this.query

      } else {

        this.invalidValue = true;
        setTimeout(() => {
          this.invalidValue = false
        }, 600);
        
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
    transition: color .1s;

    &.invalid {
      animation: validationError .6s alternate;
    }

    &:focus {
      outline: none;
    }

  }

  .submit {
    padding: 0 7px;
    margin-left: 10px;
    background-image: url("../assets/visit.svg");
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

@keyframes validationError {
  0% {
    color: inherit;
  }

  25% {
    color: indianred;
  }

  75% {
    color: indianred;
  }

  100% {
    color: inherit;
  }

}

</style>
