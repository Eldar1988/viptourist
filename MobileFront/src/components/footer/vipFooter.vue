<template>
<section class="q-mt-xl q-pt-lg">
  <div class="footer bg-grey-6 q-pt-lg q-px-md" style="padding-bottom: 80px">
    <vip-section-title title="Vip tourist" class="text-center text-white"/>
    <p class="text-white text-center">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum pharetra velit eget massa facilisis,
      tristique eleifend risus sodales. Phasellus maximus purus sed ante vulputate convallis.
      Sed efficitur sapien a justo dignissim, nec tincidunt lacus sagittis.
    </p>
    <div class="flex flex-center column">
    <router-link to="/" class="text-grey-4">Политика конфиденциальности</router-link>
    <router-link to="/" class="text-grey-4">Публичная оферта</router-link>
    </div>
    <div class="q-mt-lg text-center">
      <small class="text-uppercase">Vip Tourist© {{ year }}. </small><small>Все права защищены.</small>
    </div>
  </div>
</section>
</template>

<script>
import VipSectionTitle from "components/utils/vipSectionTitle";
export default {
  name: "vipFooter",
  components: {VipSectionTitle},
  computed: {
    year() {
      let date = new Date()
      return date.getFullYear()
    }
  }
}
</script>

<style lang="sass">

</style>
