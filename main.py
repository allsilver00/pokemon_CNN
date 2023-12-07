
from PIL import Image
import numpy as np
from model.feature import FeatureSave 
import matplotlib.pyplot as plt
from model.model import FeatureExtractor
from settings import NEW_PATH



feature_list, img_paths = FeatureSave()
fe = FeatureExtractor()

image_name = NEW_PATH+'/avalugg.png'


# Insert the image query
img = Image.open(image_name)
# Extract its features
query = fe.extract(img)
# Calculate the similarity (distance) between images
dists = np.linalg.norm(feature_list - query, axis=1)
# Extract 30 images that have lowest distance
ids = np.argsort(dists)[:30]
scores = [(dists[id], img_paths[id]) for id in ids]
# Visualize the result
axes=[]
fig=plt.figure(figsize=(8,8))
for a in range(5*6):
    score = scores[a]
    print(score)
    axes.append(fig.add_subplot(5, 6, a+1))
    subplot_title=str(score[0])
    axes[-1].set_title(subplot_title)  
    plt.axis('off')
    plt.imshow(Image.open(NEW_PATH+'/'+score[1]))
fig.tight_layout()
plt.show()

