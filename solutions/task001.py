# Databricks notebook source
"""
Baseline solution for task001
"""

def solve(grid):
    """
    Dummy solver: returns grid unchanged.
    Replace with real transformation logic.
    """
    return grid

if __name__ == "__main__":
    import json, sys
    path = "data/task001.json" if len(sys.argv) < 2 else sys.argv[1]

    with open(path) as f:
        task = json.load(f)

    for i, pair in enumerate(task["train"]):
        output = solve(pair["input"])
        print(f"Example {i+1} -> {'✅' if output == pair['output'] else '❌'}")
