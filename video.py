import sys
import cv2
import os
from tqdm import tqdm

from run import process


# ------------------------------------------------- main()
def main():
    if len(sys.argv) is 1:
        print('No video file provided.')
        return

    vidcap = cv2.VideoCapture(sys.argv[1])
    total_frames = length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    success,image = vidcap.read()
    count = 0
    for i in tqdm(range(total_frames), desc="Frames"):
        success, image = vidcap.read()
        if not success: break

        filename = 'frame-{}.png'.format(str(count).zfill(8))
        if os.path.isfile(filename):
            overwrite = input('File already exists. Overwrite? (y): ')
            if overwrite.lower() == 'n':
                continue


        watermark = process(image)
        cv2.imwrite(filename, watermark)

        count += 1


if __name__ == '__main__':
	main()
