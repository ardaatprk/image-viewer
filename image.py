import argparse
import cv2

def main():
    parser =argparse.ArgumentParser()
    parser.add_argument("TownCenter.jpg")
    ap = argparse.ArgumentParser()
    ap.add_argument('image', help="path to input image")
    image=cv2.imread('/home/arda/intern/introduction/image-viewer/image/TownCenter.jpg')
    cv2.imshow("image",image)
    cv2.waitKey(0)

if __name__== '__main__':
    main()
    exit(0)