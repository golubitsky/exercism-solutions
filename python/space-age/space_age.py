class SpaceAge(object):
    _orbital_periods = {
        'earth': 1,  # number of earth years
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    _seconds_in_earth_year = 31557600

    def __init__(self, seconds):
        self.seconds = seconds
        self.__set_planet_functions()

    def __set_planet_functions(self):
        """Define self.on_{planet} functions for each of the planets in the Solar System.
        """
        for planet in self._orbital_periods:
            fn_name = 'on_' + planet

            # use fn to bind the planet name to the target function
            def fn(planet):
                def age_on_planet(self):
                    earth_years = self.seconds / self._seconds_in_earth_year
                    other_planet_years = earth_years / self._orbital_periods[planet]

                    return round(other_planet_years, 2)

                return age_on_planet

            setattr(SpaceAge, fn_name, fn(planet))
