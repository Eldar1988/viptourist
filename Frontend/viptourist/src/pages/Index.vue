<template>
  <q-page class="">
    <vip-first-screen />
  </q-page>
</template>

<script>
import VipFirstScreen from "components/home/vipFirstScreen";
export default {
  name: 'PageIndex',
  components: {VipFirstScreen},
  preFetch({store}) {
    return store.dispatch('fetchHomeSlides')
  }
}
</script>
