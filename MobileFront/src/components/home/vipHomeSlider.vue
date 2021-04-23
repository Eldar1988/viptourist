<template>
  <div>
    <q-carousel
      animated
      v-model="slide"
      :autoplay="true"
      class="home-slider"
      infinite
    >
      <q-carousel-slide
        v-for="(slide, index) in slides"
        :key="index"
        :name="index"
        :img-src="slide.image"
      >
        <div class="flex flex-center q-px-sm" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0">
          <h1 class="text-h1 text-bold text-white">{{ slide.title }}</h1>
        </div>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
import notifier from "src/utils/notifier"

export default {
  name: "vipHomeSlider",
  data() {
    return {
      slides: [],
      slide: 0
    }
  },
  created() {
    this.loadSlides()
  },
  methods: {
    async loadSlides() {
      try {
        this.slides = await this.$axios.get(`${this.$store.getters.getServerURL}/main/home_slides/`).then(({data}) => data)
      }
      catch (e) {
        notifier(e.message)
        setTimeout(() => {
          location.reload()
        }, 4000)
      }

    }
  }
}
</script>

<style lang="sass">
.home-slider
  height: 400px

@media screen and (max-width: 650px)
  .home-slider
    height: 300px
</style>
