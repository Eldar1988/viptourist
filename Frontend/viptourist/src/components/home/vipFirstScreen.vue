<template>
<section>
  <div class="home-first-screen-bg">
    <div class="home-title-and-search-wrapper">
      <div class="flex flex-center column" style="height: 100%">
        <h1 class="page-title text-white text-bold text-center q-px-sm">
          Планируйте<br> незабываемый отдых <br>по всему миру
        </h1>
        <q-btn
          label="Выбрать направление"
          color="primary"
          class="rounded-5 text-bold q-mt-md q-px-md"
          no-caps unelevated
        />
      </div>

    </div>
    <q-carousel
      animated
      v-model="slide"
      infinite
      :autoplay="true"
      class="home-slider"
    >
      <q-carousel-slide
        v-for="(slide, index) in slides"
        :key="index"
        :name="index"
        :img-src="slide.image"
      />
    </q-carousel>
  </div>
</section>
</template>

<script>
export default {
name: "vipFirstScreen",
  computed: {
    slides() {
      return this.$store.getters.getHomeSlides
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
.home-first-screen-bg
  position: relative
  &:after
    content: ''
    position: absolute
    top: 0
    left: 0
    right: 0
    bottom: 0
    height: 100%
    width: 100%
    background: rgba(0,0,0,.5)

.home-title-and-search-wrapper
  position: absolute
  top: 0
  left: 0
  right: 0
  bottom: 0
  z-index: 10

.home-slider
  height: 60vh

@media screen and (max-width: 650px)
  .home-slider
    height: 50vh
</style>
