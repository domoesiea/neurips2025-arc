# Databricks notebook source
from solutions.task001 import solve

def test_task001_train_examples():
    # Exemple fictif
    input_grid = [[1,0],[0,1]]
    expected_output = [[1,1],[0,0]]
    assert solve(input_grid) == expected_output
