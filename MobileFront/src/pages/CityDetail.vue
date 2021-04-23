<template>
<q-page>
  <div v-if="city">
    <h2>{{ $t('failed') }}</h2>
  <q-img
    :src="city.full_image"
    class="city-detail-image"
  >
    <div class="city-detail-text-wrapper flex flex-center">
      <h1 class="text-h1 text-bold">{{ city.title }}</h1>
    </div>
    <template v-slot:loading>
      <q-skeleton class="full-width city-detail-image"/>
    </template>
  </q-img>
  <vip-categories-wrapper />
  </div>
</q-page>
</template>

<script>
import vipCategoriesWrapper from "components/categories/vipCategoriesWrapper";

export default {
  name: "CityDetail",
  components: {
    vipCategoriesWrapper
  },
  computed: {
    city() {
      return this.$store.getters.getCityDetail
    }
  },
  created() {
    this.$store.dispatch('loadCityDetail', this.$route.params.id)
  }
}
</script>

<style lang="sass">
.city-detail-image
  height: 400px

.city-detail-text-wrapper
  top: 0
  left: 0
  right: 0
  bottom: 0
  background: rgba(0,0,0, .2) !important

@media screen and (max-width: 650px)
  .city-detail-image
    height: 250px
</style>
