<template>
<div>
  <q-card class="bottom-toolbar">
    <div class="bottom-navigation">
      <div class="text-center">
      <q-btn
        :label="$t('search')"
        icon="las la-search"
        color="dark"
        dense stack no-caps flat stretch
        class="full-width"
      />
      </div>
      <div class="text-center">
        <q-btn
          :label="$t('wishList')"
          icon="lar la-heart"
          color="dark"
          dense stack no-caps flat stretch
          class="full-width"
        />
      </div>
      <div class="text-center">
        <q-btn
          :label="$t('orders')"
          icon="las la-clipboard-list"
          color="dark"
          flat dense stack no-caps stretch
          class="full-width"
        />
      </div>
      <div class="text-center">
        <q-btn
          :label="$t('profile')"
          icon="lar la-user"
          color="dark"
          flat dense stack no-caps stretch
          class="full-width"
        />
      </div>
    </div>
  </q-card>
</div>
</template>

<script>
export default {
  name: "vipBottomNavigation"
}
</script>

<style lang="sass">
.bottom-toolbar
  position: fixed
  bottom: 5px
  left: 5px
  right: 5px
  background: #ffffff
  z-index: 10

.bottom-navigation
  display: grid
  grid-template-columns: repeat(4, 1fr)
</style>
