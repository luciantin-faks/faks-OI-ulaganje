<template>
  <div class="InputField">
    <p>{{text.title}} : </p>
    <div class="Data">
      <p class="DataText" @click="onTextClick" v-if="!showInput">{{text.front}} {{localData}} {{text.back}}</p>
      <input  class="DataInput" ref="input"  :value="localData" v-else @focusout="onFocusOutOfTextInput">
    </div>
  </div>
</template>

<script>
export default {
name: "InputField",
  props:{
    ID:Number,
    type:String,
    data:String,
    text:Object
  },
  data(){
    return{
      showInput:false,
      localData:String(this.data)
    }
  },
  methods:{
    onTextClick(){
      this.showInput = true;
    },
    onFocusOutOfTextInput(e){
      this.$emit('dataChange',{
        type:this.type,
        ID:this.ID,
        data:e.srcElement.value,
      })
      this.showInput = false;
    }
  },
  updated() {
    if(this.showInput) this.$refs.input.focus()
    this.localData = String(this.data)
  },
  emits:['dataChange']
}
</script>

<style scoped lang="scss">
  .InputField{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-content: center;
    align-items: center;
    //height: 1.1em;
    line-height: 0.1em;
    .Data{
      padding-left: 5px;
      margin: auto 0;
    }
    .DataInput{
      margin: auto 0;
      width: 4em;
    }
    //.DataInput{
    //  text-align: center;
    //  display: inline;
    //  //padding-left: 10px;
    //  //width: 4em;
    //  height: 1.1em;
    //}
  }


</style>