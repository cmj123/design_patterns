"A Director Class"
from house_builder import HouseBuilder

class HouseBoatDirector: # pylint: disable=too-few-public-methods 
    "One of the Directors, that can build a complex representation"

    @staticmethod
    def construct():
        "Constructs and return the final product"
        return HouseBuilder().set_building_type("House Boat").set_wall_material("Wood").set_number_windows(8).set_number_doors(6).get_result()