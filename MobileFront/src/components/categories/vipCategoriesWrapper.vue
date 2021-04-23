<template>
<div>
  <div
    v-for="category in categories"
    :key="category.id"
  >
    <div class="q-ml-md">
    <vip-section-title :title="category.title"/>
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
