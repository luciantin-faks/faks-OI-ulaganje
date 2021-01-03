<template>
  <div class="InvestmentItem">
    <InputField class="InputField" type="Name" :ID="itemID" :data="itemData.Name" @dataChange="onInputDataChange" />
    <InputField class="InputField" type="Growth" :ID="itemID" :data="itemData.Growth" @dataChange="onInputDataChange" />
    <InputField class="InputField" type="MaxChange" :ID="itemID" :data="itemData.MaxChange" @dataChange="onInputDataChange" />
    <div @click="$emit('deleteItem',itemID)">delete</div>
    <div @click="$emit('copyItem',itemID)">copy</div>
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

    .InputField{
      padding-left: 20px;
    }
  }
</style>