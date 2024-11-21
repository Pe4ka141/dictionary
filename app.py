from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pe4ka11:1P2P3P4p!@localhost/dictionary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Word model
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False, unique=True)
    translation = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# Route: Home (Add Words)
@app.route('/')
def home():
    return render_template('index.html')

# Route: Add Word
@app.route('/add', methods=['POST'])
def add_word():
    word = request.form.get('word')
    translation = request.form.get('translation')

    if not word or not translation:
        return jsonify({"error": "Word and translation are required."}), 400

    # Check if word already exists
    existing_word = Word.query.filter_by(word=word).first()
    if existing_word:
        return jsonify({"error": "Word already exists in the dictionary."}), 409

    # Add word to database
    new_word = Word(word=word, translation=translation)
    db.session.add(new_word)
    db.session.commit()

    return jsonify({"message": "Word added successfully!"})

# Route: Search Word
@app.route('/search', methods=['GET'])
def search_word():
    query_word = request.args.get('word')  # Get the word from the query parameters
    if not query_word:
        return jsonify({"error": "Please provide a word to search for."}), 400

    # Query the database for the word
    word_entry = Word.query.filter_by(word=query_word).first()

    if word_entry:
        return jsonify({
            "word": word_entry.word,
            "translation": word_entry.translation,
            "date_added": word_entry.date_added
        })
    else:
        return jsonify({"error": "Word not found in the dictionary."}), 404

# Ensure tables are created
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    # Run the app publicly
    app.run(host='0.0.0.0', port=5000, debug=True)
