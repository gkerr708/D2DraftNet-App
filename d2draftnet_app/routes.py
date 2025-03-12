from flask import Blueprint, render_template, request, jsonify
from d2draftnet_app.config import HEROS
from d2draftnet_app.load_model import predict_match_outcome


main = Blueprint("main", __name__)

@main.route("/")
def home():
    """Render the homepage with the hero selection grid."""
    return render_template("index.html", heroes=HEROS)

@main.route("/predict", methods=["POST"])
def predict():
    """Process the draft and return a prediction result."""
    radiant_draft = request.form.get("radiant_draft", "").split(",")
    dire_draft = request.form.get("dire_draft", "").split(",")

    # Standardize hero names
    radiant_draft = [hero.replace("_", " ").title() for hero in radiant_draft]
    dire_draft = [hero.replace("_", " ").title() for hero in dire_draft]

    # Special case: Fix "natures prophet" to "Nature's Prophet"
    radiant_draft = ["Nature's Prophet" if hero.lower() == "natures prophet" else hero for hero in radiant_draft]
    dire_draft = ["Nature's Prophet" if hero.lower() == "natures prophet" else hero for hero in dire_draft]

    # Call the prediction model
    prediction = predict_match_outcome(radiant_draft, dire_draft)
    winner = "Radiant" if prediction > 0.5 else "Dire"
    confidence = round(prediction if prediction > 0.5 else 1 - prediction, 2)

    # Response message
    response_text = (
        f"Predicted Winner: {winner} (Confidence: {confidence:.2f})"
    )

    return jsonify({"message": response_text})
