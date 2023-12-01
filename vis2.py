import matplotlib.pyplot as plt
import numpy as np


def visualize(path):
    # write your code here
    itr = 0
    fig, axes = plt.subplots(nrows=1, ncols=len(path), figsize=(30, 30))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    while itr < len(path):
        node = path[itr]
        state = np.array(node.state.board)
        axes[itr].imshow(state, cmap='jet')
        axes[itr].set_yticklabels([])
        axes[itr].set_xticklabels([])
        itr += 1
    plt.show()
