from manim import *
import random

from manim_ml.neural_network.layers.parent_layers import VGroupNeuralNetworkLayer

class VectorLayer(VGroupNeuralNetworkLayer):
    """Shows a vector"""

    def __init__(self, num_values, value_func=lambda: random.uniform(0, 1),
                **kwargs):
        super().__init__(**kwargs)
        self.num_values = num_values
        self.value_func = value_func
        # Make the vector
        self.vector_label = self.make_vector()
        self.add(self.vector_label)

    def make_vector(self):
        """Makes the vector"""
        if False:
            # TODO install Latex
            values = np.array([self.value_func() for i in range(self.num_values)])
            values = values[None, :].T
            vector = Matrix(values)

        vector_label = Text(f"[{self.value_func():.2}]")
        vector_label.scale(0.5)

        return vector_label

    def make_forward_pass_animation(self):
        return AnimationGroup()
        
    @override_animation(Create)
    def _create_override(self):
        """Create animation"""
        return Write(self.vector_label)