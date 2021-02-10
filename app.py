import json
import datetime
import time
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/")
def read(key='time'):

    with open('db.json', 'r') as r:
        data = json.load(r)
    A_A_cnt = A_B_cnt = B_A_cnt = B_B_cnt = C_A_cnt = C_B_cnt = 0

    for i in range(len(data)):
        if(data[i][key] >= "2021-01-28 07:30:00" and data[i][key] < "2021-01-28 13:30:00"):

            if(int(data[i][key][11:13]) >= 6 and int(data[i][key][11:13]) < 14):
                if (data[i]['production_A'] == True):
                    A_A_cnt = A_A_cnt+1
                else:
                    A_B_cnt = A_B_cnt+1

            if(int(data[i][key][11:13]) >= 14 and int(data[i][key][11:13]) < 20):
                if (data[i]['production_A'] == True):
                    B_A_cnt = B_A_cnt+1
                else:
                    B_B_cnt = B_B_cnt+1
            if((int(data[i][key][11:13]) >= 20 and int(data[i][key][11:13]) < 24) or (int(data[i][key][11:13]) >= 0 and int(data[i][key][11:13]) < 6)):
                if (data[i]['production_A'] == True):
                    C_A_cnt = C_A_cnt+1
                else:
                    C_B_cnt = C_B_cnt+1

            # if(data[i][key].time() > "06:00:00" and data[i][key].time() <= "14:00:00"):
                #Acnt +=1
    dict1 = {"shiftA": {"production_A_count": A_A_cnt, "production_B_count": A_B_cnt},
             "shiftB": {"production_A_count": B_A_cnt, "production_B_count": B_B_cnt},
             "shiftC": {"production_A_count": C_A_cnt, "production_B_count": C_B_cnt}
             }
    return jsonify(dict1)
