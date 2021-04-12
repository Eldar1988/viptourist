<template>
  <q-page class="">
    <vip-home-slider />
    <vip-countries-and-cities />
  </q-page>
</template>

<script>
import VipHomeSlider from "components/home/vipHomeSlider";
import VipCountriesAndCities from "components/home/vipCountriesAndCities";
export default {
  name: 'PageIndex',
  components: {VipCountriesAndCities, VipHomeSlider},
  preFetch({store}) {
    return store.dispatch('loadCountriesAndCities')
  }
}
</script>
