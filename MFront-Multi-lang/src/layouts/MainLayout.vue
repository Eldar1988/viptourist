<template>
  <q-layout view="hHh lpR fFf">

    <q-header class="text-white header" style="background: transparent">
      <vip-header />
    </q-header>

    <q-page-container style="padding-top: 0">
      <router-view />
    </q-page-container>

    <div>
      <vip-bottom-navigation />
    </div>

    <vip-footer />

  </q-layout>
</template>

<script>
import VipHeader from "components/header/vipHeader";
import VipBottomNavigation from "components/utils/vipBottomNavigation";
import VipFooter from "components/footer/vipFooter";
export default {
  components: {VipFooter, VipBottomNavigation, VipHeader},
  data () {
    return {
    }
  }
}
</script>
