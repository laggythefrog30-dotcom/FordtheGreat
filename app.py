from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

ARTISTS = [
    {
        "id": "W",
        "letter": "W",
       
        "quote": "Wounds inside don't heal unless you face them.",
        "color": "#e05c2a",
        "image": "w.jpg",
        "audio": "w.mp3",
   
    },
    {
        "id": "E",
        "letter": "E",
      
        "quote": "Every fear grows stronger when you feed it.",
        "color": "#0d7ea8",
        "image": "e.jpg",
        "audio": "e.mp3",
      
    },
    {
        "id": "N",
        "letter": "N",
        
        "quote": "Not everything that feels normal is truly healthy.",
        "color": "#3a86b8",
        "image": "n.jpg",
        "audio": "n.mp3",
      
    },
]

@app.route("/")
def home():
    return render_template("index.html", artists=ARTISTS)

@app.route("/me/<artist_id>")
def artist(artist_id):
    artist = next((a for a in ARTISTS if a["id"] == artist_id), None)
    if not artist:
        return "Not found", 404
    others = [a for a in ARTISTS if a["id"] != artist_id]
    return render_template("me.html", artist=artist, others=others)

@app.route("/static/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(os.path.join(app.root_path, "static/audio"), filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
