class TV:
    def __init__(self, brand, inches=50, price=None, on_off=True, volume=50):
        self.brand = brand
        self.inches = inches
        self.price = price
        self.on_off = on_off
        self.volume = min(max(volume, 0), 100)
        self.channel = 1

    def increase_volume(self):
        self.volume = min(self.volume + 1, 100)

    def decrease_volume(self):
        self.volume = max(self.volume - 1, 0)

    def set_channel(self, channel):
        self.channel = min(max(channel, 1), 50)

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} TV at channel {self.channel}, volume {self.volume}"

class LED(TV):
    def __init__(self, brand, inches, price, thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, inches, price, on_off=True, volume=50)
        self.thickness = thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return 178

    def backlight(self):
        return "Edge-lit"

    def display_details(self):
        return f"{self.brand} LED TV with {self.inches} inches screen, {self.thickness}mm thickness, {self.energy_usage} watts energy usage, {self.lifespan} hours lifespan, {self.refresh_rate}Hz refresh rate, {self.viewing_angle()} degree viewing angle, and {self.backlight()} backlight."

class Plasma(TV):
    def __init__(self, brand, inches, price, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, inches, price, on_off=True, volume=50)
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return 170

    def backlight(self):
        return "Not applicable"

    def display_details(self):
        return f"{self.brand} Plasma TV with {self.inches} inches screen, {self.energy_usage} watts energy usage, {self.lifespan} hours lifespan, {self.refresh_rate}Hz refresh rate, {self.viewing_angle()} degree viewing angle, and {self.backlight()} backlight."
    
tv = TV("Samsung")
print(tv.status()) # Samsung TV at channel 1, volume 50

tv.increase_volume()
print(tv.status()) # Samsung TV at channel 1, volume 51

tv.set_channel(55)
print(tv.status()) # Samsung TV at channel 50, volume 51

led_tv = LED("Sony", 65, 1000, 30, 100, 50000, 120)
print(led_tv.status()) # Sony LED TV at channel 1, volume 50
print(led_tv.display_details()) # Sony LED TV with 65 inches screen, 30mm thickness, 100 watts energy usage, 50000 hours lifespan, 120Hz refresh rate, 178 degree viewing angle, and Edge-lit backlight.

plasma_tv = Plasma("LG", 70, 1500, 200, 30000, 60)
print(plasma_tv.display_details())# LG Plasma TV with 70 inches screen, 200 watts energy usage, 30000 hours lifespan, 60Hz refresh rate, 170 degree viewing angle, and Not applicable backlight.

