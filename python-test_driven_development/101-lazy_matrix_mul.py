#!/usr/bin/python3
"""
DEfining a multiplying function
"""
import numpy as num


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplying two matrices using NumPy
    """
    return num.matmul(m_a, m_b)
