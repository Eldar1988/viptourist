import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    countries: null,
    city: null,
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
    },
    async loadCityDetail({commit}, id) {
      try{
        return axios.get(`${this.getters.getServerURL}/tours/city/${id}/`)
          .then(({data}) => commit('setCityDetail', data))
      } catch (e) {
        notifier(e.message)
      }
    }
  },
  mutations: {
    setCountries(state, data) {
      state.countries = data
    },
    setCityDetail(state, data) {
      state.city = data
    }
   },
  getters: {
    getCountries: state => state.countries,
    getCityDetail: state => state.city
  }
}
