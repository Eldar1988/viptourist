<template>
<div>
  <q-card
    class="shadow-0"
  >
    <q-img
      :src="city.image"
      class="city-card-image"
    >
      <template v-slot:loading>
        <q-skeleton class="full-width city-card-image" animation="none"/>
      </template>
      <div class="city-text flex flex-center">
        <p class="city-card-title">{{ city.title }}</p>
      </div>
    </q-img>
  </q-card>
</div>
</template>

<script>
export default {
  name: "vipCityCard",
  props: {
    city: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.city-text
  position: absolute
  top: 0
  left: 0
  right: 0
  bottom: 0
  background: rgba(0,0,0,.4) !important

.city-card-image
  height: 150px

.city-card-title
  font-size: 16px
</style>
