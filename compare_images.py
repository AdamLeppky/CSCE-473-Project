import cv2
import numpy as np
import sys


def show_image(image, title):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, image)


def print_information(mask):
    white_count = np.sum(mask == 255)
    other_count = np.sum(mask != 255)
    total_count = white_count + other_count
    print(f"White: {white_count}")
    print(f"Other: {other_count}")
    print(f"Total: {total_count}")
    print("{:.2%}".format(white_count / total_count))



def create_overlay(image, mask):
    overlay = image
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

    print_information(mask)

    show_image(overlay, "Overlay")
    show_image(mask, "Mask")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
