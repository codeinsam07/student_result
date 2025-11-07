from flask import Flask, render_template, request

app = Flask(__name__)

# 30 students ka record dictionary me (sample)
students = {
    "101": {"name": "Amit", "marks": 85},
    "102": {"name": "Ravi", "marks": 78},
    "103": {"name": "Priya", "marks": 92},
    "104": {"name": "Suman", "marks": 66},
    "105": {"name": "Anjali", "marks": 90},
    "106": {"name": "Rahul", "marks": 55},
    "107": {"name": "Neha", "marks": 88},
    "108": {"name": "Deepak", "marks": 60},
    "109": {"name": "Rohit", "marks": 71},
    "110": {"name": "Sita", "marks": 69},
    "111": {"name": "Manoj", "marks": 95},
    "112": {"name": "Nisha", "marks": 48},
    "113": {"name": "Rakesh", "marks": 77},
    "114": {"name": "Ankit", "marks": 89},
    "115": {"name": "Sonal", "marks": 73},
    "116": {"name": "Vikas", "marks": 58},
    "117": {"name": "Arjun", "marks": 82},
    "118": {"name": "Pooja", "marks": 64},
    "119": {"name": "Mohan", "marks": 56},
    "120": {"name": "Sneha", "marks": 93},
    "121": {"name": "Karan", "marks": 75},
    "122": {"name": "Meena", "marks": 68},
    "123": {"name": "Ritu", "marks": 84},
    "124": {"name": "Asha", "marks": 91},
    "125": {"name": "Ravi Kumar", "marks": 57},
    "126": {"name": "Harsh", "marks": 79},
    "127": {"name": "Shivani", "marks": 87},
    "128": {"name": "Vivek", "marks": 62},
    "129": {"name": "Pankaj", "marks": 74},
    "130": {"name": "Anita", "marks": 81}
}

@app.route("/", methods=["GET", "POST"])
def index():
    results = []      # list of matched students (each: dict with roll,name,marks,status)
    message = None

    if request.method == "POST":
        roll = request.form.get("roll", "").strip()
        name = request.form.get("name", "").strip()

        # Agar roll diya gaya hai, roll se exact search karein (preferred)
        if roll:
            student = students.get(roll)
            if student:
                marks = student["marks"]
                status = "Pass" if marks >= 40 else "Fail"
                results.append({"roll": roll, "name": student["name"], "marks": marks, "status": status})
            else:
                message = f"Roll number {roll} ka record nahi mila."
        # Agar roll nahi diya aur name diya gaya, to name (partial, case-insensitive) search karein
        elif name:
            q = name.lower()
            for r, info in students.items():
                if q in info["name"].lower():
                    marks = info["marks"]
                    status = "Pass" if marks >= 40 else "Fail"
                    results.append({"roll": r, "name": info["name"], "marks": marks, "status": status})
            if not results:
                message = f"Naam '{name}' ke liye koi record nahi mila."
        else:
            message = "Kripya Roll number ya Naam me se koi ek daaliye."

    return render_template("index.html", results=results, message=message)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

