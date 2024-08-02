from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    display_taxis(taxis)
    taxi_choice = input("Choose taxi: ")
    if taxi_choice.isdigit():
        taxi_choice = int(taxi_choice)
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
    print("Invalid taxi choice")
    return None
