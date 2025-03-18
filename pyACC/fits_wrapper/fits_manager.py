#open what is needed to open fits files 
from astropy.io import fits
#import numpy 
import numpy as np 

#import the logger
from ..helpers.logger import Logger 

class FitsManager:
       
    "A class to manage FITS files, using astropy.iofits module"
    #Define the constructor
    def __init__(self, input_file):
        "constructor of the class "
        ":param input_file: the input file to be opened"

        self.input_file= input_file
        self.hdulist= fits.open(input_file)

        self.logger = Logger("FitsManager")
        self.logger("Fits open succesfully")

    def get_hdu_count(self):

        return len(self.hdulist)

    
    def get_header(self, hdu_index):
        
        if hdu_index < 0 or hdu_index >= len(self.hdulist):
            raise ValueError("Invalid HDU index")

        return self.hdulist[hdu_index].header
    
    def get_data(self, hdu_index):

        "return the data of a given HDU"
        "param: hdu: the Hdu to get header form"

        if hdu_index < 0 or hdu_index >= len(self.hdulist):
            self.logger.error("Invalid HDU index", ValueError)

        return self.hdulist[hdu_index].data
    
    
    
    