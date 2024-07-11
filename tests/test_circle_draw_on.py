import unittest
import sys
import os
import folium

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/junlee/sep/resit/datascience'))
sys.path.insert(0, module_path)

from datascience.maps import Circle, f2_branch_coverage, print_coverage, reset_coverage

class TestCircleDrawOn(unittest.TestCase):
    
    def setUp(self):
        reset_coverage()
        self.circle = Circle(lat=37.8, lon=-122.0)
        self.folium_map = folium.Map(location=[37.8, -122.0], zoom_start=13)
        print("------------------------------------------------")

    def test_draw_on_radius_in_meters_true(self):
        print("Test_draw_on_radius_in_meters_true")
        self.circle.draw_on(self.folium_map, radius_in_meters=True)
        print_coverage()
        self.assertTrue(f2_branch_coverage["draw_on_radius_true"])
        
    def test_draw_on_radius_in_meters_false(self):
        print("Test_draw_on_radius_in_meters_false")
        self.circle.draw_on(self.folium_map, radius_in_meters=False)
        print_coverage()
        self.assertTrue(f2_branch_coverage["draw_on_radius_false"])
        
if __name__ == '__main__':
    unittest.main()