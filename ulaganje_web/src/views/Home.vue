<template>
  <div class="home">
    <ItemColumn v-for="(items,index) in ModelData" :items="items" :colID="index" :key="index" @itemChange="onitemChange" @deleteItem="onDeleteItem" @addItem="onAddItem" />
    <p @click="onAddCol">Add Col</p>
  </div>
</template>

<script>
import ItemColumn from "@/components/ItemColumn";

export default {
  name: 'Home',
  components: { ItemColumn, },
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
      console.log(e)
      console.log(this.ModelData)
      this.ModelData[e.colID].splice(e.itemID,1)
    },
    onAddItem(e){
      this.ModelData[e].push({
        Name:'New',Growth:'0',MaxChange:'0'
      })
    },
    onAddCol(){
      this.ModelData.push([])
    }
  }
}
</script>

<style lang="scss" scoped>
  .home{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
</style>