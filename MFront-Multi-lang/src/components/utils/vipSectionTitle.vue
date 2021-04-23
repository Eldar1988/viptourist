<template>
<div>
  <h2 class="section-title">{{ title }}</h2>
</div>
</template>

<script>
export default {
  name: "vipSectionTitle",
  props: {
    title: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="sass">
.section-title
  font-size: 20px
  font-weight: 500
</style>
