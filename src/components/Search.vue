<template lang='pug'>
  form.adress(v-if='!isDirectlyQuery'
              @submit.prevent='explore()'
              method='GET' 
              action='/')
    input.field(v-model='strQuery'
                :class='invalidValue ? "invalid" : ""'
                @input='invalidValue = false'
                type='search' 
                placeholder='Enter adress of .onion resource' 
                autocomplete='off'
                autofocus)
    input.submit(type='submit' 
                 value='')
  p(v-else class='info') Page loading...
</template>

<script>

import regexes from '../utils/regexes';

export default {
  name: 'Search',
  props: {
    urlQuery: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      invalidValue: false,
      strQuery: '',
      proxy: 'pet'
    }
  },
  computed: {
    query() {
      return this.urlQuery || this.strQuery
    },
    isTorLink() {
      return this.query.includes('.onion') &&
             !this.query.length < 22 &&
             regexes.onionLink.test(this.query)
    },
    isDirectlyQuery() {
      return ( (this.query == this.urlQuery) && this.isTorLink )
    }
  },
  watch: {
    isTorLink() {
      this.$parent.$emit('link-type-change', this.isTorLink);
    }
  },
  methods: {
    explore() {
      if (this.isTorLink) {
        this.$root.$emit('transition', true);
        
        let url = this.query;
        if (!url.includes(this.proxy))
          url = url.replace(/\.onion/, `.onion.${this.proxy}`);
        
        window.location.href = url

      } else {
        this.invalidValue = true;
        setTimeout(() => {
          this.invalidValue = false;
        }, 600);
      }
    }
  },
  created() {
    if ( (this.urlQuery == this.query) && this.isTorLink )
      this.explore();

    this.$on('link-type-change', type => this.explore());
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
  transition: border-color .1s;

  .field.invalid {
    animation: validationError .6s alternate;
  }

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
