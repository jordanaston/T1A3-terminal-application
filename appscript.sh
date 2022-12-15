#! /bin/bash
echo "Thank you for downloading PlantApp."
sleep 2
if ! [[ -x "$(command -v python3)" ]]
then
    echo "You'll need Python 3 installed to run PlantApp. Head to https://www.python.org/downloads/ to download Python. Once you've installed Python 3, re run this script."
fi    
sleep 2
echo "Let's create the virtual environment!"
python3 -m venv venv
echo "Let's activate the virtual environment!"
source venv/bin/activate
sleep 2
echo "Now we'll install the dependancies required to run PlantApp."
pip install -r requirements.txt
sleep 2
echo "Now we can run PlantApp."
sleep 2
python3 plantapp.py

