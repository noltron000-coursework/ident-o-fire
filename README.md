# 🔥 Fire...or No Fire?
This app scans through a series of images which are tagged as either "fire" or "no fire".
Once done, the app can take in an image, and tell you whether it has fire in it or not.

All of this is done through Nueral Networks!

## Setup
1. copy and run these commands in terminal to set up the submodule:
	```bash
	touch .gitmodules
	git submodule add git@github.com:cair/Fire-Detection-Image-Dataset.git data
	git clone --recurse-submodules git@github.com:cair/Fire-Detection-Image-Dataset.git
	mkdir data
	mv Fire-Detection-Image-Dataset/* data
	mv Fire-Detection-Image-Dataset/.* data
	rmdir Fire-Detection-Image-Dataset
	```
1. extract each `.rar` file in the submodule
	- ensure that the directory structure is formatted in this way: `./data/*/*.jpg`

## Pseudocode
![whiteboard code][whiteboard]

[whiteboard]: ./IN_CLASS.jpg
