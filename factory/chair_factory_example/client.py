"Factory Use Case Example Code"

from chair_factory import ChairFactory

# The Client
CHAIR = ChairFactory.get_chair("BigChair")
print(CHAIR.get_dimensions())