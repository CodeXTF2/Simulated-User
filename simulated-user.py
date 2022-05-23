
import json
import time
import random
import routines
print("[*] User routines loaded")
configfile = "hr.json" #Put the profile of the simulated user here
count = 5
#Load and parse the config
config = json.loads(open(configfile,"r").read())
print(json.dumps(config, indent=4, sort_keys=True))
routines.spreadsheets()
#Build the user routine
cycle = []
for x in config["routines"].keys():
    for y in range(config["routines"][x]):
        cycle.append(getattr(routines,x))
print("[*] Action list generated")
print("[*] Simulated user starting up with config " + configfile)
for x in range(count):
    #Start the routines!


    random.shuffle(cycle)
    for x in cycle:
        x()
        time.sleep(random.randint(config["interval"][0],config["interval"][1]) / 1000)
    print("[*] Cycle complete - shuffling cycle")