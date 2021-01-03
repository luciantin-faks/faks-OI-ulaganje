<template>
  <div class="home">
    <div class="LeftMenu">
      <h1>Menu</h1>
      <InvestmentInput />
    </div>
    <div class="RightCol">
      <ItemColumn v-for="(items,index) in ModelData" :items="items" :colID="index" :key="index" @itemChange="onitemChange" @deleteItem="onDeleteItem" @addItem="onAddItem" @copyItem="onItemCopy" />
      <p @click="onAddCol">Add Col</p>
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
      inputData:{
        pocetniUlog:0,
        diverzifikacija:0,
        rizik:0,
      },
      ModelData:[
        [
          {Name:'Testset',Growth:'1',MaxChange:'5'},
          {Name:'Testset',Growth:'2',MaxChange:'5'},
        ],
        [
          {Name:'Testset',Growth:'3',MaxChange:'5'},
          {Name:'Testset',Growth:'4',MaxChange:'5'},
        ],
        [
          {Name:'Testset',Growth:'5',MaxChange:'5'},
          {Name:'Testset',Growth:'6',MaxChange:'5'},
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
        Name:'New',Growth:'0',MaxChange:'0'
      })
    },
    onAddCol(){
      this.ModelData.push([])
    },
    onItemCopy(e){
      console.log(this.ModelData)
      if(e.colID+1 >= this.ModelData.length ) this.ModelData.push([])
      this.ModelData[e.colID+1].push(Object.assign({},this.ModelData[e.colID][e.itemID]))
    }
  },
}
</script>

<style lang="scss" scoped>
  .home{
    display: flex;
    flex-direction: row;

    .LeftMenu{
      display: flex;
      flex-direction: column;
      //width: 20vw;
      flex-grow: 2;
      min-width: 20vw;
    }

    .RightCol{
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      //width: 80vw;
      flex-grow: 8;
      justify-content: left;
      min-width: 80vw;
    }

  }
</style>