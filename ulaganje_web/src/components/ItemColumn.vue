<template>
  <div class="ItemCol">
    <div class="header" >
      <h4>X</h4>
      <h2>Year {{colID + 1}}</h2>
      <h3 @click="$emit('deletCol',colID)">X</h3>
    </div>
    <InvestmentItem v-for="(item,index) in items" :itemData="item" :itemID="index" :key="index" @itemChange="onitemChange" @deleteItem="onDeleteItem" @copyItem="onItemCopy" />
    <div class="AddItem" @click="$emit('addItem',colID)">Add Item</div>
  </div>
</template>

<script>
import InvestmentItem from "@/components/InvestmentItem";
export default {
  name: "ItemColumn",
  components: {InvestmentItem},
  props:{
    items:Object,
    colID:Number
  },
  methods:{
    onitemChange(e){
      e['colID'] = this.colID;
      this.$emit('itemChange',e)
    },
    onDeleteItem(e){
      this.$emit('deleteItem',{
        itemID:e,
        colID:this.colID
      })
    },
    onItemCopy(e){
      this.$emit('copyItem',{
        itemID:e,
        colID:this.colID
      })
    }
  },
  emits:['itemChange','deleteItem','addItem','copyItem','deletCol']
}
</script>

<style scoped lang="scss">
  .ItemCol{
    display: flex;
    flex-direction: column;
    width: 10vw;
    height: 30vh;
    overflow-y: auto;
    align-content: center;
    margin: 20px;
    padding: 5px 20px;
    background-color: beige;
    box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;


    .AddItem{
      background-color: lightblue;
      padding: 5px 0px;
      user-select: none;
      cursor: pointer;
      border-radius: 10px;
      box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
    }

    .header{
      display: flex;
      flex-direction: row;
      //justify-items: center;
      align-items: center;
      //align-content: space-evenly;
      justify-content: space-between;
      h3{
        justify-self: right;
        cursor: pointer;
        color: indianred;
      }
      h4{
        visibility: hidden;
      }
    }

  }

</style>