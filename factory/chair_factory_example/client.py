from furniture_factory import FurnitureFactory

FURNITURE = FurnitureFactory.get_furniture("MediumChair")
print(f"{FURNITURE.__class__}: {FURNITURE.get_dimensions()}")

FURNITURE = FurnitureFactory.get_furniture("BigTable")
print(f"{FURNITURE.__class__}: {FURNITURE.get_dimensions()}")