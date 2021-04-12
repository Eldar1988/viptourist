import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    countries: null
  },
  actions: {
    async loadCountriesAndCities({commit, state}) {
      try{
        if(!state.countries) {
          return axios.get(`${this.getters.getServerURL}/tours/get_places/`)
            .then(({data}) => commit('setCountries', data))
        }
      } catch (e) {
        notifier(e.message)
      }
    }
  },
  mutations: {
    setCountries(state, data) {
      state.countries = data
    }
  },
  getters: {
    getCountries: state => state.countries
  }
}
