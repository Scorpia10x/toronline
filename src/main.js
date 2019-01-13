import Vue from 'vue'
import App from './App.vue'
import router from './router'

// Normalize.css
import normalize from 'normalize.css'

// vue-lodash
import VueLodash from 'vue-lodash'
Vue.use(VueLodash)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
