from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "fallback_local_key_only")

@app.route("/", methods=["GET", "POST"])
def index():
    # SETUP: If it's a new game, generate the number
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)
        session["attempts"] = 0
        message = "I'm thinking of a number between 1 and 100. Make a guess!"
        return render_template("index.html", message=message)

    # GAMEPLAY: If the user submitted a form (POST request)
    if request.method == "POST":
        try:
            guess = int(request.form.get("guess"))
            session["attempts"] += 1
            
            if guess < session["secret_number"]:
                message = f"Too low! Try again. (Attempts: {session['attempts']})"
            elif guess > session["secret_number"]:
                message = f"Too high! Try again. (Attempts: {session['attempts']})"
            else:
                message = f"Correct! You got it in {session['attempts']} attempts. I've picked a new number, play again!"
                session.pop("secret_number") 
                
        except ValueError:
            message = "Please enter a valid number."
            
        return render_template("index.html", message=message)

    # THE FIX: Catch-all for simple GET requests (like refreshing the page)
    message = f"Game is active! Enter your next guess. (Attempts: {session['attempts']})"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)