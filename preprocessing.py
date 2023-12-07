import os
from PIL import Image
from settings import START_PATH,NEW_PATH




def preprocess():
       
    for filename in os.listdir(START_PATH):
        image = Image.open(START_PATH+"/"+filename)
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
        image.save(NEW_PATH +'/'+filename, "PNG") # PNG 포맷으로 저장합니다.