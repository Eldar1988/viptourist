<template>
<div>
  <q-toolbar class="header-grid">
    <div>
      <q-btn
        icon="las la-home"
        flat dense
        to="/"
      />
    </div>
    <q-toolbar-title class="text-center text-bold text-uppercase">
      VIP Tourist
    </q-toolbar-title>
    <div class="text-right">
      <q-btn
        icon="las la-search"
        flat dense
        to="/"
      />
    </div>
  </q-toolbar>
</div>
</template>

<script>
export default {
name: "vipHeader"
}
</script>

<style lang="sass">
.header-grid
  display: grid
  grid-template-columns: 1fr 2fr 1fr
  &:after
    content: ""
    top: 0
    bottom: 0
    right: 0
    left: 0
    position: absolute
    z-index: -1
    background: linear-gradient(360deg, transparent 10%,#21BA45)
</style>
