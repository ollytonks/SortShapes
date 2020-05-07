# SortShapes
Sorting shapes into Triangles, Squares and Circles. Open ended project that starts from a basic object oriented design to some more interesting developments!

## To Run

Download repository and make sure all relevant libraries are installed. Run command

```
pip install matplotlib opencv-python numpy
```

Once installed can run each script individually (using python3), for the CannyTest and for the ImageSorter it will open up your webcam in case you get a shock! If you don't have a webcam program will error out :finnadie:

### Future plans

- [x] Live image feed
- [x] Adjustable threshold for images
- [x] Stack images for easy threshold manipulation
- [ ] Have option to run detection on static image input
- [ ] Comment (I know it should be done concurrently :shit:)
- [x] Detect images based on vertice and canny algorithm
- [ ] Look into machine learning shape detection for better noise handling
- [ ] Create ShapeDetector object for some delicious object oriented design
- [ ] Look into dynamic threshold calculators for reduced human input
- [ ] Try a threshold image input to reduce noise instead of customisable threshold 
