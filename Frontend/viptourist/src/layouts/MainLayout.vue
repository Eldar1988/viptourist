<template>
  <q-layout view="lHh Lpr lFf">
    <vip-header/>

    <q-page-container>
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script>

import VipHeader from "components/header/vipHeader";

export default {
  name: 'MainLayout',
  components: {VipHeader},
  data() {
    return {}
  }
}
</script>
