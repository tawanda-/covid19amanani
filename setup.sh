python3 venv venv
. /venv/bin/activate
pip3 install -r backend/api/requirements.txt
cd backend
flask init-db
flask get-data -latest
flask get-data -vaccine
flask run