# XCS224N NLP Python Sandbox

A scratch environment for experimenting with PyTorch and NumPy.

## Setup

This project uses the virtual environment at `/Users/George/PY/.venv`.

VSCode is configured to use it automatically via `.vscode/settings.json`.

## Running

Open `test_torch.py` and press the Run button, or:

```bash
/Users/George/PY/.venv/bin/python test_torch.py
```

## Contents

`test_torch.py` demonstrates:

- Random tensor generation with PyTorch
- Basic loops and printing
- NumPy array creation
- Matrix multiplication with `torch.matmul`
- Plotting `exp(x)` over an array using matplotlib
- Numerical differentiation of `exp(x)` using `np.diff`, plotted alongside the original
