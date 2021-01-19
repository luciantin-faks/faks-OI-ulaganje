<template>
  <div class="ItemCol">
    <div class="header" >
      <div class="firstRow">
        <h3 class="deleteD" @click="$emit('deletCol',colID)">X</h3>
        <h2 class="title">Period {{colID + 1}}</h2>
<!--        <h4 class="deleteCol">X</h4>-->
      </div>
<!--      <div class="secondRow">-->
      <div class="res">
        <p v-if="colGain!=undefined">Dobit : {{colGain.gain}} </p>
        <p v-if="colGain!=undefined">Suma : {{colGain.sum}} </p>
      </div>
<!--      </div>-->
    </div>
    <div class="items">
      <InvestmentItem v-for="(item,index) in items" :itemData="item" :itemID="index" :key="index" @itemChange="onitemChange" @deleteItem="onDeleteItem" @copyItem="onItemCopy" />
      <div class="AddItem" @click="$emit('addItem',colID)"><h2>+</h2></div>
    </div>
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

  .ItemCol {

    display: flex;
    flex-direction: row;
    margin: 0px 0px 10px 0px;
    //background-color: beige;
    min-height: 125px;
    //box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
    //border-radius: 20px;

    .AddItem{
          background-color: lightblue;
          padding: 0px 5px;
          margin: 0px 5px;
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
      width: 140px;
      flex-shrink: 0;
      margin: 0px 5px;
      border-radius: 10px 0px 0px 10px;

      //justify-content: start;
      //justify-items: top;



      align-items: center;
      background-color: beige;

      h3{
          justify-self: right;
          cursor: pointer;
          color: indianred;
          user-select: none;
          margin-right: 15px;
        }

      .firstRow{
        display: flex;
        flex-direction: row;
        line-height: 0.1em;
        justify-content: space-between;
      }

      .res{
        display: flex;
        flex-direction: column;
        justify-content: center;
        line-height: 0.1em;

      }

    }

    .items{
      display: flex;
      //flex: 1 0 10.5vw;
      flex-direction: row;
      overflow-x: scroll;
      padding: 1%;
      width: 100%;
      background-color: beige;
      //box-shadow: inset 5px 5px 4px rgba(0, 0, 0, 0.25);
      //border-radius: 10px;
      scrollbar-width: thin;
    }

  }

  //.ItemCol{
  //  display: flex;
  //  flex-direction: row;
  //  //width: 10vw;
  //  //height: 12vh;
  //  //overflow-y: auto;
  //  //overflow-x: hidden;
  //  align-content: center;
  //  margin: 10px;
  //  padding: 5px 20px;
  //  //background-color: beige;
  //  //box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
  //  //border-radius: 20px;
  //  min-height: 171px;
  //
  //
  //  .AddItem{
  //    background-color: lightblue;
  //    padding: 0px 5px;
  //    margin: 0px 10px;
  //    user-select: none;
  //    cursor: pointer;
  //    border-radius: 10px;
  //    box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
  //    display: flex;
  //    flex-direction: row;
  //    align-items: center;
  //  }
  //
  //  .header{
  //    background-color: beige;
  //    display: flex;
  //    flex-direction: column;
  //    justify-content: space-evenly;
  //    //min-width: 6vw;
  //
  //    .firstRow{
  //      display: flex;
  //      flex-direction: row;
  //      //justify-items: center;
  //      align-items: center;
  //      //align-content: space-evenly;
  //      justify-content: space-between;
  //      .title{
  //        margin: 0px 10px;
  //      }
  //
  //      h3{
  //        justify-self: right;
  //        cursor: pointer;
  //        color: indianred;
  //      }
  //      h4{
  //        visibility: hidden;
  //      }
  //    }
  //    .secondRow{
  //      display: flex;
  //      flex-direction: column;
  //      //justify-content: start;
  //      justify-content: center;
  //      //justify-content: space-evenly;
  //
  //    }
  //  }
  //
  //  .items{
  //    display: flex;
  //    flex-direction: row;
  //    align-content: center;
  //    overflow-x: auto;
  //    margin: 5px 10px;
  //    //min-width: 175px;
  //    //max-width: 175px;
  //  }

  //}

</style>