# Convert CV to HTML using Django
This project converts my CV to an HTML page using **Django templates**. 
The CV data is in `cv/pycv/cv.json` and is displayed using `cv/pycv/templates/cv.html`. 

## Setup

``` bash
# Clone the repo
git clone https://github.com/zeepxnflrp/django-cv.git
cd django-cv/cv

# Create and activate virtual environment
python -m venv .env
source .env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the CV.