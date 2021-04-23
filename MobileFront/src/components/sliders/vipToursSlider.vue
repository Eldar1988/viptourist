<template>
<div>
  {{ tours }}
</div>
</template>

<script>
export default {
  name: "vipToursSlider",
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
      tours: []
    }
  },
  created() {
    this.loadTours()
  },
  methods: {
    async loadTours() {
      this.tours = await this.$axios.get(`${this.$store.getters.getServerURL}/tours/tours_list/?city=${this.cityID}&category=${this.categoryID}`)
      .then(({data}) => data)
    }
  }
}
</script>

<style scoped>

</style>
