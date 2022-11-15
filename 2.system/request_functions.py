import requests

def checkPlate(plate):
    url = 'https://tcc-parking-iot.herokuapp.com/plates/find-by-name-or-save?plateNumber='+str(plate)
    x = requests.get(url)
    return x.text

def checkSpot(spot_id):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots/'+str(spot_id)
    x = requests.get(url)
    return x.text

def setParkingSpotStatus(spot_id, spot_status, plate = None):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots/set-parking-spot-available/'+str(spot_id)
    myobj = {
        "name": spot_name
    }
    x = requests.post(url, json = myobj)
    return x.text

def createNewParkingSpot(spot_name):
    url = 'https://tcc-parking-iot.herokuapp.com/parking-spots'
    myobj = {
        "name": spot_name
    }
    x = requests.post(url, json = myobj)
    return x.text