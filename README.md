# 🔥 Ident-O-Fire 2020
This app scans through a series of images which are tagged as either "fire" or "no fire".
Once done, the app can take in an image, and tell you whether it has fire in it or not.

All of this is done through Neural Networks!

### Well Documented
You can see within the jupyter notebook that terms are well-defined, and hopefully you can read along even if you have little experience with jupyter notebooks.
Hopefull, the only thing you need to understand the notebook is some knowledge with python, or another coding language.

### Contains Visual Aids
Wherever possible, the notebook utilizes visual aids.
Many of the visuals are pulled down from the internet using various resources.
Some of these aids are hand-drawn by [@noltron000][https://github.com/noltron000] personally.

### Uses Several Technologies
Technologies Used:
1. Python
1. Keras
1. Jupyter Notebooks
1. Markdown

Furthermore, everything is well-outlined to help even newbies understand the data-model.

## Setup
1. <kbd>clone</kbd> this repo
	- run `git clone git@github.com:noltron000/fire-data.git` in a directory of your choice
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
1. run `jupyter notebook` in your project to begin the notebook

## [Check it out in The Browser][Files]
## [Google Slide Deck][Slides]
## Jupyter Slides
You can run the notebook as a slide-show using the following commands in terminal:
1. set up the project as outlined above.
1. copy and run these commands in terminal to set up the submodule:
	```
	jupyter nbconvert image_data_prep.ipynb --to slides --post serve
	```

[Files]: https://github.com/noltron000/fire-data/blob/master/fire_image_classification.py
[Slides]: https://github.com/noltron000/fire-data/blob/master/image_data_prep.ipynb
