import requests
from datetime import datetime, timedelta
from random import randint

def checkPlate(plate):
    url = 'https://tcc-parking-iot.herokuapp.com/plates/find-by-name-or-save?plateNumber='+str(plate)
    x = requests.get(url)
    return x.text

def checkSpot(spot_id):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots/'+str(spot_id)
    x = requests.get(url)
    return x.text

def listParkingSpots():
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots'
    x = requests.get(url)
    return x.text

def setParkingSpotStatusAvailable(spot_id):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots/set-parking-spot-status/'+str(spot_id)
    x = requests.put(url)
    return x.text

def setParkingSpotStatusUnavailable(spot_id, plate_number):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots/ocuppy-parking-spot-and-save-plate/'+str(spot_id)
    myobj = {
            "plate":{
                "plateNumber":plate_number
            }
        }
    x = requests.put(url, json = myobj)
    return x.text

def getCurrentRental(plate_number):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-rentals/find-by-plate-end-date-null?plateNumber={}'.format(plate_number)
    x = requests.get(url)
    return x.text

def openNewRental(plate_number, parking_spot):
    start_datetime = datetime.today().strftime('%Y-%m-%dT%H:%M:%S')    
    url = 'https://tcc-parking-iot.herokuapp.com/parking-rentals/{}/{}'.format(parking_spot, plate_number)
    myobj = {
       "startDate": start_datetime
    }
    x = requests.post(url, json = myobj)
    return x.text  
        
def closeRental(plate_number):   
    try:
        rental_id = json.loads(getCurrentRental(plate_number))[0]['id']
    except:
        rental_id = None
    
    if rental_id:
        end_datetime = (datetime.today() + timedelta(hours=randint(1, 3))).strftime('%Y-%m-%dT%H:%M:%S')     
        url = 'https://tcc-parking-iot.herokuapp.com/parking-rentals/set-end-date/{}'.format(rental_id)
        myobj = {
            "endDate": end_datetime
        }
        x = requests.put(url, json = myobj)
        return x.text
       