from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

CSV_FILE = "scraped_books.csv"

@app.route("/", methods=["GET"])
def index():
    df = pd.read_csv(CSV_FILE)

    # Get sorting and filtering options from request
    sort_by = request.args.get("sort_by")
    filter_rating = request.args.get("rating")
    filter_availability = request.args.get("availability")

    # Clean the Price column
    df["Price (£)"] = df["Price (£)"].str.replace("Â£", "£").str.replace("£", "").astype(float)

    # Filtering
    if filter_rating:
        df = df[df["Rating"] == filter_rating]
    if filter_availability:
        df = df[df["Availability"].str.contains(filter_availability, case=False)]

    # Sorting
    if sort_by == "price_asc":
        df = df.sort_values(by="Price (£)", ascending=True)
    elif sort_by == "price_desc":
        df = df.sort_values(by="Price (£)", ascending=False)
    elif sort_by == "rating_asc":
        df = df.sort_values(by="Rating", ascending=True)
    elif sort_by == "rating_desc":
        df = df.sort_values(by="Rating", ascending=False)

    return render_template("index.html", books=df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
