<template>
  <div class="InvestmentInput">

    <InputField :ID="0" :type="`Initial Investment`"  :data="inputData.initialInvestment" @dataChange="onInitInvestmentChange" :text="{title:'Initial Investment',front:'',back:''}" />

    <p>Risk</p>
    <select name="Risk" v-model="inputData.risk">
      <option disabled value="">Please select one</option>
      <option value="Low">Low</option>
      <option value="Medium">Medium</option>
      <option value="High">High</option>
    </select>

    <p>Diversification</p>
    <select name="Diversification" v-model="inputData.diversification" @change="">
      <option disabled value="">Please select one</option>
      <option value="100%">100%</option>
      <option value="75%">75%</option>
      <option value="50%">50%</option>
      <option value="25%">25%</option>
    </select>

    <div @click="onCalculate">
      <h2>Calculate</h2>
    </div>

  </div>
</template>

<script>
import InputField from "@/components/InputField";
export default {
  name: "InvestmentInput",
  components: {InputField},
  props:{
    propInputData:Object,
  },
  data(){
    return{
      inputData:{},
    }
  },
  methods:{
    onCalculate(){
      this.$emit('calculate',this.inputData)
    },
    onInitInvestmentChange(e){
      this.inputData.initialInvestment = e.data;
    }
  },
  beforeMount() {
    this.inputData = Object.assign({},this.propInputData)
  },
  emits:['calculate']
}
</script>

<style scoped lang="scss">
  .InvestmentInput{
    display: flex;
    flex-direction: column;
  }
</style>