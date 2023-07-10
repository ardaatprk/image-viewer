import argparse
import cv2
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('image', help="patho to input image")
    args = vars(ap.parse_args())
    image=cv2.imread(args["image"])
    cv2.imshow("TownCenter",image)
    cv2.waitKey(0)
if __name__== '__main__':
    main()
    exit(0)

