<template>
  <header class="header">
    <div
      v-if="!$q.platform.is.mobile"
      class="header-wrapper q-pa-sm flex justify-end hide-on-mobile"
    >
      <div class="logo">
        <router-link to="/" class="logo-text text-bold text-white">
          VIP Tourist
        </router-link>
      </div>
      <div class="desktop-nav">
      </div>
    </div>
  </header>

</template>

<script>
export default {
  name: "vipHeader"
}
</script>

<style lang="sass">
.header
  position: absolute
  top: 0
  left: 0
  width: 100%
  color: #fff
  background: rgba(0, 0, 0, 0) !important
  z-index: 10

.logo-text
  font-size: 16px

</style>
