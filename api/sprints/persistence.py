import os
import json

from ..teams.repository import get_team_by_id
from .common import create_sprint_dict

SPRINTS_FILE = "data/sprints.json"

os.makedirs("data", exist_ok=True)
if not os.path.exists(SPRINTS_FILE):
    file = open(SPRINTS_FILE, "a")
    file.write("[]")
    file.close()

# dict layout
# {
#   "id": id da sprint
#   "team_id": id do time dono dessas sprints
#   "status": aberta/fechada
# }

def write_sprints(sprints):
    file = open(SPRINTS_FILE, "w")
    file.write(json.dumps([
        {
            "id": sprint["id"],
            "team_id": sprint["team"]["id"],
            "name": sprint["name"],
            "status": sprint["status"]
        }
        for sprint in sprints
    ]))
    file.close()

def read_sprints():
    file = open(SPRINTS_FILE, "r")
    content = file.read()
    sprints = json.loads(content)
    file.close()
    sprints = [
        create_sprint_dict(
            sprint["id"],
            get_team_by_id(sprint["team_id"]),
            sprint["name"],
            sprint["status"]
        )
        for sprint in sprints
    ]
    return sprints
