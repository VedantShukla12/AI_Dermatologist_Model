import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report
# from tensorflow.keras.applications.vgg16 import preprocess_input

model1 = tf.keras.models.load_model("melanoma_cnn.keras")
model1.save("model_from_scratch.h5")

model2 = tf.keras.models.load_model("vgg16_melanoma_cnn.keras")
model2.save("vgg16_model.h5")

model3 = tf.keras.models.load_model("resnet_melanoma_cnn.keras")
model3.save("resnet_model.h5")

'''
def load_data():
    x_train = np.load("x_train.npy")
    y_train = np.load("y_train.npy")

    x_test = np.load("x_test.npy")
    y_test = np.load("y_test.npy")

    return x_train, y_train, x_test, y_test

x_train, y_train, x_test, y_test = load_data()
# x_test = x_test.astype('float32') / 255.0
# y_test.reshape(y_test.shape[0], 1)
x_test = preprocess_input(x_test)

# evaluate model
print(f"Accuracy: {model.evaluate(x_test, y_test)[1] * 100}%")
print(model.summary())

predictions = model.predict(x_test)
predictions[predictions >= 0.5] = 1
predictions[predictions < 0.5] = 0

print(predictions)
print(classification_report(y_test, predictions))
# tf.keras.utils.plot_model(model, to_file="model architecture.png", show_shapes=True)
'''