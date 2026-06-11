# Installation Guide

Detailed instructions to configure the development environment for the Keplerian Orbital Dynamics Laboratory.

---

## Prerequisites

Ensure you have the following installed:
- Python 3.9+ (Check via `python --version`)
- pip 21.0+ (Check via `pip --version`)
- Git 2.0+ (Check via `git --version`)

---

## 1. Installation via pip and venv (Recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/gnss-orbital-py.git
cd gnss-orbital-py
```

### Step 2: Create a Virtual Environment

#### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
*Note: If you receive an execution policy error on Windows PowerShell, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`*

#### Windows (CMD)
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

#### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Upgrade pip and Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -e .
```
*Note: Installing with `-e .` (editable mode) registers the `orbital` package so it can be imported anywhere inside the virtual environment.*

### Step 4: Launch JupyterLab
```bash
jupyter lab
```

---

## 2. Alternative Installation via Conda

### Step 1: Create the Conda Environment
```bash
conda create -n orbital python=3.11 -y
conda activate orbital
```

### Step 2: Install Package in Editable Mode
```bash
pip install -e .
```

### Step 3: Register the Jupyter Kernel
```bash
python -m ipykernel install --user --name=orbital --display-name="Python (Orbital)"
```

---

## 3. Verification

To verify that the installation succeeded and all package imports are correct, run:

```bash
python -c "import orbital; print('orbital package version:', orbital.__version__ if hasattr(orbital, '__version__') else 'installed')"
```

And run the test suite:
```bash
python -m pytest tests/ -v
```

---

## 4. Troubleshooting Common Issues

### Plotly figures do not load in JupyterLab
Install the ipywidgets extension support for JupyterLab:
```bash
pip install "ipywidgets>=8.0" jupyterlab
```
Then refresh the JupyterLab page.

### Execution Policy Error on Windows
Open PowerShell as administrator and run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then reactivate the virtual environment.
