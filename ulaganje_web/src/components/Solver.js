// var solver = require("javascript-lp-solver");
//
// function StringNumberToPercentage(num){ return String(Number(num)/100)}
// function CreateSumStringFromVars(vars){ return vars.reduce((v,c) => v+" + "+c);}
// function CArrayToLpString(arr){
//     let tmp = "";
//     arr.forEach(a=>{
//         tmp += a + "\n";
//     })
//     return tmp;
// }
//
// function SolveModel(model,inputData){
//     model.forEach((Col)=>{
//
//         let Ulog = inputData.initialInvestment
//         let Vars = [];
//         let Risk = [];
//         let Max = [];
//         let Min = [];
//         let ROI = [];
//
//
//
//
//         Col.forEach((Var)=>{
//             Vars.push(Var.Name.replace(/\s/g, ""))
//             ROI.push(StringNumberToPercentage(Var.ROI))
//             Risk.push(String(Number(Var.Risk)))
//             Min.push(StringNumberToPercentage(Var.Min))
//             Max.push(StringNumberToPercentage(Var.Max))
//         })
//
//         let VarSum = " ( " + CreateSumStringFromVars(Vars) + " ) ";
//         let f_cilj = [];
//         let c_min = [];
//         let c_max = [];
//         let c_risk = [];
//         let c_sum = " ";
//
//         Vars.forEach((c,index)=> c_risk.push(Risk[index]+" "+c));
//         c_risk = CreateSumStringFromVars(c_risk) + " <= " + String(Ulog);
//
//         Vars.forEach((c,index)=> f_cilj.push(ROI[index]+" "+c));
//         f_cilj = CreateSumStringFromVars(f_cilj);
//
//         c_sum = VarSum + " <= " + String(Ulog);
//
//         Vars.forEach((v,i)=>{
//             c_min.push(v + " <= " + VarSum + " * " + Min[i] );
//             c_max.push(v + " >= " + VarSum + " * " + Max[i] );
//         })
//
//
//         let localModel = `
//         max : ${f_cilj};
//         ${c_sum}
//         ${CArrayToLpString(c_min)}
//         ${CArrayToLpString(c_max)}
//         `
//         // console.log(solver.ReformatLP(localModel))
//         console.log(localModel)
//         console.log(solver.ReformatLP)
//         console.log(solver)
//         // console.log(f_cilj)
//         // console.log(Vars,ROI,Risk,Max,Min)
//         // console.log(VarSum,c_min,c_max,c_risk,c_sum)
//     })
//
// }
//
// export default SolveModel;