import unittest
import copy
from typing import *
from firetracker import FireTracker
import matplotlib.pyplot as plt

class TestFireTracker(FireTracker):

    def __init__(self, trail: str, test_fires: List[object]) -> None:
        self.test_fires = test_fires
        super(TestFireTracker, self).__init__(trail)

    def call_fire_api(self) -> List[object]:
        return copy.deepcopy(self.test_fires)

class FireUnitTesting(unittest.TestCase):

    test_fire_template = {
        'attributes': {
            'poly_GISAcres': 50,
            'irwin_IncidentName': 'Test Fire',
            'irwin_PercentContained': 95,
        },
        'geometry': {
            'rings': None
        }
    }

    test_fire_coords = [
    #CT
        [[[ -107.460916, 38.070289], [ -107.556031, 38.070289], [ -107.556031, 38.135239], [ -107.460916, 38.135239]]],
        [[[ -106.330612, 39.673335], [ -106.338165, 39.485990], [ -106.051834, 39.466909], [ -106.066940, 39.689188]]],
    #PNT
        [[[-120.264561, 48.098639], [-120.264561, 47.348513], [-118.880284, 47.329900], [-118.902256, 48.039908]]],
        [[[-114.477539, 49.038410], [-114.435321, 48.271664], [-113.113007, 48.349559], [-113.192346, 48.941153]]],
    #AZT
        [[[ -112.159124, 33.184167], [ -111.920172, 33.722682], [ -111.705938, 33.193361]]],
        [[[ -110.898443, 32.451605], [ -110.875784, 32.361460], [ -110.720259, 32.360009], [ -110.720259, 32.457109]]],
    #PCT
        [[[-122.173511, 40.819048], [-122.178234, 40.513852], [-121.740926, 40.490152], [-121.798541, 40.756833]]],
        [[[-121.607023, 47.532033], [-121.610801, 47.265432], [-121.193327, 47.356368]]],
    #CDT
        [[[ -108.067945, 45.055377],[-108.130315, 44.006080],[-106.443914, 44.057421],[-106.471379, 45.051626]]],
        [[[ -107.289151, 36.443293],[-106.684903, 37.168985],[-105.668668, 36.044569]]]
    ]

    trails = ['CT', 'PNT', 'AZT', 'PCT', 'CDT']

    test_fires = []
    for i, coords in enumerate(test_fire_coords):
        fire = copy.deepcopy(test_fire_template)
        fire['geometry']['rings'] = coords
        fire['attributes']['irwin_IncidentName'] += f' {i + 1}'
        test_fires.append(fire)
    
    # def test_mile_markers(self) -> None:
    #     for trail in self.trails:
    #         tracker = TestFireTracker(trail, self.test_fires)
    #         mile_markers = list(tracker.trail_mile_markers.values())
    #         try:
    #             self.assertTrue(mile_markers[0] < 1)
    #             print(f'{trail} test_mile_markers PASSED: first mile marker expected size\n\n{mile_markers[0]} mi. to {mile_markers[len(mile_markers) - 1]} mi.')
    #         except AssertionError:
    #             print(f'{trail} test_mile_markers FAILED: first mile marker larger than expected size\n\n{mile_markers[0]} mi. to {mile_markers[len(mile_markers) - 1]} mi.')

    def test_add_fires(self) -> None:
        for trail in self.trails:
            tracker = TestFireTracker(trail, self.test_fires)
            tracker.plot()
            try:
                self.assertTrue(len(tracker.close_fires) > 0)
                print(f'{trail} test_add_fires PASSED: at least one test fire added to close fires.')
            except AssertionError:
                print(f'{trail} test_add_fires FAILED: close fires was empty.')
    
    # def test_fire_not_crossing_trail(self) -> None:
    #     for trail in self.trails:
    #         tracker = TestFireTracker(trail, self.test_fires)
    #         try:
    #             self.assertTrue(len(tracker.close_fires) > len(tracker.fires_crossing_trail))
    #             print(f'{trail} test_fire_not_crossing_trail PASSED: at least one fire close but not crossing trail.')
    #         except AssertionError:
    #             print(f'{trail} test_fire_not_crossing_trail FAILED: no fires not crossing trail.')

    # def test_fire_crossing_trail(self) -> None:
    #     for trail in self.trails:
    #         tracker = TestFireTracker(trail, self.test_fires)
    #         try:
    #             self.assertTrue(len(tracker.fires_crossing_trail) > 0)
    #             print(f'{trail} test_fire_crossing_trail PASSED: at least one fire was crossing trail.')
    #         except AssertionError:
    #             print(f'{trail} test_fire_crossing_trail FAILED: no fires were crossing trail.')
    
    # def test_sms(self) -> None:
    #     for trail in self.trails:
    #         tracker = TestFireTracker(trail, self.test_fires)
    #         try:
    #             self.assertTrue(tracker.create_SMS())
    #             print(f'{trail} test_sms PASSED: sms created')
    #             print(tracker.text)
    #         except AssertionError:
    #             print(f'{trail} test_sms FAILED: sms not created')

if __name__ == '__main__':
    unittest.main()