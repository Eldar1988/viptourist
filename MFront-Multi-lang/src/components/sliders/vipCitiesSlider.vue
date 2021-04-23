<template>
<div>
  <swiper class="swiper" :options="swiperOptions">
    <swiper-slide
      v-for="city in cities"
      :key="city.id"
    >
      <vip-city-card :city="city" />
    </swiper-slide>
  </swiper>
</div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import VipCityCard from "components/cards/vipCityCard";

export default {
  name: "vipCitiesSlider",
  props: {
    cities: {
      type: Array,
      default: null
    }
  },
  components: {
    VipCityCard,
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },

  data() {
    return {
      swiperOptions: {
        spaceBetween: 7,
        freeMode: true,
        autoplay: {
          delay: 3000,
          stopOnLastSlide: false,
          disableOnInteraction: true,
        },
        // freeMode: true,
        breakpoints: {
          700: {
            slidesPerView: 4.3,
          },
          300: {
            slidesPerView: 2.3,
          }
        }
      }
    }
  },
}
</script>

<style scoped>

</style>
