import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image",required=True, help="path to input be displayed")
    args = vars(ap.parse_args())
    
    image=cv2.imread(args["image"]) 
    cv2.imshow("image",image)
    cv2.waitKey(0)

if __name__== '__main__':
    main() 