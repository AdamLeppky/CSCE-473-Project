# CSCE-473-Project
CSCE-473 Computer Vision Final Project - Fall 2022

## Team
- Anthony Luu
- Adam Leppky
- Peter Cao
- John Cerny

## Visualizing Changes in Water Area
Given two satellite image masks produced by the DeepLabV3 model, calculate the difference and visualize it.

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
