import twint 
import os
import json
import datetime
from time import sleep


path = os.path.abspath(__file__)
NoraCop_full_path = path.replace('main.py', "NoraCop.json")
NurikAIO_full_path = path.replace('main.py', "NurikAIO.json")
vision_aio_full_path = path.replace('main.py', "vision_aio.json")
_7MSe1523NJtYp6j_full_path = path.replace('main.py', "A7MSe1523NJtYp6j.json")
cmd_root_full_path = path.replace('main.py', "cmd_root.json")
EnigmaRobotic_full_path = path.replace('main.py', "EnigmaRobotic.json")

    #Scraping NoraCop
NoraCop_scrap = twint.Config()
NoraCop_scrap.Store_json = True
NoraCop_scrap.Output = NoraCop_full_path# <= Destination of json file 
NoraCop_scrap.Username = 'NoraCop'# <= Name of Parsed account

    #Scraping Nurik
NurikAIO_scrap = twint.Config()
NurikAIO_scrap.Store_json = True
NurikAIO_scrap.Output = NurikAIO_full_path# <= Destination of json file 
NurikAIO_scrap.Username = 'NurikAIO'# <= Name of Parsed account

    #Scraping NoraCop
vision_aio_scrap = twint.Config()
vision_aio_scrap.Store_json = True
vision_aio_scrap.Output = vision_aio_full_path# <= Destination of json file 
vision_aio_scrap.Username = 'vision_aio'# <= Name of Parsed account

    #Scraping NoraCop
_7MSe1523NJtYp6j_scrap = twint.Config()
_7MSe1523NJtYp6j_scrap.Store_json = True
_7MSe1523NJtYp6j_scrap.Output = _7MSe1523NJtYp6j_full_path# <= Destination of json file 
_7MSe1523NJtYp6j_scrap.Username = '7MSe1523NJtYp6j'# <= Name of Parsed account

    #Scraping cmd_root
cmd_root_scrap = twint.Config()
cmd_root_scrap.Store_json = True
cmd_root_scrap.Output = cmd_root_full_path# <= Destination of json file 
cmd_root_scrap.Username = 'cmd_root'# <= Name of Parsed account

    #Scraping EnigmaRobotic
EnigmaRobotic_scrap = twint.Config()
EnigmaRobotic_scrap.Store_json = True
EnigmaRobotic_scrap.Output = EnigmaRobotic_full_path# <= Destination of json file 
EnigmaRobotic_scrap.Username = 'EnigmaRobotic'# <= Name of Parsed account

while True:
    #Recreat json files

    file = open(cmd_root_full_path, 'r+')
    file.truncate(0)
    file.close()

    file = open(_7MSe1523NJtYp6j_full_path, 'r+')
    file.truncate(0)
    file.close()

    file = open(vision_aio_full_path, 'r+')
    file.truncate(0)
    file.close()

    file = open(EnigmaRobotic_full_path, 'r+')
    file.truncate(0)
    file.close()

    file = open(NurikAIO_full_path, 'r+')
    file.truncate(0)
    file.close()

    file = open(NoraCop_full_path, 'r+')
    file.truncate(0)
    file.close()


  

    # Get time from where to start

    in_miliseconds_2_min_ago = datetime.datetime.now() - datetime.timedelta(minutes=2)
    two_min_ago = in_miliseconds_2_min_ago.strftime("%Y-%m-%d %H:%M:%S")
    cmd_root_scrap.Since = str(two_min_ago)
    NoraCop_scrap.Since = str(two_min_ago)
    NurikAIO_scrap.Since = str(two_min_ago)
    vision_aio_scrap.Since = str(two_min_ago)
    _7MSe1523NJtYp6j_scrap.Since = str(two_min_ago)
    EnigmaRobotic_scrap.Since = str(two_min_ago)
    #Start scraping

    twint.run.Search(cmd_root_scrap)
    twint.run.Search(vision_aio_scrap)
    twint.run.Search(_7MSe1523NJtYp6j_scrap)
    twint.run.Search(NurikAIO_scrap)
    twint.run.Search(NoraCop_scrap)
    twint.run.Search(EnigmaRobotic_scrap)

    # Wait until next time
    sleep(120)

