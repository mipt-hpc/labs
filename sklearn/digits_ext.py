tandard scientific Python imports
import matplotlib.pyplot as plt
import matplotlib
import sys
from skimage import color
from skimage import io
import numpy as np
# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()
img_file=sys.argv[1]

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 3 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# pylab.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:10]):
    plt.subplot(3, 5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])
print(data[1])
# Now predict the value of the digit on the second half:
img_data = color.rgb2gray(io.imread('./'+img_file))
img_data_r=np.reshape(img_data,(1,64))
img_data_r-=1
img_data_r*=-16

print(img_data_r[0])
predicted=classifier.predict(img_data_r)

plt.subplot(3, 5, 11)
plt.axis('off')
plt.imshow(img_data, cmap=plt.cm.gray_r, interpolation='nearest')
plt.title('Prediction: %i' % predicted)
print(predicted)
plt.show()

