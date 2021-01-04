<template>
  <div class="home">
    <div class="LeftMenu">
      <h1>Menu</h1>
      <InvestmentInput :propInputData="inputData" @calculate="onCalculate" />
    </div>
    <div class="RightCol">
      <ItemColumn v-for="(items,index) in ModelData" :items="items" :colID="index" :key="index" @itemChange="onitemChange" @deleteItem="onDeleteItem" @addItem="onAddItem" @copyItem="onItemCopy" />
      <div class="AddCol" @click="onAddCol"><p>Add Col</p></div>
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
      inputData:{
        initialInvestment:100,
        diversification:'25%',
        risk:'Low',
      },
      ModelData:[
        [
          {Name:'TestA',ROI:'1',Min:'0',Max:'100',Risk:0},
          {Name:'TestB',ROI:'2',Min:'0',Max:'100',Risk:0},
        ],
        [
          {Name:'TestC',ROI:'3',Min:'0',Max:'100',Risk:0},
          {Name:'TestD',ROI:'4',Min:'0',Max:'100',Risk:0},
        ],
        [
          {Name:'TestE',ROI:'5',Min:'0',Max:'100',Risk:0},
          {Name:'TestF',ROI:'6',Min:'0',Max:'100',Risk:0},
        ]
      ]
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
        Name:'New',ROI:'0',Min:'0',Max:'100',Risk:0
      })
    },
    onAddCol(){
      this.ModelData.push([])
    },
    onItemCopy(e){
      console.log(this.ModelData)
      if(e.colID+1 >= this.ModelData.length ) this.ModelData.push([])
      this.ModelData[e.colID+1].push(Object.assign({},this.ModelData[e.colID][e.itemID]))
    },
    onCalculate(inputData){
      this.inputData = Object.assign({},inputData)
      console.log('Sending Data...');
      this.connection.send(JSON.stringify({
        ModelData:this.ModelData,
        InputData:this.inputData
      }))
    }
  },
  created() {
    console.log('Connecting to server...');
    this.connection = new WebSocket("ws://oi.tin.blue/calculate/:9090");
    this.connection.onmessage = function(event) {
      console.log('New Message....')
      console.log(event);
    }
    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the server...")
    }
  }
}
</script>
<!--

 let a = new WebSocket("ws://oi.tin.blue/calculate/:9090");
a.onmessage = function(e){console.log(e)}
 a.onopen = function(event) {
console.log(event)
console.log("Successfully connected to the server...")
}

-->
<style lang="scss" scoped>
  .home{
    display: flex;
    flex-direction: column;

    .LeftMenu{
      display: flex;
      flex-direction: column;
      //width: 20vw;
      flex-grow: 1;
    }

    .RightCol{
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      //width: 80vw;
      flex-grow: 8;
      justify-content: left;
    }

    .AddCol{
      width: 10vw;
      height: 30vh;
      overflow-y: auto;
      align-content: center;
      margin: 20px;
      padding: 5px 20px;
      background-color: dodgerblue;
      align-self: center;
    }

  }
</style>