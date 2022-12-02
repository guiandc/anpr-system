import requests

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

def createNewParkingSpot(spot_name):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots'
    myobj = {
        "name": spot_name
    }
    x = requests.post(url, json = myobj)
    return x.text

def rentalParkingSpot():
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots/set-parking-spot-status/'+str(spot_id)
    myobj = {
        "plate": {
            "plateNumber": "aaa-1230"
        },
        "startDate": "",
        "endDate": None
    }
    x = requests.post(url, json = myobj)
    return x.text