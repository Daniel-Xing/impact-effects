# -*- encoding: utf-8 -*-
"""
Filename         :Targets.py
Description      :
Time             :2022/07/10 09:38:31
Author           :daniel
Version          :1.0
"""


from .checker import numeric_checker, positive_checker


class Target:
    def __init__(
        self,
        depth,
        distance,
        density,
        ttype=3,
        rhoSurface=1,
        dragC=2,
        schaleHeight=8000,
        fp=7,
        pEarth=1.794 * 10 ** 32,
        mEarth=5.97 * 10 ** 24,
        lEarth=5.86 * 10 ** 33,
        g=9.8,
        R_earth=6370,
        surface_wave_v=5,
        melt_coeff=8.9 * 10 ** -21,
        vEarth=1.1 * 10 ** 12,
        Po=10 ** 5,
        seefloor_density=2700,
    ):

        if density == 1000 and depth == 0:
            raise ValueError(
                "density and depth can not be equal to 1000 and 0"
            )

        self.set_density(density=density)
        self.set_rhoSurface(rhoSurface=rhoSurface)
        self.set_dragC(dragC=dragC)
        self.set_fp(fp=fp)
        self.set_schaleHeight(schaleHeight=schaleHeight)
        self.set_pEarth(pEarth=pEarth)
        self.set_mEarth(mEarth=mEarth)
        self.set_lEarth(lEarth=lEarth)
        self.set_g(g=g)
        self.set_R_earth(R_earth=R_earth)
        self.set_surface_wave_v(surface_wave_v=surface_wave_v)
        self.set_melt_coeff(melt_coeff=melt_coeff)
        self.set_vEarth(vEarth=vEarth)
        self.set_depth(depth=depth)
        self.set_distance(distance=distance)
        self.set_Po(Po=Po)
        self.set_seefloor_density(seefloor_density=seefloor_density)
        self.set_ttype(ttype=ttype)

        return

    """setter
    setter function set the value after checker pass
    """

    def set_density(self, density):
        if not numeric_checker(density):
            raise ValueError("density must be numeric")
        if not positive_checker(density):
            raise ValueError("density must be positive")

        self.density = density

    def set_rhoSurface(self, rhoSurface):
        if not numeric_checker(rhoSurface):
            raise ValueError("rhoSurface must be numeric")
        if not positive_checker(rhoSurface):
            raise ValueError("rhoSurface must be positive")

        self.rhoSurface = rhoSurface

    def set_dragC(self, dragC):
        if not numeric_checker(dragC):
            raise ValueError("dragC must be numeric")
        if not positive_checker(dragC):
            raise ValueError("dragC must be positive")

        self.dragC = dragC

    def set_fp(self, fp):
        if not numeric_checker(fp):
            raise ValueError("fp must be numeric")
        if not positive_checker(fp):
            raise ValueError("fp must be positive")

        self.fp = fp

    def set_schaleHeight(self, schaleHeight):
        if not numeric_checker(schaleHeight):
            raise ValueError("schaleHeight must be numeric")
        if not positive_checker(schaleHeight):
            raise ValueError("schaleHeight must be positive")

        self.schaleHeight = schaleHeight

    def set_pEarth(self, pEarth):
        if not numeric_checker(pEarth):
            raise ValueError("pEarth must be numeric")
        if not positive_checker(pEarth):
            raise ValueError("pEarth must be positive")

        self.pEarth = pEarth

    def set_mEarth(self, mEarth):
        if not numeric_checker(mEarth):
            raise ValueError("mEarth must be numeric")
        if not positive_checker(mEarth):
            raise ValueError("mEarth must be positive")

        self.mEarth = mEarth

    def set_lEarth(self, lEarth):
        if not numeric_checker(lEarth):
            raise ValueError("lEarth must be numeric")
        if not positive_checker(lEarth):
            raise ValueError("lEarth must be positive")

        self.lEarth = lEarth

    def set_g(self, g):
        if not numeric_checker(g):
            raise ValueError("g must be numeric")
        if not positive_checker(g):
            raise ValueError("g must be positive")

        self.g = g

    def set_R_earth(self, R_earth):
        if not numeric_checker(R_earth):
            raise ValueError("R_earth must be numeric")
        if not positive_checker(R_earth):
            raise ValueError("R_earth must be positive")

        self.R_earth = R_earth

    def set_surface_wave_v(self, surface_wave_v):
        if not numeric_checker(surface_wave_v):
            raise ValueError("surface_wave_v must be numeric")
        if not positive_checker(surface_wave_v):
            raise ValueError("surface_wave_v must be positive")

        self.surface_wave_v = surface_wave_v

    def set_melt_coeff(self, melt_coeff):
        if not numeric_checker(melt_coeff):
            raise ValueError("melt_coeff must be numeric")
        if not positive_checker(melt_coeff):
            raise ValueError("melt_coeff must be positive")

        self.melt_coeff = melt_coeff

    def set_vEarth(self, vEarth):
        if not numeric_checker(vEarth):
            raise ValueError("vEarth must be numeric")
        if not positive_checker(vEarth):
            raise ValueError("vEarth must be positive")

        self.vEarth = vEarth

    def set_depth(self, depth):
        if not numeric_checker(depth):
            raise ValueError("depth must be numeric")
        if not positive_checker(depth):
            raise ValueError("depth must be positive")

        self.depth = depth

    def set_distance(self, distance):
        if not numeric_checker(distance):
            raise ValueError("distance must be numeric")
        # if not positive_checker(distance):
        #     raise ValueError("distance must be positive")

        self.distance = distance

    def set_Po(self, Po):
        if not numeric_checker(Po):
            raise ValueError("Po must be numeric")
        if not positive_checker(Po):
            raise ValueError("Po must be positive")

        self.Po = Po

    def set_seefloor_density(self, seefloor_density):
        if not numeric_checker(seefloor_density):
            raise ValueError("seefloor_density must be numeric")
        if not positive_checker(seefloor_density):
            raise ValueError("seefloor_density must be seefloor_densitysitive")

        self.seefloor_density = seefloor_density

    def set_ttype(self, ttype):
        if not numeric_checker(ttype):
            raise ValueError("ttype must be numeric")
        if not positive_checker(ttype):
            raise ValueError("ttype must be ttypesitive")

        self.ttype = ttype

    """getter
    getter return the member value without access it directly
    """

    def get_rhoSurface(self):
        return self.rhoSurface

    def get_dragC(self):
        return self.dragC

    def get_schaleHeight(self):
        return self.schaleHeight

    def get_fp(self):
        return self.fp

    def get_pEarth(self):
        return self.pEarth

    def get_mEarth(self):
        return self.mEarth

    def get_lEarth(self):
        return self.lEarth

    def get_g(self):
        return self.g

    def get_R_earth(self):
        return self.R_earth

    def get_surface_wave_v(self):
        return self.surface_wave_v

    def get_melt_coeff(self):
        return self.melt_coeff

    def get_v_earth(self):
        return self.vEarth

    def get_depth(self):
        return self.depth

    def get_distance(self):
        return self.distance

    def get_Po(self):
        return self.Po

    def get_density(self):
        return self.density
