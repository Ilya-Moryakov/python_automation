from smartphone import Smartphone

catalog = [
    Smartphone("Huawei", "1", "+79999999999"),
    Smartphone("Xiaomi", "2", "+78888888888"),
    Smartphone("Samsung", "3", "+77777777777"),
    Smartphone("Apple", "4", "+76666666666"),
    Smartphone("Realme", "5", "+75555555555")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
