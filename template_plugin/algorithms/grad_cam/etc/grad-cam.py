import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import requests
from tf_keras_vis.utils import num_of_gpus
from tensorflow.keras.applications.vgg16 import VGG16 as Model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
from io import BytesIO
from tf_keras_vis.utils.model_modifiers import ReplaceToLinear

model = Model(weights='imagenet', include_top=True)
image_titles = ['Dog']
url = "https://raw.githubusercontent.com/jacobgil/keras-grad-cam/master/examples/cat_dog.png"
try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    img = load_img(BytesIO(response.content), target_size=(224, 224))
except requests.exceptions.RequestException as e:
    print("Error fetching the image:", e)
except Exception as e:
    print("Error processing the image:", e)

images = np.asarray([np.array(img)])
X = preprocess_input(images)
f, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 4))
for i, title in enumerate(image_titles):
    ax.set_title(title, fontsize=16)
    ax.imshow(images[i])
    ax.axis('off')

plt.tight_layout()
plt.savefig('./output/images.png')

replace2linear = ReplaceToLinear()
def model_modifier_function(cloned_model):
    cloned_model.layers[-1].activation = tf.keras.activations.linear

from tf_keras_vis.utils.scores import CategoricalScore

score = CategoricalScore([1, 294, 413])

def score_function(output):
    return (output[0][1], output[1][294], output[2][413])

from tensorflow.keras import backend as K
from tf_keras_vis.saliency import Saliency

saliency = Saliency(model,
                    model_modifier=replace2linear,
                    clone=True)

print(score, X)
saliency_map = saliency(score, X)
# f, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 4))
# for i, title in enumerate(image_titles):
#     ax.set_title(title, fontsize=16)
#     ax.imshow(saliency_map[i], cmap='jet')
#     ax.axis('off')

# plt.tight_layout()
# plt.savefig('./output/saliency_map.png')
