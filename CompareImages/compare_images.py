import copy
import cv2
import numpy as np
import sys


### GLOBAL VARIABLES
#
# Text and Rectangle
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_X, FONT_Y, FONT_WIDTH, FONT_HEIGHT = 0, 0, 250, 80
FONT_SCALE = 1
FONT_THICKNESS = 2
FONT_COLOR = (255, 255, 255)
RECTANGLE_BACKGROUND_COLOR = (50, 50, 50)
CUSTOM_OVERLAY_WIDTH = 500
CUSTOM_MASK_WIDTH = 180
# Overlay
OVERLAY_COLOR = (0, 0, 255)
SHOW_TEXT_ON_OVERLAY = True


def show_all_images(img1, img2, mask, overlay, change_text):
    if SHOW_TEXT_ON_OVERLAY:
        # Black Rectangle
        cv2.rectangle(img1, (FONT_X, FONT_X), (FONT_X + FONT_WIDTH, FONT_Y + FONT_HEIGHT), RECTANGLE_BACKGROUND_COLOR, -1)
        cv2.rectangle(img2, (FONT_X, FONT_X), (FONT_X + FONT_WIDTH, FONT_Y + FONT_HEIGHT), RECTANGLE_BACKGROUND_COLOR, -1)
        cv2.rectangle(mask, (FONT_X, FONT_X), (FONT_X + CUSTOM_MASK_WIDTH, FONT_Y + FONT_HEIGHT), RECTANGLE_BACKGROUND_COLOR, -1)
        cv2.rectangle(overlay, (FONT_X, FONT_X), (FONT_X + CUSTOM_OVERLAY_WIDTH, FONT_Y + FONT_HEIGHT), RECTANGLE_BACKGROUND_COLOR, -1)

        # Text
        img1 = cv2.putText(img1, 'Image 1', (FONT_X + int(FONT_WIDTH/10),FONT_Y + int(FONT_HEIGHT/2)), FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, cv2.LINE_AA)
        img2 = cv2.putText(img2, 'Image 2', (FONT_X + int(FONT_WIDTH/10),FONT_Y + int(FONT_HEIGHT/2)), FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, cv2.LINE_AA)
        mask = cv2.putText(mask, 'Mask', (FONT_X + int(CUSTOM_MASK_WIDTH/10),FONT_Y + int(FONT_HEIGHT/2)), FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, cv2.LINE_AA)
        overlay = cv2.putText(overlay, "Change (Red): " + change_text, (FONT_X + int(CUSTOM_OVERLAY_WIDTH/10),FONT_Y + int(FONT_HEIGHT/2)), FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    # Concatenate all images into one
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hor1 = np.concatenate((img1, img2), axis=1)
    hor2 = np.concatenate((mask, overlay), axis=1)
    vert = np.concatenate((hor1, hor2), axis=0)

    cv2.namedWindow("Images", cv2.WINDOW_NORMAL)
    cv2.imshow("Images", vert)


def show_image(image, title):
    height, width = image.shape[:2]
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, width, height)
    cv2.imshow(title, image)


def calculate_change_percent(mask):
    white_count = np.sum(mask == 255)
    other_count = np.sum(mask != 255)
    total_count = white_count + other_count
    print(f"White: {white_count}")
    print(f"Other: {other_count}")
    print(f"Total: {total_count}")
    print("Change: {:.2%}".format(white_count / total_count))
    return "{:.2%}".format(white_count / total_count)



def create_overlay(image, mask):
    overlay = copy.copy(image)
    overlay[:, :, 0][mask > 0] = OVERLAY_COLOR[0]
    overlay[:, :, 1][mask > 0] = OVERLAY_COLOR[1]
    overlay[:, :, 2][mask > 0] = OVERLAY_COLOR[2]
    return overlay


def create_mask(img1, img2):
    mask = cv2.bitwise_xor(img1, img2)
    non_black = np.any(mask != [0, 0, 0], axis=-1)
    mask[non_black] = [255, 255, 255]	
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    return mask


def main():
    if len(sys.argv) not in [3, 4]:
        print("Requires two or three image paths as input.")
        return
    
    img1 = cv2.imread(sys.argv[1])
    img2 = cv2.imread(sys.argv[2])
    if img1 is None or img2 is None:
        print("Images don't exist.")
        return
    
    if len(sys.argv) == 4:
        original_image = cv2.imread(sys.argv[3])
    else:
        original_image = None

    mask = create_mask(img1, img2)
    if original_image is None:
        overlay = create_overlay(img1, mask)
    else:
        overlay = create_overlay(original_image, mask)

    change = calculate_change_percent(mask)
    print(change)

    height, width, _ = img1.shape
    img2 = cv2.resize(img2, (width, height))
    mask = cv2.resize(mask, (width, height))
    overlay = cv2.resize(overlay, (width, height))

    # show_image(img1, "img1")
    # show_image(img2, "img2")
    # show_image(mask, "Mask")
    # show_image(overlay, "Overlay")
    show_all_images(img1, img2, mask, overlay, change)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
