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

### Uses Several Technologies
Technologies Used:
1. Python
1. Keras
1. Jupyter Notebooks
1. Markdown

Furthermore, everything is well-outlined to help even newbies understand the data-model.

## Setup
Clone the project and initialize its dataset submodule:

```bash
git clone --recurse-submodules https://github.com/noltron000/fire-data.git
cd fire-data
```

The `data` submodule contains the dataset's `.rar` archives. With 7-Zip
installed, extract all archives into the ignored `extracted/` directory:

```powershell
Get-ChildItem data\*.rar | ForEach-Object { 7z x $_.FullName -oextracted }
```

The extracted images should be arranged under class folders, for example
`extracted/Fire images/*.jpg` and `extracted/Normal Images 1/*.jpg` (with the
other `Normal Images` folders alongside). The notebook reads images from
`extracted/*/*.*`.

Run `jupyter notebook` in the project directory to start the notebook.

## [Check it out in The Browser][Files]
## [Google Slide Deck][Slides]
## Jupyter Slides
You can run the notebook as a slide-show using the following commands in terminal:
1. set up the project as outlined above.
1. copy and run these commands in terminal to set up the submodule:
	```
	jupyter nbconvert image_data_prep.ipynb --to slides --post serve
	```

[Files]: https://github.com/noltron000/ident-o-fire/blob/master/image_data_prep.ipynb
[Slides]: https://docs.google.com/presentation/d/1uY8cokZ4nUqoJmNRkWXFD0RDhwb9IgcwDOxFQAVybtM/edit#slide=id.g6d71e4cbe1_0_236
