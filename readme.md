# LPP Solver (Flask + Simplex)

A simple Linear Programming Problem solver using **Flask** and **SciPy**.

## 🚀 Deployment
1. Push this folder to GitHub.
2. Deploy to [Render](https://render.com).
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## 🧮 Example
- Objective: Maximize `3x + 2y`
- Constraints:
  - `x + 2y ≤ 8`
  - `4x ≤ 16`
  - `4y ≤ 12`
