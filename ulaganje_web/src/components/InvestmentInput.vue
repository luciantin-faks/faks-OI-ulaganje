<template>
  <div class="InvestmentInput">

    <InputField :ID="0" :type="`Input`" :data="1000" />

    <select name="Risk">
      <option value="Low">Low</option>
      <option value="Medium">Medium</option>
      <option value="High">High</option>
    </select>


    <select name="Diversification">
      <option value="None">100%</option>
      <option value="High">75%</option>
      <option value="Medium">50%</option>
      <option value="Low">25%</option>
    </select>

  </div>
</template>

<script>
import InputField from "@/components/InputField";
export default {
name: "InvestmentInput",
  components: {InputField}
}
</script>

<style scoped>

</style>