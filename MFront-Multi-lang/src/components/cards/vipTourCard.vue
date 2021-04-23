<template>
  <div>
    <q-card
      v-if="tour"
      class="shadow-0 overflow-hidden"
    >
      <router-link :to="`/tours/tour/${tour.id}`">
        <q-img
          :src="tour.image"
          class="tour-card-image"
        >
          <template v-slot:loading>
            <q-skeleton class="tour-card-image full-width" square/>
          </template>
          <!--      Rating   -->
          <div v-if="rating" style="background: inherit !important">
            <q-rating
              v-model="rating"
              :max="5"
              icon="star_border"
              icon-selected="star"
              icon-half="star_half"
              class="q-ma-sm"
            />
          </div>
          <!--      /// Rating   -->
          <!--      Comments   -->
          <q-btn
            :label="tour.reviews_count"
            color="primary"
            class="q-pa-sm"
            icon="las la-comment"
            size="xs"
            dense padding="0" unelevated
            style="position: absolute; right: 5px; top: 5px; padding: 5px"
          />
          <!--      /// Comments   -->
        </q-img>
      </router-link>
      <!--    Title & Price   -->
      <div class="q-py-md q-px-sm">
        <div class="" style="height: 55px">
          <router-link :to="`/tours/tour/${tour.id}`">
            <p class="cards-title ellipsis-2-lines text-dark text-bold">{{ tour.title }}</p>
          </router-link>
        </div>
        <div class="flex justify-between">
          <div>
            <p class="q-pt-sm">
              {{ $t('priceFrom') }}
              <span class="price">{{ tour.offers_minimal_price }}
                <q-icon class="price-icon" name="mdi-currency-usd"/>
              </span>

            </p>
          </div>
          <div>
            <vip-wish-list-icon/>
          </div>
        </div>
      </div>
      <!--    /// Title & Price   -->
    </q-card>
  </div>
</template>

<script>
import VipWishListIcon from "components/wishList/vipWishListIcon";

export default {
  name: "vipTourCard",
  components: {VipWishListIcon},
  props: {
    tour: {
      type: Object,
      default: null
    }
  },
  computed: {
    rating() {
      return +this.tour.rating || null
      // return Math.round(this.tour.rating) || null
    }
  },
  data() {
    return {}
  },
}
</script>

<style lang="">

</style>
