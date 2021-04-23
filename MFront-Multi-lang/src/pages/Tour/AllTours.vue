<template>
  <q-page>
    <div>
      <q-infinite-scroll @load="onLoad" :offset="700">
        <div v-for="(tour, index) in tours" :key="index" class="caption">
          <div class="flex flex-center" style="height: 700px">
            <p>{{ tour.title }}</p>
          </div>
        </div>
          <template v-slot:loading>
            <div class="row justify-center q-my-md" v-if="!allToursLoaded">
              <q-spinner-dots color="primary" size="40px"/>
            </div>
          </template>
      </q-infinite-scroll>
    </div>

    <div></div>
  </q-page>
</template>

<script>
export default {
  name: "AllTours",
  data() {
    return {
      tours: [],
      allToursLoaded: false
    }
  },
  created() {
    // this.onLoad(1, false)
  },
  methods: {
    async onLoad(index, done) {
      if (!this.allToursLoaded) {
        if (this.tours) {
          await this.$axios.get(`${this.$store.getters.getServerURL}/tours/tours_by_city/${this.$route.params.id}/?page=${index}`)
            .then(response => this.pushTours(response.data.results))
            .catch(e => this.allToursLoaded = true)
          done()
        }
      }
    },
    pushTours(tours) {
      tours.forEach(tour => this.tours.push(tour))
    }

  }
}
</script>

<style scoped>

</style>
