# MyContactsApp

## Installation

This is a Python application, based on Streamlit. To install it, you need to have Python installed on your system.

```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt
```

## Untertitel
Demo für BMLD Informatik 2

## To Do

- Would be nice to have all options in the sidebar 
  - before login -> login / register
  - After login: logout button and pages in pages
  - **Or:** Hide sidebar during login! 
- testapp.py auschecken
- LoginManager funktioniert
- Muss noch angepasst werden für Multi Page App -> gelöst mit go_home methode
- DataManager muss getestet werden
- MyContacts App anpassen
- DataManger -> Zusammenfügen mit meinen Methoden in github_contents. github_contents im original belassen...
- Es ist anscheinend möglich, die Sidebar zu überschreiben wenn man nicht eingeloggt ist... 
  - May be use https://github.com/victoryhb/streamlit-option-menu
  - This student managed (I don't know how): https://github.com/deliriumastrae/dvor_osm_projekt
  - Probable best would be: https://github.com/blackary/st_pages  