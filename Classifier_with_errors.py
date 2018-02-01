from keras.applications.resnet50 import ResNet
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

"""
Creates a CNN with the ResNet50 architecture and initializes the
weights to those trained using ImageNet. If the ImageNet ResNet50
weights aren't yet on the server, this will download them from
the keras github page.
"""
model = ResNet50(weights='imagenet')



class Classifier:
    def __init__(self):
        self._architecture = 'ResNet50'
        self._target_size = (224,224)

    def process_image(self, img_path):

        self._img_path = img_path
        img = image.load_img(img_path, target_size=self._target_size)

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        self._orig_img = img
        self._x = x

    def classify_image(self):

        self._preds = model.predict(self._x)

    def get_classification(self):

        self.category = decode_predictions(self._preds, top=1)[0][1]

    def get_border(self):
        if len(category)%2 > 0:
            self.border = 'blue'
        else:
            self.border = 'blue'

    def response(self):
        return {'category': self.category, 'border': self.border}

    def pipeline(self, img_path):
        self.process_image(img_path)
        self.classify_image()
        self.get_classification()

        return self.response()



# to use the above class, use the following commands

# classifier = Classifier()
#
# classifier.process_image('/PATH/TO/elephant.jpg')
# classifier.classify_image()
# classifier.get_classification()
# classifier.get_border()
# out = classifier.response()

# or

# classifier = Classifier()
out = classifier.pipeline('/FIR/recruiting/challenge_questions/elephant.jpg')
out
