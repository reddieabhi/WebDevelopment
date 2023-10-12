
echo "BUILD START"
python3.10.0 -m pip install -r requirements.txt
python3.10.0 manage.py collecstatic --noinput --clear
echo "BUILD END"
