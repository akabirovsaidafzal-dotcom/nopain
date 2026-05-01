from flask import Flask, render_template

app = Flask(__name__)

team_members = {
    "brand-face": {
        "name": "Co-Founder / Brand Face",
        "photo": "team/director.jpg",
        "role": "Brand identity, public face and creative positioning.",
        "bio": "Responsible for how NOPAIN is seen, remembered and trusted. Builds the image, tone and emotional presence of the brand.",
        "skills": ["Brand Face", "Creative Direction", "Public Image", "Content Presence"]
    },
    "videographer": {
        "name": "CEO / Videographer",
        "photo": "team/videographer.jpg",
        "role": "Direction, camera, lighting and cinematic execution.",
        "bio": "Leads the production process from visual planning to shooting. Focuses on movement, light, composition and premium visual quality.",
        "skills": ["Video Production", "Camera Work", "Lighting", "Visual Direction"]
    },
    "editor": {
        "name": "CEO / Editor",
        "photo": "team/editor.jpg",
        "role": "Editing, rhythm, storytelling and final impact.",
        "bio": "Turns raw footage into emotional, high-retention content. Controls pacing, hooks, sound, color and final polish.",
        "skills": ["Editing", "Storytelling", "Color", "Retention"]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/team/<member_id>")
def member(member_id):
    person = team_members.get(member_id)
    if not person:
        return "Member not found", 404
    return render_template("member.html", person=person)

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
