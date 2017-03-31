# Deep-Learning-in-Visual-Recognition-and-Planning

Instructions to retrain tensorflow:

Preparing model:
 - Install bazel ( check tensorflow's github for more info )
    Ubuntu 14.04:
        - Requirements:
            sudo add-apt-repository ppa:webupd8team/java
            sudo apt-get update
            sudo apt-get install oracle-java8-installer
        - Download bazel, ( https://github.com/bazelbuild/bazel/releases )
          tested on: https://github.com/bazelbuild/bazel/releases/download/0.2.0/bazel-0.2.0-jdk7-installer-linux-x86_64.sh
        - chmod +x PATH_TO_INSTALL.SH
        - ./PATH_TO_INSTALL.SH --user
        - Place bazel onto path ( exact path to store shown in the output)
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
- bazel build tensorflow/examples/image_retraining:retrain
- bazel-bin/tensorflow/examples/image_retraining/retrain --image_dir /path/to/root_folder_name  --output_graph /path/output_graph.pb --output_labels /path/output_labels.txt --bottleneck_dir /path/bottleneck
** Training done. **

How to test it:

Run file evaluate_image.py


