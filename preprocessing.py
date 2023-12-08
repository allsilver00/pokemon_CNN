import os
from PIL import Image





def preprocess(path,new_path):
       
    for filename in os.listdir(path):
        image = Image.open(path+"/"+filename)
        image = image.convert("RGBA")
        datas = image.getdata()
        
        newData = []
        cutOff = 240
        
        for item in datas:
            if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
                newData.append((255, 255, 255, 0))
                # RGB의 각 요소가 모두 cutOff 이상이면 transparent하게 바꿔줍니다.
            else:
                newData.append(item)
                # 나머지 요소는 변경하지 않습니다.
        
        image.putdata(newData)
        image.save(new_path +'/'+filename, "PNG") # PNG 포맷으로 저장합니다.