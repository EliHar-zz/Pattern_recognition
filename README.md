# Face Recognition

### Install Docker
[Installation guide](https://docs.docker.com/engine/getstarted/step_one/)</br>
[Docker commands](https://docs.docker.com/engine/reference/commandline/)

### Pull Docker container
<code>docker pull elihar/openface</code>

### Run Docker container
<code>docker run -v [shared/directory/path]:/root/openface/shared -p 9000:9000 -p 8000:8000 -t -i elihar/openface /bin/bash</code>

### Go to openface directory
<code>cd /root/openface</code>

### Add training data
Add images of people to be classified in directories named after each person. These will be the classes. Then move these directories to <code>./training-images/</code>

### Face detection, cropping, pose detection and alignment
<code>pose_detect_align</code> OR

<code>./util/align-dlib.py ./training-images/ align outerEyesAndNose ./aligned-images/ --size 96</code>

### Extract 128 features per face and generate a face representation
<code>gen_rep</code> OR

<code>./batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/</code>

### Train a face recognition model with desired classifier
<code>train_model [classifier name]</code> OR

<code>./demos/classifier.py train ./generated-embeddings/ --classifier [classifier name]</code>

Classifier name: <code>LinearSvm, GridSearchSvm, GMM, RadialSvm, DecisionTree, GaussianNB, DBN</code>

### Recognize an unknown face
<code>recognize [image/path]</code> OR

<code>./demos/classifier.py infer ./generated-embeddings/classifier.pkl [image/path]</code>

Add <code>--multi</code> for recognizing multiple faces in an image


### Web Interface
Navigate to <code>/root/web_server</code>

run <code>python server.py</code>

Open <code>0.0.0.0:8000</code> in Chrome or Firefox

#####[Original resource](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78#.fh7imzgnm)
