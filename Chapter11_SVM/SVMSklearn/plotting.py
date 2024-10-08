from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


cmap_light = ListedColormap(["#FFAAAA", "#AAAAFF"])
colors = np.array(["red", "blue"])


def plot_dataset(x: np.ndarray, y: np.ndarray) -> None:
    plt.scatter(x[:, 0], x[:, 1], c=colors[y])
    plt.show()


def make_meshgrid(x: np.ndarray, y: np.ndarray, h: float = 0.02) -> Any:
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy


def plot_contours_(
    ax: Any,
    clf: Any,
    xx: np.ndarray,
    yy: np.ndarray,
    **params: Any,
) -> Any:
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])  # noqa: N806
    Z = Z.reshape(xx.shape)  # noqa: N806
    return ax.contourf(xx, yy, Z, **params)


def plot_contours(clf: Any, x: np.ndarray, y: np.ndarray) -> None:
    _, ax = plt.subplots()
    X0, X1 = x[:, 0], x[:, 1]  # noqa: N806
    xx, yy = make_meshgrid(X0, X1)
    plot_contours_(ax, clf, xx, yy, cmap=cmap_light, alpha=0.8)
    plt.scatter(x[:, 0], x[:, 1], c=colors[y])
    plt.show()
