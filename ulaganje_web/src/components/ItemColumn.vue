<template>
  <div class="ItemCol">
    <InvestmentItem v-for="(item,index) in items" :itemData="item" :itemID="index" :key="index" @itemChange="onitemChange" @deleteItem="onDeleteItem" />
    <div @click="$emit('addItem',colID)">Add Item</div>
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
    }
  },
  emits:['itemChange','deleteItem','addItem']
}
</script>

<style scoped>
  .ItemCol{
    display: flex;
    flex-direction: column;
  }

</style>