<template>
<div>
  <q-card
    class="shadow-0 bg-white"
  >
    <q-skeleton class="tour-card-image full-width" square animation="none"/>
    <div class="q-py-md q-px-sm">
      <q-skeleton height="30px" animation="none"/>
      <div class="flex q-pt-md justify-between">
        <q-skeleton height="20px" width="40%" animation="none"/>
        <q-skeleton height="20px" width="15%" animation="none"/>
      </div>
    </div>


  </q-card>
</div>
</template>

<script>
export default {
name: "vipTourCardSkeleton"
}
</script>

<style scoped>

</style>
