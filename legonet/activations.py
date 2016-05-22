# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:55:04 2016

@author: lifu
"""


import tensorflow as tf


def identity(x):
    """Return the input tensor without any change.
    :param x: Input tensor.
    :return: The input tensor.
    """

    return x


def relu(x):
    """Compute the rectified linear of x.
    :param x: Input tensor.
    :return: A `Tensor` of same shape as `x`.
    """

    return tf.nn.relu(x)


def tanh(x):
    """Compute the hyperbolic tangent of x.
    :param x: Input tensor.
    :return: A `Tensor` of same shape as `x`.
    """

    return tf.tanh(x)


def sigmoid(x):
    """Compute the sigmoid of x.
    :param x: Input tensor.
    :return: A `Tensor` of same shape as `x`.
    """

    return tf.sigmoid(x)


def softmax(x):
    """Compute the softmax of x.
    :param x: Input tensor.
    :return: A `Tensor` of same shape as `x`.
    """

    return tf.nn.softmax(x)


_activations = {'relu': relu,
                'identity': identity,
                'sigmoid': sigmoid,
                'softmax': softmax,
                'tanh': tanh}


def get(name):
    """Return activation according to name.
    :param name: name of activation function.
    :return: the activation according to `name`.
    """
    
    if name not in _activations:
        raise ValueError('Unknown activation function: {0}'.format(name))
    return _activations[name]
