<template>
<div class="q-pl-md">
  <div
    v-for="country in countries"
    :key="country.id"
    class="q-mt-md"
  >
  <vip-section-title :title="country.title"/>
  <vip-cities-slider :cities="country.cities"/>
  </div>
</div>
</template>

<script>
import VipSectionTitle from "components/utils/vipSectionTitle";
import VipCitiesSlider from "components/sliders/vipCitiesSlider";
export default {
  name: "vipCountriesAndCities",
  components: {VipCitiesSlider, VipSectionTitle},
  computed: {
    countries() {
      return this.$store.getters.getCountries
    }
  }
}
</script>

<style scoped>

</style>
