<template>
  <div>
    <div
      v-for="category in categories"
      :key="category.id"
    >
      <div class="q-ml-md q-mt-lg">
        <div class="flex justify-between" style="align-items: center">
          <vip-section-title :title="category.title"/>
<!--          <p class="q-mr-md text-accent">{{ $t('showAll') }} <q-icon name="las la-angle-double-right"/></p>-->
        </div>
        <vip-tours-slider :category-i-d="category.id" :city-i-d="cityID"/>
      </div>
    </div>
  </div>
</template>

<script>
import VipSectionTitle from "components/utils/vipSectionTitle";
import VipToursSlider from "components/sliders/vipToursSlider";

export default {
  name: "vipCategoriesWrapper",
  components: {VipToursSlider, VipSectionTitle},
  created() {
    this.$store.dispatch('loadCategoriesByCity', this.$route.params.id)
  },
  computed: {
    categories() {
      return this.$store.getters.getCategories
    },
    cityID() {
      return Number(this.$route.params.id)
    }
  }
}
</script>

<style scoped>

</style>
