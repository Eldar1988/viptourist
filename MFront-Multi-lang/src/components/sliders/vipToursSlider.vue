<template>
<div>
  <swiper
    v-if="tours.length > 0"
    class="swiper"
    :options="swiperOptions"
  >
    <swiper-slide
      v-for="tour in tours"
      :key="tour.id"
    >
      <vip-tour-card :tour="tour"/>
    </swiper-slide>
  </swiper>

  <swiper
    v-else
    class="swiper"
    :options="swiperOptions"
  >
    <swiper-slide
      v-for="(tour, index) in 6"
      :key="index"
    >
      <vip-tour-card-skeleton />
    </swiper-slide>
  </swiper>
</div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import VipTourCardSkeleton from "components/skeletons/vipTourCardSkeleton";
import VipTourCard from "components/cards/vipTourCard";

export default {
  name: "vipToursSlider",
  components: {
    VipTourCard,
    VipTourCardSkeleton,
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  props: {
    categoryID: {
      type: Number,
      default: null
    },
    cityID: {
      type: Number,
      default: null
    }
  },
  data() {
    return {
      tours: [],
      swiperOptions: {
        spaceBetween: 15,
        freeMode: true,
        autoplay: {
          delay: 3000,
          stopOnLastSlide: false,
          disableOnInteraction: true,
        },
        // freeMode: true,
        breakpoints: {
          1600: {
            slidesPerView: 7.3,
          },
          1400: {
            slidesPerView: 6.3,
          },
          1200: {
            slidesPerView: 5.3,
          },
          1000: {
            slidesPerView: 4.3,
          },
          700: {
            slidesPerView: 3.3,
          },
          300: {
            slidesPerView: 1.6,
          }
        }
      }
    }
  },
  created() {
    setTimeout(() => {
      this.loadTours()
    }, 1100)

  },
  methods: {
    async loadTours() {
      this.tours = await this.$axios.get(`${this.$store.getters.getServerURL}/tours/tours_list/?city=${this.cityID}&category=${this.categoryID}`)
      .then(({data}) => data.results)
    }
  }
}
</script>

<style scoped>

</style>
