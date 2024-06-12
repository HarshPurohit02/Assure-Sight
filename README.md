# Assure-Sight
Assure Sight is a security system that utilizes computer vision to detect human presence and sends an alert notification via SMS. This project leverages OpenCV for image processing and the Twilio API for sending SMS alerts.

# Install dependencies: 
Make sure you have Python installed. Then, install the required packages:
pip install opencv
pip install cvzone
pip install twilio

# Setup Twillo
Sign up for a Twilio account.
Get your Account SID and Auth Token from the Twilio Console.
Replace the placeholder values in send.py with your Twilio credentials and phone numbers.

# Run the main script to start the human detection and alert system:
main.py

# Project Structure
main.py: The main script that handles video capture, human detection, and triggering SMS alerts.
send.py: A helper script that integrates with the Twilio API to send SMS alerts.
