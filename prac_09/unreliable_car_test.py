from unreliable_car import UnreliableCar


def main():
    new_unreliable_car = UnreliableCar("Bad Car", 100, 60)

    distance_driven = new_unreliable_car.drive(40)
    print(f"Attempted to drive 40km. Distance driven: {distance_driven}km")

    print(new_unreliable_car)


main()