"A Director Class"
from house_builder import HouseBuilder

class IglooDirector: #pylint: disable=too-few-public-methods
    "One of the Directors, that can build a complex representation"

    @staticmethod
    def construct():
        """Constructus and returns the final product
        Note that in this IghlooDirtector, it has omitted the set_number_of_window
        call since this Igloo will have no windows.
        """

        return HouseBuilder().set_building_type("Igloo").set_wall_material("Ice").set_number_doors(1).get_result()