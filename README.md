# Pandemic-Volunteer-App
🏥 During the times of the pandemic and the lockdown in our homes, back in 2020, we saw many initiatives from people trying to help in any way they could. 

Some people already had it in their profession. They were doctors, nurses, paramedics, psychologists. Others, like us engineers🧑‍🔧, found it more difficult to contribute to the situation. 

In this repository I want to share a small project that I carried out in my community and that was supported by our beloved Python🐍.

Since people's movements were very limited, the purpose was to create a database with the exact locations of each of the people willing to help their neighbours, as well as those neighbours requesting some kind of support, so that we could put in contact those Volunteer/requester pairs geographically close.

We created a network of volunteers, which you could join by simply filling in a form that we distributed by Whatsapp. From there, I developed a very simple App in Python that allowed me to access the data hosted in Google Sheets from the form and, through a google geolocator, generate a map that allowed me to know, in a very visual way, which volunteers were closer to the applicant. Finally, I would contact both parties and arrange an appointment. In this way, we did the shopping, took out the rubbish, walked dogs and brought medicine and food to more than 50 people in our community.

I just wanted to share the code here for my personal record. It is very simple, a probably full of possible improvements. It worked though, and I am really proud of it.

Very grateful to all the volunteers and to the power of Python🐍.

Some guidelines:

## 1. main.py
  It allows initiating the main GUI. It requires data.py and map.py to be useful.
## 2. data.py 
  Contains the GUI code and other methods necessary to load the data from Google into the App.
## 3. map.py
  Contains the GUI code for the Map.
## 4. google_functions.py
  Methods to initiate Google Oauth services and get the data from Google Sheets
## 5. geofunctions.py
  Initiates geocoder from Google to find the coordinates upon the different addresses loaded in the DataFrame.
## 6. browser.py
  It draws the new map once the different coordinates have been calculated by the geocoder.


See for the API_key
https://developers.google.com/workspace/guides/create-credentials?hl=es-419