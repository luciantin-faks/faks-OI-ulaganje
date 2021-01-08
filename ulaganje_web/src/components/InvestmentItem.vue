<template>
  <div class="InvestmentItem">
    <InputField class="InputField" type="Name" :ID="itemID" :data="itemData.Name" @dataChange="onInputDataChange" :text="{title:'Name',front:'',back:''}" />
    <InputField class="InputField" type="ROI" :ID="itemID" :data="itemData.ROI" @dataChange="onInputDataChange"   :text="{title:'ROI',front:'',back:'%'}"/>
    <InputField class="InputField" type="Risk" :ID="itemID" :data="itemData.Risk" @dataChange="onInputDataChange"   :text="{title:'Risk',front:'',back:''}"/>
    <InputField class="InputField" type="Min" :ID="itemID" :data="itemData.Min" @dataChange="onInputDataChange"   :text="{title:'Min',front:'',back:'%'}" />
    <InputField class="InputField" type="Max" :ID="itemID" :data="itemData.Max" @dataChange="onInputDataChange"   :text="{title:'Max',front:'',back:'%'}" />
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
      tmp[e.type] = e.data;

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
    margin-bottom: 10px;
    //justify-items: center;
    justify-content: space-evenly;
    flex-wrap: wrap;

    background: #FFFFFF;
    box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    .InputField{
      padding-left: 20px;
    }

    .Buttons{
      display: flex;
      flex-direction: column;

      .DeleteItem{
        justify-self: center;
        align-self: center;
        background-color: indianred;
        width: 100%;
        margin-bottom: 5px;
        user-select: none;
        cursor: pointer;
        border-radius: 8px;
      }

      .CopyItem{
        justify-self: center;
        align-self: center;
        background-color: dodgerblue;
        width: 100%;
        user-select: none;
        cursor: pointer;
        border-radius: 8px;
      }
    }

  }
</style>