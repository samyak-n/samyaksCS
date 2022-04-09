import utils
from operator import attrgetter


class Earthquake:
    """A class to represent an Earthquake."""

    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return (
                self.place == other.place and self.mag == other.mag and
                self.longitude == other.longitude and self.latitude ==
                other.latitude and self.time == other.time)

    def __str__(self):
        return "({1:.2f}) {0:>40} at {4} ({2:>8.3f}, {3:.3f})".format(
            self.place, float(self.mag), float(self.longitude),
            float(self.latitude), utils.time_to_str(float(self.time)))

    def __repr__(self):
        return ('%s %s %s %s %s' %
                (self.mag, self.longitude, self.latitude,
                 self.time, self.place))


def quake_from_feature(feature):
    place = feature["properties"]["place"]
    mag = feature["properties"]["mag"]
    longitude = feature["geometry"]["coordinates"][0]
    latitude = feature["geometry"]["coordinates"][1]
    milliseconds = feature["properties"]["time"]
    time = int(milliseconds / 1000)
    quake = Earthquake(place, mag, longitude, latitude, time)
    return quake


def read_quakes_from_file(filename):
    quakes = []
    for line in filename:
        raw_data = line.split()
        new_place = ' '.join(raw_data[4:])
        new_quake = Earthquake(new_place, float(raw_data[0]),
                               float(raw_data[1]), float(raw_data[2]),
                               int(raw_data[3]))
        quakes.append(new_quake)
    return quakes


def filter_by_mag(quakes, low, high):
    lst = []
    for obj in quakes:
        if low <= obj.mag <= high:
            lst.append(obj)
    return lst


def filter_by_place(quakes, word):
    return [quake for quake in quakes if word.lower() in quake.place.lower()]


def sort_quakes(quakes, choice):
    if choice == 'm':
        return sorted(quakes, key=attrgetter('mag'), reverse=True)
    elif choice == 't':
        return sorted(quakes, key=attrgetter('time'), reverse=True)
    elif choice == 'l':
        return sorted(quakes, key=attrgetter('longitude'))
    elif choice == 'a':
        return sorted(quakes, key=attrgetter('latitude'))
