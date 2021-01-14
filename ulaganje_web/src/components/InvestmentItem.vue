<template>
  <div class="InvestmentItem" v-bind:class="{'invested' : itemData.invested > 0 }">
    <div class="firstCol">
      <InputField class="InputField" type="Name" :ID="itemID" :data="itemData.Name" @dataChange="onInputDataChange" :text="{title:'Name',front:'',back:''}" />
      <InputField class="InputField" type="ROI" :ID="itemID" :data="itemData.ROI" @dataChange="onInputDataChange"   :text="{title:'ROI',front:'',back:'%'}"/>
      <InputField class="InputField" type="Risk" :ID="itemID" :data="itemData.Risk" @dataChange="onInputDataChange"   :text="{title:'Risk',front:'',back:''}"/>
    </div>
    <div class="secondCol">
      <InputField class="InputField" type="Min" :ID="itemID" :data="itemData.Min" @dataChange="onInputDataChange"   :text="{title:'Min',front:'',back:'%'}" />
      <InputField class="InputField" type="Max" :ID="itemID" :data="itemData.Max" @dataChange="onInputDataChange"   :text="{title:'Max',front:'',back:'%'}" />
      <div> <p>Invested : {{itemData.invested}}</p> </div>
    </div>
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

      if(e.type === 'ROI' && res < 0) return ;
      if(e.type === 'Risk' && res < 0) return ;

      if(e.type === 'Min' && res < 0) return ;
      if(e.type === 'Max' && res < 0) return ;

      if(e.type === 'Min' && res > 100) return ;
      if(e.type === 'Max' && res > 100) return ;

      if(e.type === 'Max' && tmp.Min >= res) return ;
      if(e.type === 'Min' && tmp.Max <= res) return ;

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

    min-width: 12vw;

    //flex-wrap: wrap;

    background: #FFFFFF;
    box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    justify-items: center;
    justify-content: space-between;

    .InputField{
      padding-left: 20px;
    }

    .firstCol{
      display: flex;
      flex-direction: column;
      justify-items: center;
      justify-content: space-evenly;
      align-items: start;
    }

    .secondCol{
      display: flex;
      flex-direction: column;
      justify-content: space-evenly;
      align-items: start;
      text-align: start;
      align-content: start;
    }

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