<template>
  <q-page class="">
    <section>
      <vip-home-slider/>
    </section>
    <section>
      <vip-countries-and-cities/>
    </section>
  </q-page>
</template>

<script>
import VipHomeSlider from "components/home/vipHomeSlider";
import VipCountriesAndCities from "components/home/vipCountriesAndCities";

export default {
  name: 'PageIndex',
  components: {VipCountriesAndCities, VipHomeSlider},
  created() {
    this.$store.dispatch('loadCountriesAndCities')
  },
  // preFetch({store}) {
  //   return store.dispatch('loadCountriesAndCities')
  // }
}
</script>
