import os
from datetime import datetime

from flask import Flask, render_template, request, url_for
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Mapi za nalaganje in generiranje slik
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, "static")
GENERATED_FOLDER = os.path.join(STATIC_FOLDER, "generated")

os.makedirs(GENERATED_FOLDER, exist_ok=True)


def create_meme(image_path, top_text, bottom_text):
    """Naložim sliko, dodam tekst in vrnem ime nove datoteke."""
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Privzeti font
    font_size = int(img.height / 12)
    font = ImageFont.load_default()

    # Tekst v upper-case
    top_text = (top_text or "").upper()
    bottom_text = (bottom_text or "").upper()

    def draw_centered_text(text, y):
        if not text:
            return
        # Najprej sem uporabil textsize samo, ker več ne obstaja sem uporabil textbox
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (img.width - text_width) / 2
        draw.text((x, y), text, fill="black", font=font)

    # Zgornji tekst
    draw_centered_text(top_text, y=10)

    # Spodnji tekst
    bottom_y = img.height - font_size * 2
    draw_centered_text(bottom_text, y=bottom_y)

    # Ime nove datoteke
    filename = f"meme_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    output_path = os.path.join(GENERATED_FOLDER, filename)
    img.save(output_path, format="JPEG")

    return filename



@app.route("/", methods=["GET"])
def index():
    # Prvi prikaz strani: samo obrazec
    return render_template("index.html", meme_url=None)


@app.route("/generate", methods=["POST"])
def generate():
    # Prejme podatke iz HTML obrazca
    image_file = request.files.get("image")
    top_text = request.form.get("top_text", "")
    bottom_text = request.form.get("bottom_text", "")

    if not image_file:
        return render_template(
            "index.html",
            meme_url=None,
            error="Naloži sliko, prosim."
        )

    # Začasno shranim naloženo sliko v formatu jpg
    temp_filename = f"upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    temp_path = os.path.join(GENERATED_FOLDER, temp_filename)
    image_file.save(temp_path)

    # Ustvarim meme
    meme_filename = create_meme(temp_path, top_text, bottom_text)


    meme_url = url_for("static", filename=f"generated/{meme_filename}")
    return render_template("index.html", meme_url=meme_url, error=None)


if __name__ == "__main__":
    # V Dockerju mora teči na 0.0.0.0 in portu iz okolja
    port = int(os.environ.get("PORT", 5556))
    app.run(host="0.0.0.0", port=port, debug=True)
