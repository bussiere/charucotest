'''
Sample Command:-
python generate_aruco_tags.py --id 24 --type DICT_5X5_100 -o tags/
'''


import numpy as np
import argparse
from utils import ARUCO_DICT
import cv2
import sys


ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=False,default="../../../assets/aruco/", help="path to output folder to save ArUCo tag")
ap.add_argument("-i", "--id", type=int, required=False, help="ID of ArUCo tag to generate")
ap.add_argument("-t", "--type", type=str, default="DICT_2X2_50", help="type of ArUCo tag to generate")
ap.add_argument("-s", "--size", type=int, default=200, help="Size of the ArUCo tag")
args = vars(ap.parse_args())


# Check to see if the dictionary is supported
if ARUCO_DICT.get(args["type"], None) is None:
	print(f"ArUCo tag type '{args['type']}' is not supported")
	sys.exit(0)

arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])

i = 0
while i < int(args["type"].split("_")[-1]):
	print("toto")
	args["id"] = i
	print("Generating ArUCo tag of type '{}' with ID '{}'".format(args["type"], args["id"]))
	tag_size = args["size"]
	tag = np.zeros((tag_size, tag_size, 1), dtype="uint8")
	cv2.aruco.drawMarker(arucoDict, args["id"], tag_size, tag, 1)

	# Save the tag generated
	type_aruco = args["type"].replace("DICT_", "")
	tag_name = f'{args["output"]}{type_aruco}/{args["type"]}_id_{args["id"]}.png'
	print(tag_name)
	cv2.imwrite(tag_name, tag)
	i+=1
#cv2.imshow("ArUCo Tag", tag)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
