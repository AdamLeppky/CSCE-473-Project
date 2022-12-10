# CSCE-473-Project
CSCE-473 Computer Vision Final Project - Fall 2022

## Team
- Anthony Luu
- Adam Leppky
- Peter Cao
- John Cerny

## Visualizing Changes in Water Area
Given two satellite image masks produced by the DeepLabV3 model, calculate the difference and visualize it.

<img src="https://user-images.githubusercontent.com/13823591/206872380-def1435e-317a-4454-99c2-62d6b56c9ec0.png" width="300"> <img src="https://user-images.githubusercontent.com/13823591/206872386-5248faae-337f-47b4-ac51-0350469861c9.png" width="300">

<img src="https://user-images.githubusercontent.com/13823591/206872542-f6a6968b-b0f2-4e24-adf1-ee44b7e3be3a.png" width="300"> <img src="https://user-images.githubusercontent.com/13823591/206872543-375c9cac-2e0d-4b71-af44-11a411d9c061.png" width="300">

<img src="https://user-images.githubusercontent.com/13823591/206872607-ed775706-0aac-40e2-81dd-5ab472327aba.png" width="300"> <img src="https://user-images.githubusercontent.com/13823591/206872608-52351bcf-e6ec-4d5d-bb6d-35a33721a601.png" width="300">

### Instructions
This example uses the following images you can try:
- Original Satellite Image from 2005: `examplesImages\1-2005.png`
- Original Satellite Image from 2021: `examplesImages\1-2021.png`
- Mask Image from 2005: `examplesImages\1-mask2005.png`
- Mask Image from 2021: `examplesImages\1-mask2021.png`

How to Run:
- To run with a visualization overlay on one of the masks, run:
  - `python compare_images.py examplesImages\1-2005.png examplesImages\1-2021.png`
  - The two arguments are the paths to the mask images.
- To run with a visualization overlay on one of the original satellite images, run:
  - `python compare_images.py examplesImages\1-2005.png examplesImages\1-2021.png examplesImages\1-2005.png`
  - The first two arguments are the paths to the mask images. The third argument is the original image for which the overlay will be added.
