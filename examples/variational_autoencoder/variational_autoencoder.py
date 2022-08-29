"""Autoencoder Manim Visualizations

In this module I define Manim visualizations for Variational Autoencoders
and Traditional Autoencoders.

"""
from pathlib import Path

from manim import *
import numpy as np
from PIL import Image
from manim_ml.neural_network.layers import EmbeddingLayer
from manim_ml.neural_network.layers import FeedForwardLayer
from manim_ml.neural_network.layers import ImageLayer
from manim_ml.neural_network.neural_network import NeuralNetwork

ROOT_DIR = Path(__file__).parents[2]


class VAEScene(Scene):
    """Scene object for a Variational Autoencoder and Autoencoder"""

    def construct(self):

        numpy_image = np.asarray(Image.open(ROOT_DIR / 'assets/mnist/digit.jpeg'))
        vae = NeuralNetwork([
            ImageLayer(numpy_image, height=1.4),
            FeedForwardLayer(5),
            FeedForwardLayer(3),
            EmbeddingLayer(dist_theme="ellipse").scale(2),
            FeedForwardLayer(3),
            FeedForwardLayer(5),
            ImageLayer(numpy_image, height=1.4),
        ])

        vae.scale(1.3)

        self.play(Create(vae))
        self.play(vae.make_forward_pass_animation(run_time=15))
