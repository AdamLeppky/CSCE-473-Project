import copy
import cv2
import numpy as np
import sys


def show_all_images(img1, img2, mask, overlay, change_text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 2
    color = (255, 255, 0)
    thickness = 2

    img1 = cv2.putText(img1, 'Image 1', org, font, fontScale, color, thickness, cv2.LINE_AA)
    img2 = cv2.putText(img2, 'Image 2', org, font, fontScale, color, thickness, cv2.LINE_AA)
    mask = cv2.putText(mask, 'Mask', org, font, fontScale, color, thickness, cv2.LINE_AA)
    overlay = cv2.putText(overlay, "Change: " + change_text, org, font, fontScale, color, thickness, cv2.LINE_AA)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hor1 = np.concatenate((img1, img2), axis=1)
    hor2 = np.concatenate((mask, overlay), axis=1)
    ver = np.concatenate((hor1, hor2), axis=0)
    cv2.namedWindow("Images", cv2.WINDOW_NORMAL)
    cv2.imshow("Images", ver)


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
    overlay[:, :, 0][mask > 0] = 0
    overlay[:, :, 1][mask > 0] = 0
    overlay[:, :, 2][mask > 0] = 255
    return overlay


def create_mask(img1, img2):
    mask = cv2.bitwise_xor(img1, img2)
    non_black = np.any(mask != [0, 0, 0], axis=-1)
    mask[non_black] = [255, 255, 255]	
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    return mask


def main():
    if len(sys.argv) != 3:
        print("Requires exactly two image paths as input.")
        return
    
    img1 = cv2.imread(sys.argv[1])
    img2 = cv2.imread(sys.argv[2])

    if img1 is None or img2 is None:
        print("Images don't exist.")
        return

    mask = create_mask(img1, img2)
    overlay = create_overlay(img1, mask)

    change = calculate_change_percent(mask)
    print(change)

    height, width, _ = img1.shape
    img2 = cv2.resize(img2, (width, height))
    mask = cv2.resize(mask, (width, height))
    overlay = cv2.resize(overlay, (width, height))

    print(img1.shape)
    print(img2.shape)
    print(mask.shape)
    print(overlay.shape)

    # show_image(img1, "img1")
    # show_image(img2, "img2")
    # show_image(mask, "Mask")
    # show_image(overlay, "Overlay")
    show_all_images(img1, img2, mask, overlay, change)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
