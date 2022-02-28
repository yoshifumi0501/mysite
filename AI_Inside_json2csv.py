#!/usr/bin/env python
# coding: utf-8

# In[14]:


import json
import pandas as pd
from datetime import datetime

json_path = input("JSONファイルを指定してください")
new_dir_path_recursive = input("保存先フォルダを指定してください")

json_open = open(json_path, 'r')
json_load = json.load(json_open)

cols = ['text','x','y','x+w','y+h', 'page']
df = pd.DataFrame(index=[], columns=cols)

for j in range(0, len(json_load["results"][0]["pages"])):
    page = json_load["results"][0]["pages"][j]["pageNum"]
    

    for i in range(0,len(json_load["results"][0]["pages"][j]["ocrResults"])):
        txt = json_load["results"][0]["pages"][j]["ocrResults"][i]["text"]
        x = json_load["results"][0]["pages"][j]["ocrResults"][i]["bbox"]["left"]
        xw = json_load["results"][0]["pages"][j]["ocrResults"][i]["bbox"]["right"]
        y = json_load["results"][0]["pages"][j]["ocrResults"][i]["bbox"]["top"]
        yh = json_load["results"][0]["pages"][j]["ocrResults"][i]["bbox"]["bottom"]
        record = pd.Series([txt,x,y,xw,yh,page], index=df.columns)
        df = df.append(record, ignore_index=True)

print("レコード数：" + str(len(df)))

today = datetime.today()
new_csvname = '{0}/json2csv_{1:%Y%m%d%H%M}.csv'.format(new_dir_path_recursive,today)
df.to_csv(new_csvname, encoding='cp932', header=True, index=False)

