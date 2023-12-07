import os
from settings import NEW_PATH
from PIL import Image
from model.model import FeatureExtractor



def FeatureSave():
    fe = FeatureExtractor()
    #feature, image_path 저장
    feature_list = []
    img_paths = []

    for img_path in os.listdir(NEW_PATH):
        img_paths.append(img_path)
        # Extract Features
        feature = fe.extract(img=Image.open(NEW_PATH+"/"+img_path))

        feature_list.append(feature)

    return feature_list, img_paths


