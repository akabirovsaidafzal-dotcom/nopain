from flask import Flask, render_template, abort

app = Flask(__name__)

TEAM_MEMBERS = {
    "brand-face": {
        "name": "Brand Face",
        "role": "Co-Founder / Brand Face",
        "photo": "team/director.jpg",
        "bio": "NOPAIN brendining ommaviy yuzi, ishonchli obrazi va kommunikatsiya yo‘nalishini shakllantiradi. Brend xabari aniq, do‘stona va esda qoladigan bo‘lishi uchun ishlaydi.",
        "skills": [
            "Brand presence",
            "Public image",
            "Client trust",
            "Story delivery"
        ]
    },
    "videographer": {
        "name": "Videographer",
        "role": "CEO / Videographer",
        "photo": "team/videographer.jpg",
        "bio": "Kamera, yorug‘lik, harakat va cinematic kadrlar orqali biznes hikoyasini professional vizualga aylantiradi. Jarayonni mijoz uchun oson, stressiz va aniq qiladi.",
        "skills": [
            "Cinematic shooting",
            "Lighting setup",
            "Production direction",
            "Visual storytelling"
        ]
    },
    "editor": {
        "name": "Editor",
        "role": "CEO / Editor",
        "photo": "team/editor.jpg",
        "bio": "Xom materialni ritm, retention, hissiyot va aniq xabarga ega yakuniy kontentga aylantiradi. Har bir video scrollni to‘xtatish va ishonch yaratish uchun yig‘iladi.",
        "skills": [
            "Video editing",
            "Retention rhythm",
            "Story structure",
            "Final impact"
        ]
    }
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/team/<slug>")
def member(slug):
    person = TEAM_MEMBERS.get(slug)
    if not person:
        abort(404)
    return render_template("member.html", person=person)


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
