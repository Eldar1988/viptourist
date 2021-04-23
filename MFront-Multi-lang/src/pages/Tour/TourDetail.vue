<template>
  <q-page>
    <article>
      <vip-tour-images-slider :images="tour.images"/>
      <div class="tour-detail q-pa-md">
        <h1 class="text-h1 text-bold q-mt-sm">{{ tour.title }}</h1>
        <div class="tour-detail-section">
          <div v-html="tour.short_description"></div>
        </div>
      </div>
    </article>
  </q-page>
</template>

<script>
import vipTourImagesSlider from "components/sliders/vipTourImagesSlider"


export default {
  name: "TourDetail",
  components: {
    vipTourImagesSlider
  },
  computed: {
    tour() {
      return this.$store.getters.getTour
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('loadTourDetail', currentRoute.params.id)
  }
}
</script>

<style scoped>

</style>
