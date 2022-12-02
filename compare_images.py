import sys
import cv2


def main():
    # if len(sys.argv) != 3:
    #     print("Requires exactly two image paths as input.")
    #     return
    
    # path1 = sys.argv[1]
    # path2 = sys.argv[2]
    path1 = "C:\\Users\\Adam\\Downloads\\TEST_COMPARE1.png"
    path2 = "C:\\Users\\Adam\\Downloads\\TEST_COMPARE2.png"

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    img_bwa = cv2.bitwise_and(img1,img2)
    img_bwo = cv2.bitwise_or(img1,img2)
    img_bwx = cv2.bitwise_xor(img1,img2)

    cv2.imshow("Bitwise AND of Image 1 and 2", img_bwa)
    cv2.imshow("Bitwise OR of Image 1 and 2", img_bwo)
    cv2.imshow("Bitwise XOR of Image 1 and 2", img_bwx)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
