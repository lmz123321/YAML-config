## This is a simple yet detailed instruction on how to use YAML to set your configs.
### Environments requirement
`pip install yacs`
### Functions of our code
* main.py This is you main training code.
* setting.yaml You can set the specific configs for a particular experiment here.
* defauls.py You can set all your deault configs here.
### Examples
Say you want to train a **ResNet-50** model on **ImageNet** dataset. You also want to set you **batch size** into 64 and your **base learning rate** into 0.001.

You can either directly change them in the **setting.yaml** and use command like:

`python main.py --config-file ./setting.yaml`

Or without changing the **setting.yaml** and use command like:

`python main.py --config-file ./setting.yaml MODEL.ARCH ResNet50 DATA.TYPE ImageNet SOLVER.BATCH_SIZE_CLS 64 SOLVER.BASE_LR 0.001`
### License
If you are a beginer to YAML, feel free to raise a Issue, I will responde as fast as I see it.

Some of this code borrows ideas from FaceBook Research MaskRCNN_Benchmark.
