# PI
PI = math.pi
# 焦耳到兆吨的转换
joules2megatones = 1 / (4.186 * 10 ** 15)

class Target:
    
    def __init__(self, rhoSurface = 1, dragC = 2, schaleHeight = 8000,
                 fp = 7, pEarth = 1.794 * 10**32, mEarth = 5.97 * 10**24,
                 lEarth = 5.86 * 10**33, g = 9.8, R_earth = 6370, surface_wave_v = 5,
                 melt_coeff = 8.9 * 10**-21, vEarth = 1.1 * 10**12):
        
        self.rhoSurface = rhoSurface # suface density of atmosphere kg/m^3
        self.dragC = dragC
        self.schaleHeight = self.schaleHeight
        self.fp = fp
        self.schaleHeight = schaleHeight
        self.pEarth = pEarth
        self.mEarth = mEarth
        self.lEarth = lEarth
        self.g = g
        self.R_earth = R_earth
        self.surface_wave_v = surface_wave_v
        self.melt_coeff = melt_coeff
        self.vEarth = vEarth
        
        return