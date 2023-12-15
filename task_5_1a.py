computers = {
    "pc1":{
        "os":"Windows 10",
        "Processor":"ADM Phenom II",
        "ram":"8 Gb",
        "motherboard": "MSI87343",
        "hdd": "1Tb",
    },
    "pc2": {
        "os": "Windows 8.1",
        "Processor": "ADM Phenom II",
        "ram": "8 Gb",
        "motherboard": "ASrock-7898",
        "hdd": "512gb",
    },
    "pc3": {
        "os": "Windows 7",
        "Processor": "ADM Phenom II",
        "ram": "4 Gb",
        "motherboard": "Asus-4565",
        "hdd": "1Tb",
    },
}

device = input("Введите имя устройства: ")
parametr = input("Введите имя параметра: ")
print(computers[device][parametr])


