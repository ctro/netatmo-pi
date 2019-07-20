#!/bin/bash

# netatmo-api hits the api and writes a .json file
cd netatmo-api && ruby write_api_response.rb

# papirus-display reads the .json file and displays it nicely
cd ../papirus-display
python refresh.py
