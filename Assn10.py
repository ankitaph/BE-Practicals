# Write a python program to implement CNN object detection. Discuss numerous performance
# evaluation metrics for evaluating the object detection algorithm's performance
from keras.datasets import cifar10 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D  
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

# Load CIFAR-10 dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data() 

##scales the pixel values of the images between 0 and 1)
train_set = ImageDataGenerator(rescale=1./255).flow(X_train, y_train, batch_size=64)
test_set = ImageDataGenerator(rescale=1./255).flow(X_test, y_test, batch_size=64)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu'),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Conv2D(64, (3, 3), activation='relu'),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
#Stochastic Gradient Descent
sgd = SGD(learning_rate=0.01, decay=1e-6, nesterov=True)
model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_set, epochs=2, 
          validation_data=test_set, 
          steps_per_epoch=len(X_train)//64, 
          validation_steps=len(X_test)//64 )

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_set) 
print('Test loss:', test_loss)
print('Test accuracy:', test_accuracy)