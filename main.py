from flask import Flask, render_template_string, request
from scipy.optimize import linprog

app = Flask(__name__)

# Simple HTML template
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>LPP Solver</title>
</head>
<body>
    <h2>Linear Programming Solver (Simplex)</h2>
    <form method="post">
        <label>Objective Coefficients (comma separated):</label><br>
        <input type="text" name="c" value="3,2"><br><br>

        <label>Inequality Coefficients (rows separated by ;):</label><br>
        <input type="text" name="A" value="1,2;4,0;0,4"><br><br>

        <label>Inequality Bounds (comma separated):</label><br>
        <input type="text" name="b" value="8,16,12"><br><br>

        <button type="submit">Solve</button>
    </form>

    {% if result %}
        <h3>Result:</h3>
        <p>Status: {{ result['status'] }}</p>
        <p>Optimal Value: {{ result['fun'] }}</p>
        <p>Decision Variables: {{ result['x'] }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def solve():
    result = None
    if request.method == "POST":
        c = [float(i) for i in request.form["c"].split(",")]
        A = [list(map(float, row.split(","))) for row in request.form["A"].split(";")]
        b = [float(i) for i in request.form["b"].split(",")]

        res = linprog(c=c, A_ub=A, b_ub=b, method="highs")

        result = {
            "status": res.message,
            "fun": res.fun,
            "x": res.x.tolist()
        }

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
