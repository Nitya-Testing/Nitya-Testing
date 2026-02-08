from datetime import datetime, timezone
from github import Github
import svgwrite
import os

g = Github(os.environ["GITHUB_TOKEN"])
user = g.get_user("NityaRanjan")

events = user.get_events()
last_push = None

for event in events:
    if event.type == "PushEvent":
        last_push = event.created_at
        break

dwg = svgwrite.Drawing("consistency-status.svg", size=("900px", "80px"))

if last_push is None:
    message = "Nitya, start committing today. Small steps matter."
    color = "#f39c12"
else:
    days_inactive = (datetime.now(timezone.utc) - last_push).days

    if days_inactive > 2:
        message = (
            "Nitya, you are going to your comfort zone again... "
            "Focus on your Goals and keep trying."
        )
        color = "#e74c3c"
    else:
        message = "Nitya you are good going."
        color = "#2ecc71"

# Background
dwg.add(dwg.rect(insert=(0, 0), size=("100%", "100%"), fill="#0d1117"))

# Text
dwg.add(
    dwg.text(
        message,
        insert=(20, 50),
        fill=color,
        font_size="26px",
        font_family="Verdana"
    )
)

dwg.save()
