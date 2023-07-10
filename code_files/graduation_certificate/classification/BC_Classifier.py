import cv2
import numpy as np

def BC_Classifier(org, model):
        
    # resize the image
    image = cv2.resize(org, (224, 224), interpolation=cv2.INTER_LINEAR)

    # normalize the image
    image = np.array(image).astype(np.float32) / 255

    # expand the image dimention to be able to make the prediction
    image = np.expand_dims(image, axis=0)

    # classify BC images
    pred = model.predict(image)
    pred = np.round(pred)
    label = (np.where(pred==1)[1])

    if label == 1:
        image_label = 'Bachelor Cert(Ain Shams)'
    elif label == 0:
        image_label = 'Bachelor Cert'
    elif label == 2:
        image_label = 'Other'
            
    return image_label