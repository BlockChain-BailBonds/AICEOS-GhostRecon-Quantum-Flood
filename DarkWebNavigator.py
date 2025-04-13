
import random

class DarkWebNavigator:
    def __init__(self):
        self.routes = []

    def generate_route(self):
        layers = ['Tor', 'I2P', 'VPN']
        route = random.sample(layers, k=3)
        self.routes.append(route)
        print(f"[Navigator] Generated route: {' -> '.join(route)}")
        return route
