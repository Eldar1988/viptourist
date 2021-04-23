import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    tour: null
  },
  actions: {
    async loadTourDetail({commit}, id) {
      try {
        return axios.get(`${this.getters.getServerURL}/tours/tour/${id}/`)
          .then(({data}) => {commit('setTour', data)})
      } catch (e) {
        notifier(e.message)
      }
    }
  },
  mutations: {
    setTour(state, data) {
      state.tour = data
    }
  },
  getters: {
    getTour: state => state.tour
  }
}
