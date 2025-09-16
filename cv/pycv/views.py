from django.shortcuts import render
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

def cv_view(request):
    file = BASE_DIR / "pycv" / "cv.json"
    if file.exists():
        with open (file, "r") as f:
            cv = json.load(f)
    
    else:
        cv = {"name":"import your CV first!",
              "email":"blank",
              "phone":"blank",
              "links":[],
              "education":[],
              "skills":{},
              "experience":[],
              "projects":[]}
        
    return render(request, "cv.html", {"cv": cv})