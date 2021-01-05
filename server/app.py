import numpy as np
from scipy.optimize import minimize
import sys
import json

jsan = sys.argv[1]
#print(jsan)
#jsan = "{\"ModelData\":[[{\"Name\":\"TestA\",\"ROI\":\"1\",\"Min\":\"0\",\"Max\":\"100\",\"Risk\":0},{\"Name\":\"TestB\",\"ROI\":\"2\",\"Min\":\"0\",\"Max\":\"100\",\"Risk\":0}],[{\"Name\":\"TestC\",\"ROI\":\"3\",\"Min\":\"0\",\"Max\":\"100\",\"Risk\":0},{\"Name\":\"TestD\",\"ROI\":\"4\",\"Min\":\"0\",\"Max\":\"100\",\"Risk\":0}],[{\"Name\":\"TestE\",\"ROI\":\"5\",\"Min\":\"0\",\"Max\":\"100\",\"Risk\":0},{\"Name\":\"TestF\",\"ROI\":\"6\",\"Min\":\"0\",\"Max\":\"100\",\"Risk\":0}]],\"InputData\":{\"initialInvestment\":100,\"diversification\":\"25%\",\"risk\":\"Low\"}}\n"
# print(json.loads(jsan))
Data = json.loads(jsan)


##########################################################################################################
##########################################################################################################
##########################################################################################################


def PrepareData(Col):
    tmp = {}
    tmp['Name']=[]
    tmp['Risk']=[]
    tmp['ROI']=[]
    tmp['Min']=[]
    tmp['Max']=[]
    for i in Col:
        tmp['Name'].append(i['Name'])
        tmp['Risk'].append(np.array(i['Risk']).astype(np.float))
        tmp['ROI'].append(np.array(i['ROI']).astype(np.float))
        tmp['Min'].append(np.array(i['Min']).astype(np.float))
        tmp['Max'].append(np.array(i['Max']).astype(np.float))
    return tmp


##########################################################################################################
##########################################################################################################
##########################################################################################################


def SolveCol(Col,max_risk,pocetni_ulog):
    stavke = Col['Name']
    length = len(stavke)

    Risk = Col['Risk']
    Min = Col['Min']
    Max = Col['Max']
    ROI = Col['ROI']

    def objective(x):
        obj = 0
        for i in range(length):
            obj = obj - ROI[i]*x[i]
        return obj

    def c_min_maker(target_index):
        def c_min(x):
            summ = 0
            for i in range(length):
                summ = summ + x[i]
            summ = x[target_index]/summ - Min[target_index]
            return summ
        return c_min

    def c_max_maker(target_index):
        def c_max(x):
            summ = 0
            for i in range(length):
                summ = summ + x[i]
            summ = Max[target_index] - x[target_index]/summ
            return summ
        return c_max

    def c_risk(x):
        summ = 0
        tmp_sum = 0
        for i in range(length):
            tmp_sum = tmp_sum + x[i]
        for i in range(length):
            summ = summ + ((x[i]/tmp_sum) * Risk[i])
        summ = max_risk - summ
        return summ

    def c_sum(x):
        summ = 0
        for i in range(length):
            summ = summ - x[i]
        summ = summ + pocetni_ulog
        return summ

    x0 = []
    bounds = []

    for i, x in enumerate(stavke):
        bounds.append((0,pocetni_ulog))
        x0.append(1)

    bnds = tuple(bounds)

    con_sum = {'type': 'ineq', 'fun': c_sum}
    con_risk = {'type': 'ineq', 'fun': c_risk}
    cons = [con_sum,con_risk]

    for i in range(length):
        cons.append(dict(type= 'ineq',fun= c_min_maker(i)))
        cons.append(dict(type= 'ineq',fun= c_max_maker(i)))


    sol = minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)
    return sol

##########################################################################################################
##########################################################################################################
##########################################################################################################

prepared_model_data = []
ReturnData = []

for i in Data['ModelData']:
    prepared_model_data.append(PrepareData(i))


user_pocetni_ulog = float(Data['InputData']['initialInvestment'])
user_max_risk = 1

for i in prepared_model_data:
    tmp = SolveCol(i,user_max_risk,user_pocetni_ulog)
    tmpData = []
    rez = round( tmp.fun ,2)
    val = []
    for x in tmp.x:
        val.append(round( x ,2))
    ReturnData.append([rez,val])
    user_pocetni_ulog = tmp.fun * -1

print(json.dumps(ReturnData))




#import sys
#print('#Hello from python#')
#print('First param:'+sys.argv[1]+'#')
#print('Second param:'+sys.argv[2]+'#')
#import json
#with open('countries.json') as json_data:
# for entry in json_data:
#  print(entry)

#import sys
#for i in range(1,10):
#   print(i)
#print('#Hello from python#')
#print(sys.argv[1])
