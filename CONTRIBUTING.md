# Contributing Guide

Thank you for your interest in contributing to the Keplerian Orbital Dynamics Interactive Laboratory.

This guide outlines the development workflow and coding conventions for the project.

---

## 1. Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you agree to maintain a respectful, inclusive, and constructive environment.

---

## 2. Setting Up Your Development Environment

### Step 1: Fork and Clone
1. Fork the repository at `https://github.com/your-username/gnss-orbital-py`.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/gnss-orbital-py.git
   cd gnss-orbital-py
   ```

### Step 2: Configure Remotes
```bash
git remote add upstream https://github.com/your-username/gnss-orbital-py.git
```

### Step 3: Create a Virtual Environment and Install
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -e .
```

---

## 3. Git Workflow

1. Sincronize your fork with upstream:
   ```bash
   git checkout main
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git add file_modified.py
   git commit -m "feat: add J2 perturbation model to propagation strategy"
   ```

### Branch Naming Conventions
- `feature/` - New features (e.g., `feature/hohmann-transfer`)
- `fix/` - Bug fixes (e.g., `fix/kepler-convergence`)
- `docs/` - Documentation changes (e.g., `docs/api-ref-update`)
- `test/` - Adding/updating tests (e.g., `test/solver-edge-cases`)
- `refactor/` - Code refactoring (e.g., `refactor/plotter-template`)

---

## 4. Coding Conventions (PEP 8)

All Python code must follow the PEP 8 style guide.

### Basic Rules
- **Indentation**: 4 spaces (no tabs).
- **Line Length**: Max 88 characters (Black code formatter standard).
- **Naming Conventions**:
  - Variables & Functions: `snake_case` (e.g., `solve_kepler_equation`, `semi_major_axis`)
  - Classes: `PascalCase` (e.g., `OrbitalPropagator`, `KeplerianPropagation`)
  - Constants: `UPPER_SNAKE_CASE` (e.g., `MU_EARTH`, `EARTH_RADIUS`)
- **Emojis**: Emojis are strictly forbidden in comments, docstrings, variable names, and code output. Emojis must only be used in metadata badges or achievements where explicitly required.

### Docstring Format
All docstrings must be written in English using the NumPy/SciPy docstring convention:

```python
def solve_kepler_equation(
    M: numpy.typing.ArrayLike,
    e: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> numpy.ndarray:
    """Solves Kepler's equation using the Newton-Raphson method.

    Args:
        M: Mean anomaly in radians.
        e: Orbital eccentricity (0 <= e < 1).
        tol: Convergence tolerance.
        max_iter: Maximum number of iterations.

    Returns:
        Eccentric anomaly in radians.

    Raises:
        ValueError: If eccentricity or numerical parameters are invalid.
        ConvergenceError: If Newton-Raphson fails to converge.
    """
    pass
```

---

## 5. Submitting a Pull Request

1. Ensure the test suite passes:
   ```bash
   python -m pytest tests/
   ```
2. Verify mypy strict type checking:
   ```bash
   python -m mypy orbital/ --strict
   ```
3. Push changes to your fork and open a Pull Request against the `main` branch of the upstream repository.
