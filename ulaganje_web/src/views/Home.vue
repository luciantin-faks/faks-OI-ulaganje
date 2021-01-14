<template>
  <div class="home">
    <div class="TopMenu">
      <h1>Menu</h1>
      <InvestmentInput :propInputData="inputData" @calculate="onCalculate" />
    </div>
    <div class="BotItems">
      <ItemColumn v-for="(items,index) in ModelData" :items="items" :colID="index" :key="index" :colGain="ResultData[index]" @itemChange="onitemChange" @deleteItem="onDeleteItem" @addItem="onAddItem" @copyItem="onItemCopy" @deletCol="onDeleteCol" />
      <div class="AddCol" @click="onAddCol"><h2>+</h2></div>
    </div>
  </div>
</template>

<script>
import ItemColumn from "@/components/ItemColumn";
import InvestmentInput from "@/components/InvestmentInput";

export default {
  name: 'Home',
  components: {InvestmentInput, ItemColumn, },
  data(){
    return{
      connection: null,
      showResult:false,
      inputData:{
        initialInvestment:100,
        diversification:'25%',
        risk:1,
      },
      ModelData:[
        [
          {Name:'TestA',ROI:'1',Min:'0',Max:'100',Risk:0,invested:0},
          {Name:'TestB',ROI:'2',Min:'0',Max:'100',Risk:0,invested:0},
        ],
        [
          {Name:'TestC',ROI:'3',Min:'0',Max:'50',Risk:0,invested:0},
          {Name:'TestD',ROI:'4',Min:'0',Max:'50',Risk:0,invested:0},
        ],
        [
          {Name:'TestE',ROI:'5',Min:'0',Max:'100',Risk:0,invested:0},
          {Name:'TestF',ROI:'6',Min:'0',Max:'100',Risk:0,invested:0},
        ]
      ],
      ResultData:[],
    }
  },
  methods:{
    onitemChange(e){
      this.ModelData[e.colID][e.itemID] = Object.assign({}, e.itemData)
    },
    onDeleteItem(e){
      this.ModelData[e.colID].splice(e.itemID,1)
    },
    onAddItem(e){
      this.ModelData[e].push({
        Name:'New',ROI:'0',Min:'0',Max:'100',Risk:0,invested:0
      })
    },
    onAddCol(){
      this.ModelData.push([])
    },
    onDeleteCol(colId){
      this.ModelData.splice(colId,1);
      this.ResultData.splice(colId,1);
    },
    onItemCopy(e){
      console.log(this.ModelData)
      if(e.colID+1 >= this.ModelData.length ) this.ModelData.push([])
      this.ModelData[e.colID+1].push(Object.assign({},this.ModelData[e.colID][e.itemID]))
    },
    onCalculate(inputData){
      this.inputData = Object.assign({},inputData)

      let tmpModelData = Array.from(this.ModelData)
      for(let key in tmpModelData ) console.log(key)

      console.log('Sending Data...');
      let data = JSON.stringify({
        ModelData:this.ModelData,
        InputData:this.inputData
      })
      this.connection.send(data)
    },
    HandleResult(res){
      console.log(res)
      let result = JSON.parse(res.data);
      result.forEach((e,i)=>{
        let summ = 0;

        e[1].forEach((f,j)=>{
          summ = summ+f;
          this.ModelData[i][j].invested = f;
        })
        let resD = {
          gain:e[0]*-1,
          sum:(e[0]*-1 + summ).toFixed(2),
        }
        this.ResultData.splice(i,0,resD)
      })
    }
  },
  created() {
    console.log('Connecting to server...');
    this.connection = new WebSocket("ws://oi.tin.blue/calculate/:9090");
    this.connection.onmessage = this.HandleResult;
    this.connection.onopen = function(event) {
      // console.log(event)
      console.log("Successfully connected to the server...")
    }
  },
}
</script>


<style lang="scss" scoped>
  .home{
    margin-top: 20px;
    display: flex;
    flex-direction: column;

    .TopMenu{
      display: flex;
      flex-direction: column;
      width: 20vw;
      flex-grow: 1;
      align-items: center;
      align-self: center;
      background-color: #C1E0F5;
      box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
      border-radius: 5px;
    }

    .BotItems{
      display: flex;
      flex-direction: column;
      //flex-wrap: wrap;
      flex-grow: 8;
      justify-content: left;
    }

    .AddCol{
      //width: 10vw;
      width: 90%;
      height: 5vh;
      overflow-y: auto;
      align-content: center;
      margin: 10px;
      padding: 5px 20px;
      //background-color: dodgerblue;
      align-self: center;
      cursor: pointer;
      background: lightgreen;
      box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
      border-radius: 20px;
    }

  }
</style>