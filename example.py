import datetime
""" This file is create an empty file """
filename = datetime.datetime.now()

def create_file():
    """ The function create an empty file """
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("");

create_file()