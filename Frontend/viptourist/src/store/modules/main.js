import axiosInstance from 'axios'
import notifier from "src/utils/notifier"

export default {

  state: {
    homeSlides: null
  },

  actions: {
    async fetchHomeSlides({commit, state}) {

      if (!state.homeSlides) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/main/home_slides/`)
            .then(({data}) => commit('setHomeSlides', data))
        } catch (e) {
          notifier(e.message)
        }
      }

    }
  },

  mutations: {
    setHomeSlides(state, data) {
      state.homeSlides = data
    }
  },

  getters: {
    getHomeSlides: state => state.homeSlides
  }
}
