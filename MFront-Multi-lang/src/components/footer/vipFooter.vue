<template>
<section class="q-mt-xl q-pt-lg">
  <div class="footer bg-grey-7 q-pt-lg q-px-md" style="padding-bottom: 80px">
    <vip-section-title title="Vip tourist" class="text-center text-white text-uppercase text-bold"/>
    <small class="text-white text-center block q-mt-md">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum pharetra velit eget massa facilisis,
      tristique eleifend risus sodales. Phasellus maximus purus sed ante vulputate convallis.
      Sed efficitur sapien a justo dignissim, nec tincidunt lacus sagittis.
    </small>
    <div class="flex flex-center column q-mt-lg">
    <router-link to="/" class="text-grey-4"><small>{{ $t('privacyPolicy') }}</small></router-link>
    <router-link to="/" class="text-grey-4"><small>{{ $t('publicOffer') }}</small></router-link>
    </div>
    <div class="q-mt-lg text-center text-grey-4">
      <small class="text-uppercase ">Vip Tourist© {{ year }}. </small><small>{{ $t('allRightReserved') }}.</small>
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
