# SortShapes
Sorting shapes into Triangles, Squares and Circles. Open ended project that starts from a basic object oriented design to some more interesting developments!

## To Run

Download repository and make sure all relevant libraries are installed. Run command

```
pip install matplotlib opencv-python numpy
```

Once installed can run each script individually (using python3), for the CannyTest and for the ImageSorter it will open up your webcam in case you get a shock!

### Current status

When run you will see a parameters frame and the frame with the relevant images. Currently the preset paramaters for threshold and area work fine. However when looking at the images in the frame if there is a lot of noise, try increasing the minimum threshold. This works best for images with really diverse lighting / backgrounds. If you have an image with a blank background, clear lighting and really clear shapes the current settings should work. Feel free to play with the settings though, thats why there are the trackbars! The shape detection is a bit finicky at the moment with a lot of noise being a problem as well as dealing with shapes that have multiple colours, I'm looking into better detection methods. I might have reached the end of the line with working with OpenCV and it's inbuilt functionality, I'm starting to look at some machine learning methods.

### Future plans

- [x] Live image feed
- [x] Adjustable threshold for images
- [x] Stack images for easy threshold manipulation
- [X] Have option to run detection on static image input
- [ ] Review comments, maybe too much?
- [x] Detect images based on vertice and canny algorithm
- [ ] Look into machine learning shape detection for better noise handling
- [ ] Create ShapeDetector object for some delicious object oriented design, need to reduce file length
- [ ] Look into dynamic threshold calculators for reduced human input
- [ ] Try a threshold image input to reduce noise instead of customisable threshold 
- [ ] Review classification placement, can be visually cluttered
- [ ] Create demonstration video / pictures
- [X] Write on read me what thresholds to use usually
- [ ] Customisable image dilation for finer images
