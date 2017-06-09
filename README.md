# Deep-Learning-in-Visual-Recognition-and-Planning

## Install requirements:

Install bazel and tensorflow ( check tensorflow's github for more info ) 

### If you have Ubuntu 14.04

Run the following commands

```
sudo add-apt-repository ppa:webupd8team/java
```
```
sudo apt-get update
```
```
sudo apt-get install oracle-java8-installer
```
- Download bazel (version: https://github.com/bazelbuild/bazel/releases/download/0.2.0/bazel-0.2.0-jdk7-installer-linux-x86_64.sh)

```
-chmod +x PATH_TO_INSTALL.SH
```
```
- ./PATH_TO_INSTALL.SH --user
```
- Place bazel onto path ( exact path to store shown in the output)


### How to retrain the imagenet from tensorflow
- For retraining, prepare folder structure as
    - root_folder_name
        - class 1
            - file1
            - file2
        - class 2
            - file1
            - file2
- Clone tensorflow
- Go to root of tensorflow
```
sudo bazel build tensorflow/examples/image_retraining:retrain
```
```
sudo bazel-bin/tensorflow/examples/image_retraining/retrain --image_dir /path/to/root_folder_name  --output_graph /path/output_graph.pb --output_labels /path/output_labels.txt --bottleneck_dir /path/bottleneck
```
Train done passing for test

### How to test it:

Run file evaluate_image.py


## Cut videos in frames

You must install ffmpeg for this

```
ffmpeg -i video.mp4 -r 5 image%03d.jpg
```
If you need more frames increase the number followed by the flag -r


##Run with kinect 2
```
roslaunch kinect2_bridge kinect2_bridge.launch
```

## Run evaluate images to get images and save them
 In ros directory
``` 
 source devel/setup.bash
```
Then run 

```
rosrun kinect_images save_image.py 

```

