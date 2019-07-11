
"""

"mnist_conv_display.py"

A program to display the results of a trained ConvNN.

"""

#Libraries
import sys
sys.path.insert(0, "/Users/ryan/Documents/Coding/neural-networks/src")
from conv_nn import Network, Layer, Conv, Pooling, Dense
sys.path.insert(0, "/Users/ryan/Documents/Coding/neural-networks/\
                 mnist/mnist-code")
from mnist_loader import load_data
import matplotlib.pyplot as plt
import numpy as np
from time import time

#Graphics
def closest_multiples(n):
  #returns two multiples of n that are closest together
  if n == 1 or n == 0: return (n, n)
  factors = []
  for i in range(1, n):
    if n % i == 0: factors.append(((i, int(n / i)), (abs(i - int(n / i)))))
  return factors[np.argmin(list(zip(*factors))[1])][0]

def display(net, show_kernel = False, layer = Layer):
  #displays output of a layer or kernel weights using plt.imshow
  if show_kernel: layer = Conv
  disp_layer = next((l for l in net.layers if isinstance(l, layer)), None)
  if disp_layer is None: return None
  disp_obj = np.copy(disp_layer.weights if show_kernel else disp_layer.output)
  fig, axes = plt.subplots() if layer is Layer \
              else plt.subplots(*closest_multiples(disp_layer.dim[0]))
  fig.canvas.set_window_title("Visualizing convolutional networks")
  if show_kernel: fig.suptitle("Kernel weights for {0} layer".format(layer))
  else: fig.suptitle("Output for {0} layer".format(layer))
  try:
    for ax in axes.flatten():
      ax.imshow(disp_obj[list(axes.flatten()).index(ax)], cmap = "gray")
      ax.axis("off")
  except AttributeError:
    axes.imshow(disp_obj, cmap = "gray")
    axes.axis("off")
  plt.show()

def display_net(net):
  for layer in net.layers:
    if isinstance(layer, Conv):
      display(net, show_kernel = True)
      display(net, layer = Conv)
    elif isinstance(layer, Pooling): display(net, layer = Pooling)
    elif isinstance(layer, Dense): continue
    else: display(net, layer = Layer)
  input("Press any key to continue: ")

#Testing train functions
def generate_zero_data():
  #generates zero data in the shape of MNIST data
  data = {"train": [], "validation": [], "test": []}
  target = np.zeros((10, 1))
  target[0] = 1.0
  data["train"] = [(np.ones((28, 28)), target) for i in range(50000)]
  data["validation"] = [(np.ones((28, 28)), 0) for i in range(10000)]
  data["test"] = [(np.ones((28, 28)), 0) for i in range(10000)]
  return data

def test(net_type = "conv", data = None, shorten = False, test_acc = False):
  #tests conv_nn.py
  if data is None: data = generate_zero_data()
  if shorten:
    data["train"] = data["train"][:1000]
    data["validation"] = data["validation"][:1000]
    data["test"] = data["test"][:1000]
  
  if net_type == "conv":
    net = Network([Layer((28, 28)), Conv((5, 5), 20, actv = "sigmoid"),
                   Pooling((2, 2)), Dense(100, actv = "sigmoid", reg = 0.0),
                   Dense(10, actv = "softmax", reg = 0.0)],
                  cost = "log-likelihood")
  elif net_type == "mlp":
    net = Network([Layer((28, 28)),
                   Dense(100, actv = "relu", reg = 0.0),
                   Dense(10, actv = "softmax", reg = 0.0)],
                  cost = "log-likelihood")

  start = time()

  if test_acc:
    print ("Evaluation without training: {0}%".format(
      net.eval_acc(data["test"])))
  
  net.SGD(data["train"], 60, 0.03, 10, data["validation"])

  for i in range(10):
    pred = net.propagate(data["test"][i][0])
    if np.argmax(pred) != data["test"][i][1]:
      print ("Ground truth: index {0} - {1}".format(
        data["test"][i][1], round(np.asscalar(pred[data["test"][i][1]]), 5)))
      print ("Max activation: index {0} - {1}".format(
        np.argmax(pred), round(np.max(pred), 5)))
      #display_net(net)

  if test_acc: print ("Accuracy: {0}%".format(net.eval_acc(data["test"])))
  print ("Time elapsed: {0} seconds".format(round(time() - start, 3)))

  return net

#Testing area
if __name__ == "__main__":
  np.seterr(all = "raise")
  data = load_data("conv")
##  net = test(net_type = input("MLP or ConvNN test? (mlp/conv): "), data = data,
##             shorten = False)
  for i in range(10):
    net = test(net_type = "mlp", data = data, shorten = True)
