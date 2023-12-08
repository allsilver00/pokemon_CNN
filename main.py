

from model.feature import FeatureSave 
import settings
from data.preprocessing import preprocess
from data.result import visualize



if __name__=="__main__":

    start_path = settings.START_PATH
    new_path = settings.NEW_PATH


    # 이미지 데이터 전처리 배경 삭제
    preprocess(start_path,new_path)

    # 
    feature_list, img_paths = FeatureSave()

    # 유사도 찾을 이미지 파일 이름
    name = 'pikachu.png'


    # 결과 시각화

    visualize(name,feature_list,img_paths)
    

