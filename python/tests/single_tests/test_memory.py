#! /usr/bin/env python

import themis_imager_readfile
import os
import psutil
import time


def main():
    num_workers = 2
    print('RAM Used (MB):', psutil.virtual_memory()[3] / 1000000)
    counter = 0
    for _ in range(0, 10):
        for hour in sorted(os.listdir('stream0/')):
            folder_path = 'stream0/' + hour
            file_names = os.listdir(folder_path)
            file_names = [folder_path + '/' + f for f in file_names if 'full' in f and not f.startswith('.')]
            file_names = file_names[0:5]
            counter += len(file_names)
            img, meta, problematic_files = themis_imager_readfile.read(file_names, workers=num_workers)
            frame_num = img.shape[2]

        print(f"{counter} images read")
        print('RAM Used (MB):', psutil.virtual_memory()[3] / 1000000)

    del frame_num, counter, img, meta, problematic_files, file_names
    time.sleep(10)
    print("after deleting and 10 secs")
    print('RAM Used (MB):', psutil.virtual_memory()[3] / 1000000)


# ------------------------
if (__name__ == '__main__'):
    main()
