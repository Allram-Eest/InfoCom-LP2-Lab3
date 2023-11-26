import math
import requests
import argparse


step_length = 0.00003

def distanceBetweenPoints(start_coords, end_coords):
    return math.sqrt((end_coords[0]-start_coords[0])**2+(end_coords[1]-start_coords[1])**2)
#Write you own function that moves the dron from one place to another 
#the function returns the drone's current location while moving
#====================================================================================================
def travel(current_coords, to_coords):
    distance = distanceBetweenPoints(current_coords, to_coords)
    angle = math.atan2((to_coords[1]-current_coords[1]),(to_coords[0]-current_coords[0]))
    steps = round(distance/step_length)
    for x in range(steps):
        current_coords = move(current_coords, math.cos(angle)*step_length, math.sin(angle)*step_length)
        with requests.Session() as session:
            drone_location = {'longitude': current_coords[0],
                              'latitude': current_coords[1]
                        }
            resp = session.post(SERVER_URL, json=drone_location)
#====================================================================================================


def move(coords, dx, dy):
    return (coords[0]+dx, coords[1] + dy)

def run(current_coords, from_coords, to_coords, SERVER_URL):
    # Compmelete the while loop:
    # 1. Change the loop condition so that it stops sending location to the data base when the drone arrives the to_address
    # 2. Plan a path with your own function, so that the drone moves from [current_address] to [from_address], and the from [from_address] to [to_address]. 
    # 3. While moving, the drone keeps sending it's location to the database.
    #====================================================================================================
    travel(current_coords, from_coords)
    travel(from_coords, to_coords)
  #====================================================================================================

   
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    print(current_coords)
    print(from_coords)
    print(to_coords)

    run(current_coords, from_coords, to_coords, SERVER_URL)
