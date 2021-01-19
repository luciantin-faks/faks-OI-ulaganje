<template>
  <div class="InvestmentItem" v-bind:class="{'invested' : itemData.invested > 0 }">
    <div class="parent">
<!--      <div class="row">-->
        <InputField class="InputField div1" type="Name" :ID="itemID" :data="itemData.Name" @dataChange="onInputDataChange" :text="{title:'Ime',front:'',back:''}" />
        <InputField class="InputField div6" type="ROI" :ID="itemID" :data="itemData.ROI" @dataChange="onInputDataChange"   :text="{title:'ROI',front:'',back:'%'}"/>
<!--      </div>-->
<!--      <div class="row">-->
        <InputField class="InputField div3" type="Risk" :ID="itemID" :data="itemData.Risk" @dataChange="onInputDataChange"   :text="{title:'Rizik',front:'',back:''}"/>
        <InputField class="InputField div2" type="Min" :ID="itemID" :data="itemData.Min" @dataChange="onInputDataChange"   :text="{title:'Min',front:'',back:'%'}" />
<!--      </div>-->
<!--      <div class="row">-->
        <InputField class="InputField div5" type="Max" :ID="itemID" :data="itemData.Max" @dataChange="onInputDataChange"   :text="{title:'Max',front:'',back:'%'}" />
        <p class="investEd div4"> Ulog : {{itemData.invested}} </p>
<!--      </div>-->
    </div>
<!--    <div class="firstCol">-->
<!--      <InputField class="InputField" type="Name" :ID="itemID" :data="itemData.Name" @dataChange="onInputDataChange" :text="{title:'Name',front:'',back:''}" />-->
<!--      <InputField class="InputField" type="ROI" :ID="itemID" :data="itemData.ROI" @dataChange="onInputDataChange"   :text="{title:'ROI',front:'',back:'%'}"/>-->
<!--      <InputField class="InputField" type="Risk" :ID="itemID" :data="itemData.Risk" @dataChange="onInputDataChange"   :text="{title:'Risk',front:'',back:''}"/>-->
<!--    </div>-->
<!--    <div class="secondCol">-->
<!--      <InputField class="InputField" type="Min" :ID="itemID" :data="itemData.Min" @dataChange="onInputDataChange"   :text="{title:'Min',front:'',back:'%'}" />-->
<!--      <InputField class="InputField" type="Max" :ID="itemID" :data="itemData.Max" @dataChange="onInputDataChange"   :text="{title:'Max',front:'',back:'%'}" />-->
<!--      <div> Invested : {{itemData.invested}} </div>-->
<!--    </div>-->
    <div class="Buttons">
      <div class="DeleteItem" @click="$emit('deleteItem',itemID)">delete</div>
      <div class="CopyItem" @click="$emit('copyItem',itemID)">copy</div>
    </div>
  </div>
</template>

<script>
import InputField from "@/components/InputField";
export default {
  name: "InvestmentItem",
  components: {InputField},
  props:{
    itemID:Number,
    itemData:Object
  },
  methods:{
    onInputDataChange(e){
      // console.log(e)

      let tmp = Object.assign({},this.itemData);
      let res = e.data;

      if(e.type === 'ROI' && Number(res) < 0) return ;
      if(e.type === 'Risk' && Number(res) < 0) return ;

      if(e.type === 'Min' && Number(res) < 0) return ;
      if(e.type === 'Max' && Number(res) < 0) return ;

      if(e.type === 'Min' && Number(res) > 100) return ;
      if(e.type === 'Max' && Number(res) > 100) return ;


      if(e.type === 'Max' && Number(tmp.Min) >= Number(res)) return ;
      if(e.type === 'Min' && Number(tmp.Max) <= Number(res)) return ;


      tmp[e.type] = res;


      this.$emit('itemChange',{
        itemID:this.itemID,
        itemData:tmp
      })
    }
  },
  emits:['itemChange','deleteItem','copyItem']
}
</script>

<style scoped lang="scss">


  .InvestmentItem{
    display: flex;
    flex-direction: row;
    //margin-bottom: 10px;
    margin-right: 10px;
    flex-shrink: 0;

    //min-width: 10.5vw;

    //flex-wrap: wrap;

    background: #FFFFFF;
    box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    justify-items: center;
    justify-content: space-between;

    .InputField{
      padding-left: 0px;
    }
    .investEd{
      line-height: 0.1em;
      //background-color: inherit ;
    }

    //.flex{
    //  display: flex;
    //  flex-direction: column;
    //
    //
    //}
    //.row{
    //  display: flex;
    //  flex-direction: row;
    //  margin-left: 10px;
    //  //justify-items: start;
    //  //justify-content: space-between;
    //}

    .parent {
      margin-left: 5px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: repeat(3, 1fr);
      grid-column-gap: 5px;
      grid-row-gap: 0px;
      //align-items: start;
      //align-content: start;
      //justify-content: start;
      justify-items: start;
    }


    .div1 { grid-area: 1 / 1 / 2 / 2; }
    .div2 { grid-area: 2 / 1 / 3 / 2; }
    .div3 { grid-area: 3 / 1 / 4 / 2; }
    .div4 { grid-area: 3 / 2 / 4 / 3; }
    .div5 { grid-area: 2 / 2 / 3 / 3; }
    .div6 { grid-area: 1 / 2 / 2 / 3; }

    //.firstCol{
    //  display: flex;
    //  flex-direction: column;
    //  //justify-items: center;
    //  justify-content: space-evenly;
    //  align-items: start;
    //  padding-left: 5px;
    //  //flex-wrap: wrap;
    //  //flex-grow: 1;
    //}
    //
    //.secondCol{
    //  display: flex;
    //  flex-direction: column;
    //  justify-content: space-evenly;
    //  align-items: start;
    //
    //  //justify-content: space-evenly;
    //  //align-items: start;
    //  //text-align: start;
    //  //align-content: start;
    //}

    .Buttons{
      display: flex;
      flex-direction: column;

      padding-left: 10px;

      justify-items: center;
      justify-content: space-between;

      .DeleteItem{
        justify-self: center;
        align-self: center;
        background-color: indianred;
        width: 100%;
        padding-left: 1px;
        margin-bottom: 5px;
        user-select: none;
        cursor: pointer;
        border-radius: 0px 8px 0px 8px;
        //color: lightgray;
      }

      .CopyItem{
        justify-self: center;
        align-self: center;
        background-color: dodgerblue;
        width: 100%;
        user-select: none;
        cursor: pointer;
        border-radius: 8px 0px 8px 0px;
      }
    }

  }

  .invested{
    background-color: lightgray !important;
  }

</style>