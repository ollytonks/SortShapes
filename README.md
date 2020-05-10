# SortShapes
Sorting shapes into Triangles, Squares and Circles. Open ended project that starts from a basic object oriented design to some more interesting developments!

## To Run

Download repository and make sure all relevant libraries are installed. Run command

```
pip install matplotlib opencv-python numpy
```

Once installed can run each script individually (using python3), for the CannyTest and for the ImageSorter it will open up your webcam in case you get a shock!

If you want to run the detection over static inputs, just input the file path as an argument when running the program. It will accept multiple files but will analyse them one after the other. Press 'q' to close a live feed or to move onto the next image

### Current status

When run you will see a parameters frame and the frame with the relevant images. Currently the preset paramaters for threshold and area work fine. However when looking at the images in the frame if there is a lot of noise, try increasing the minimum threshold. This works best for images with really diverse lighting / backgrounds. If you have an image with a blank background, clear lighting and really clear shapes the current settings should work. Feel free to play with the settings though, thats why there are the trackbars! The shape detection is a bit finicky at the moment with a lot of noise being a problem as well as dealing with shapes that have multiple colours, I'm looking into better detection methods. I might have reached the end of the line with working with OpenCV and it's inbuilt functionality.

Machine learning notes:
- There are a lot of tools out there to use; tensorflow, keras, lasagne, scikit-learn
- Autoencoder is seriously promising for reducing image noise effectively. This could then be plugged in to work with OpenCV contour detection for some noice shape detection
- Could use tensorflow object detection api, unsure if it works for just pure geometric shape detection? This is an easy way out if it's possible
- Think what would be better would be if I could build model from the ground up
- https://www.kaggle.com/smeschke/four-shapes#display_model.py  < this is a good example using keras, think it might have limited functionality when it comes to working with shapes that aren't the one colour / different sizes. So current OpenCV work would probably be the same
- https://www.coursera.org/learn/machine-learning < ML course that starts on Monday
- https://medium.com/@kaibrooks/creating-a-neural-network-from-the-ground-up-for-classifying-your-own-images-in-keras-tensorflow-91e57d480c24 < this looks handy

### Future plans

- [x] Live image feed
- [x] Adjustable threshold for images
- [x] Stack images for easy threshold manipulation
- [X] Have option to run detection on static image input
- [ ] Review comments, maybe too much?
- [x] Detect images based on vertice and canny algorithm
- [X] **Look into machine learning shape detection for better noise handling**
- [ ] Create ShapeDetector object for some delicious object oriented design, need to reduce file length
- [ ] Look into dynamic threshold calculators for reduced human input
- [ ] Try a threshold image input to reduce noise instead of customisable threshold 
- [ ] Review classification placement, can be visually cluttered
- [ ] Create demonstration video / pictures
- [X] Write on read me what thresholds to use usually
- [ ] Customisable image dilation for finer images
- [X] **Look into ML tools for object detection in images**

