# 🔥 Fire...or No Fire?
This app scans through a series of images which are tagged as either "fire" or "no fire".
Once done, the app can take in an image, and tell you whether it has fire in it or not.

All of this is done through Nueral Networks!

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

## Jupyter Slides
You can run the app as a slide-show using the following commands in terminal:
1. copy and run these commands in terminal to set up the submodule:
	```
	jupyter nbconvert image_data_prep.ipynb --to slides --post serve
	```

## Pseudocode
![whiteboard code][whiteboard]

[whiteboard]: ./IN_CLASS.jpg
