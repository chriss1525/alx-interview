#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """ rotate a 2d matrix in 90 degrees clockwise. """
    # do not return anything, modify matrix in-place instead.
    # assume the matrix will have 2 dimensions and will not be empty.

    n = len(matrix)

    # transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for i in range(n):
        matrix[i].reverse()
