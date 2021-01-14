<template>
  <div class="ItemCol">
    <div class="header" >
      <div class="firstRow">
        <h3 @click="$emit('deletCol',colID)">X</h3>
        <h2 class="title">Period {{colID + 1}}</h2>
        <h4 class="deleteCol">X</h4>
      </div>
      <div class="secondRow">
        <p v-if="colGain!=undefined">Gain : {{colGain.gain}} </p>
        <p v-if="colGain!=undefined">Sum : {{colGain.sum}} </p>
      </div>
    </div>
    <InvestmentItem v-for="(item,index) in items" :itemData="item" :itemID="index" :key="index" @itemChange="onitemChange" @deleteItem="onDeleteItem" @copyItem="onItemCopy" />
    <div class="AddItem" @click="$emit('addItem',colID)"><h2>+</h2></div>
  </div>
</template>

<script>
import InvestmentItem from "@/components/InvestmentItem";
export default {
  name: "ItemColumn",
  components: {InvestmentItem},
  props:{
    items:Object,
    colID:Number,
    colGain:String,
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
    flex-direction: row;
    //width: 10vw;
    height: 10vh;
    overflow-y: auto;
    overflow-x: hidden;
    align-content: center;
    margin: 20px;
    padding: 5px 20px;
    background-color: beige;
    box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;


    .AddItem{
      background-color: lightblue;
      padding: 0px 5px;
      user-select: none;
      cursor: pointer;
      border-radius: 10px;
      box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
      display: flex;
      flex-direction: row;
      align-items: center;
    }

    .header{
      display: flex;
      flex-direction: column;
      justify-content: space-evenly;

      .firstRow{
        display: flex;
        flex-direction: row;
        //justify-items: center;
        align-items: center;
        //align-content: space-evenly;
        justify-content: space-between;
        .title{
          margin: 0px 10px;
        }

        h3{
          justify-self: right;
          cursor: pointer;
          color: indianred;
        }
        h4{
          visibility: hidden;
        }
      }
      .secondRow{
        display: flex;
        flex-direction: column;
        //justify-content: start;
        //justify-content: space-evenly;

      }
    }

  }

</style>