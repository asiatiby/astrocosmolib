import numpy as np
import scipy.integrate as spi
from scipy.constants import c

c1= c/1000

class Distances:
    """
    Class to calculate cosmological distances.
    """

    def __init__(self, hubble_function):
        self.hubble_function = hubble_function

    def comoving_distance(self, z):
        """
        Calculate the comoving distance for a given redshift.

        Parameters
        ----------
        z : float
            Redshift.

        Returns
        -------
        float
            Comoving distance in Mpc.
        """
        # Integrate the inverse of the Hubble parameter
        # from 0 to z
        # integral, err_integral = spi.quad(lambda z: c / self.hubble_function(z), 0, z)[0]
        integral, err_integral = spi.quad(lambda z: c1 / self.hubble_function(z), 0, z)
        #integral = np.trapezoid(c / self.hubble_function(z), z)
        return integral 
        # Convert to Mpc

    def rhubble_distance(self, z):
        integral, err_integral = spi.quad(lambda z: 1.0 / self.hubble_function(z), z, np.inf)
        return integral 


    def angular_distance(self, z):
        return self.comoving_distance(z) / (1 + z)
    
    def luminosity_distance(self, z):
        return self.comoving_distance(z) * (1 + z)
    
    def hubble_distance(self, z):
        #return self.comoving_distance(z) * (1 + z) / self.hubble_function(z)
        return 299792.458 / self.hubble_function(z)
    
    def angular_diameter_distance(self, z): 
        # D_a = D_m / (1 + z)
        # D_m = D_a * (1 + z)
        return self.angular_distance(z)*(1 + z)
    
    def Dv_distance(self, z):
        #dove D_m è la distanza comovente trasversale D_m = D_a*(1+z)
        # Calculate the comoving distance and the Hubble parameter at z
        D_a = self.angular_distance(z)
        D_h = self.hubble_distance(z)
        D_m = D_a * (1 + z)

        # Calculate Dv
        D_v = (z* D_m**2 * D_h )**(1/3)

        return D_v