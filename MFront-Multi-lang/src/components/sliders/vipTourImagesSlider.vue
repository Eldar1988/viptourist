<template>
<div>
  <q-carousel
    swipeable
    animated
    v-model="slide"
    thumbnails
    infinite
    :autoplay="true"
    class="tour-images-slider"
  >
    <q-carousel-slide
      v-for="(image, index) in images"
      :key="index"
      :name="index"
      :img-src="image.image"
    />
  </q-carousel>
</div>
</template>

<script>
export default {
  name: "vipTourImagesSlider",
  props: {
    images: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      slide: 0
    }
  },
}
</script>

<style lang="sass">
.tour-images-slider
  height: 300px
</style>
