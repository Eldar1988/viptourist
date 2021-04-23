import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    categories: null
  },
  actions: {
    async loadCategoriesByCity({commit}, id) {
      try {
        return axios.get(`${this.getters.getServerURL}/tours/categories_by_city/${id}/`)
          .then(({data}) => commit('setCategories', data.results))
      } catch (e) {
        notifier(e.message)
      }
    }
  },
  mutations: {
    setCategories(state, data) {
      state.categories = data
    }
  },
  getters: {
    getCategories: state => state.categories
  }
}
