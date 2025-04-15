import numpy as np
from astropy.io import fits
from ..helpers.logger import Logger

class Catalogue:
    
    def __init__(self, input_file, cosmology):
        self.input_file = input_file
        self.cosmology = cosmology
        self.hdulist = fits.open(input_file)

        self.logger = Logger("Catalogue")
        self.logger("FITS file opened successfully with custom cosmology.")

    def get_data(self, hdu_index=1):
        if hdu_index < 0 or hdu_index >= len(self.hdulist):
            self.logger.error("Invalid HDU index", ValueError)
        return self.hdulist[hdu_index].data

    def compute_cartesian_coordinates(
        self,
        z_key="zspec",
        ra_key="alpha",
        dec_key="delta",
        z_min=0.4,
        z_max=1.4
    ):
        data = self.get_data()
        redshift = data[z_key]
        ra = data[ra_key]
        dec = data[dec_key]

        # Applica il filtro di redshift
        mask = (redshift >= z_min) & (redshift < z_max)
        z_cut = redshift[mask]
        ra_cut = ra[mask]
        dec_cut = dec[mask]

        # Calcola distanza comovente
        dc = self.cosmology.comoving_distance(z_cut).value  # in Mpc

        # Coordinate cartesiane
        X = dc * np.cos(np.radians(dec_cut)) * np.cos(np.radians(ra_cut))
        Y = dc * np.cos(np.radians(dec_cut)) * np.sin(np.radians(ra_cut))
        Z = dc * np.sin(np.radians(dec_cut))

        self.logger("Coordinate cartesiane calcolate correttamente.")
        return X, Y, Z
