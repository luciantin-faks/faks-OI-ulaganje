<template>
  <div class="ItemCol">
    <h2>Year {{colID + 1}}</h2>
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
  emits:['itemChange','deleteItem','addItem','copyItem']
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

    .AddItem{
      background-color: lightblue;
      padding: 5px 0px;
      user-select: none;
      cursor: pointer;

    }

  }

</style>