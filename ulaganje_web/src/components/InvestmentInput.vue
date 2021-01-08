<template>
  <div class="InvestmentInput">

    <InputField :ID="0" :type="`Initial Investment`"  :data="inputData.initialInvestment" @dataChange="onInitInvestmentChange" :text="{title:'Initial Investment',front:'',back:''}" />
    <InputField :ID="0" :type="`Risk`"  :data="inputData.risk" @dataChange="onRiskChange" :text="{title:'Risk',front:'',back:''}" />

<!--    <p>Risk</p>-->
<!--    <select name="Risk" v-model="inputData.risk">-->
<!--      <option disabled value="">Please select one</option>-->
<!--      <option value="Low">Low</option>-->
<!--      <option value="Medium">Medium</option>-->
<!--      <option value="High">High</option>-->
<!--    </select>-->

<!--    <p>Diversification</p>-->
<!--    <select name="Diversification" v-model="inputData.diversification" @change="">-->
<!--      <option disabled value="">Please select one</option>-->
<!--      <option value="100%">100%</option>-->
<!--      <option value="75%">75%</option>-->
<!--      <option value="50%">50%</option>-->
<!--      <option value="25%">25%</option>-->
<!--    </select>-->

    <div class="ClacButton" @click="onCalculate">
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
    },
    onRiskChange(e){
      this.inputData.risk = e.data;
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

    .ClacButton{
      margin: 20px 10px;
      background-color: #214D76;
      color: #FFFFFF;
      box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.25);
      border: none;
      display: inline-block;
      //margin: 0.5em 0;
      padding: 0.5em 1em;
      font-size: 1em;
      line-height: 1;
      cursor: pointer;
      &:hover{
        background-color: #214D76;
        box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
      }

      &:hover{
        background-color: #214D76;
      }

    }

  }
</style>