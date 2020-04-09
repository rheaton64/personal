from __future__ import print_function
from spike.app import SpikeLive
from imutils.video import VideoStream
import argparse
import time

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required = True, help = "path of output directory")
args = vars(ap.parse_args())

print("[INFO] warming up camera...")
vs = VideoStream().start()
time.sleep(2.0)

a = SpikeLive(vs, args['output'])
a.root.mainloop()