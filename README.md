# neural-networks

Contains code, datasets and results for various ANN projects.

## Contents:

### Neural networks:

These neural networks were written using scipy and numpy and can be found in the `src` folder. They are not optimized or efficient and are instead intended for educational purposes.

#### Multilayer perceptron (`mlp.py`): 

A basic feed-forward network. Class-oriented implementation allows for various features to be added and tweaked, including the structure of the network, the cost function, the activation function, and the process used to train the network. 

#### Convolutional neural network (`conv_nn.py`):

A basic convolutional neural network. Its structure is different from `mlp.py` in that this neural network is built by stacking layers. This allows for greater versatility-- both a convolutional and a feed-forward network can be created using `conv_nn.py`. Though this program does not have as many features as `mlp.py` (i.e., it is lacking dropout, SGD momentum, learning rate decay, etc.), it is still functional.

### Projects:

Application of neural networks to various problems.

#### MNIST (`mnist`):

MLPs and ConvNNs applied to the classic "Hello World" of machine learning problems-- digit recognition with the MNIST dataset.

#### AI Credit (`credit-analysis`):

Part of a joint effort to create a credit analysis tool trained on Lending Club's dataset. `original` created during HackMHS VI and `new` created for submission to a Blockstack program.

## Download instructions:

(These are the download instructions for Mac as of 2019 and assume that the user has downloaded Python.)

### Libraries:

In order to use the code in this repository, run the following command in terminal: `pip3 install pandas xlrd matplotlib numpy scipy tensorflow keras`. (For Python2 users, replace `pip3` with `pip`.)

If you do not have `pip` installed, you will get the following error: `-bash: pip: command not found`. Refer to https://pip.pypa.io/en/stable/installing/ for a `pip` installation guide.

### Cloning this repository:

In order to clone this repository, `cd` to the target directory and run the command: `git clone https://github.com/orangese/neural-networks.git <name>`.
