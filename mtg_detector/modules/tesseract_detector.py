from PIL import Image
import pytesseract
import numpy as np

from pprint import pprint

filename = 'C:\\Users\\Utente\\Desktop\\mtg_detector\\test_img\\31.jpg'

# Text classification
print("--------- CLASSIFICATION ----------")
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)


# Text detection and localization

from pytesseract import Output
import cv2

print("--------- DETECTION AND LOCALIZATION ----------")
image = cv2.imread(filename)

######################### PROCESSING
#img =image
#norm_img = np.zeros((img.shape[0], img.shape[1]))
#img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
#img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
#img = cv2.GaussianBlur(img, (1, 1), 0)
#cv2.imwrite('results/preprocess_result.jpg', img)
#results = pytesseract.image_to_data(img, output_type=Output.DICT)


# Convert the RGB image to grayscale
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imwrite('results/output_gray_image.jpg', image)
"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
image = 255 - opening

cv2.imwrite('results/processed_image.jpg', image)
"""
results = pytesseract.image_to_data(image, output_type=Output.DICT)


#results = pytesseract.image_to_data(image, output_type=Output.DICT)

#pprint(results)


def save_txt_detected(image, results):

    for i in range(0, len(results['text'])):
        x = results['left'][i]
        y = results['top'][i]

        w = results['width'][i]
        h = results['height'][i]

        text = results['text'][i]
        conf = int(results['conf'][i])

        if conf > 70:
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

    cv2.imwrite('results/result.jpg', image)
    return 


def show_result_img():
    cv2.imshow('Result',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 