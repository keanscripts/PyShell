import os
os.system('cls' if os.name == 'nt' else 'clear')
import re
import time 
import json
import requests
os.chdir("/")
in_to_cm = lambda val: val * 2.54; cm_to_in = lambda val: val / 2.54
yd_to_ft = lambda val: val * 3; ft_to_yd = lambda val: val / 3
mi_to_km = lambda val: val * 1.60934; km_to_mi = lambda val: val / 1.60934
m_to_yd = lambda val: val * 1.09361; yd_to_m = lambda val: val / 1.09361
mm_to_in = lambda val: val / 25.4; in_to_mm = lambda val: val * 25.4
lb_to_kg = lambda val: val * 0.453592; kg_to_lb = lambda val: val / 0.453592
oz_to_g = lambda val: val * 28.3495; g_to_oz = lambda val: val / 28.3495
c_to_f = lambda val: (val * 1.8) + 32; f_to_c = lambda val: (val - 32) / 1.8
gal_to_l = lambda val: val * 3.78541; l_to_gal = lambda val: val / 3.78541
qt_to_l = lambda val: val * 0.946353; l_to_qt = lambda val: val / 0.946353
floz_to_ml = lambda val: val * 29.5735; ml_to_floz = lambda val: val / 29.5735
conversions = {
    "in to cm": (in_to_cm, "Inches: ", "cm"), "cm to in": (cm_to_in, "Centimeters: ", "in"),
    "yd to ft": (yd_to_ft, "Yards: ", "ft"), "ft to yd": (ft_to_yd, "Feet: ", "yd"),
    "mi to km": (mi_to_km, "Miles: ", "km"), "km to mi": (km_to_mi, "Kilometers: ", "mi"),
    "m to yd": (m_to_yd, "Meters: ", "yd"), "yd to m": (yd_to_m, "Yards: ", "m"),
    "mm to in": (mm_to_in, "Millimeters: ", "in"), "in to mm": (in_to_mm, "Inches: ", "mm"),
    "lb to kg": (lb_to_kg, "Pounds: ", "kg"), "kg to lb": (kg_to_lb, "Kilograms: ", "lb"),
    "oz to g": (oz_to_g, "Ounces: ", "g"), "g to oz": (g_to_oz, "Grams: ", "oz"),
    "c to f": (c_to_f, "Celsius: ", "Fahrenheit"), "f to c": (f_to_c, "Fahrenheit: ", "Celsius"),
    "gal to l": (gal_to_l, "Gallons: ", "Liters"), "l to gal": (l_to_gal, "Liters: ", "Gallons"),
    "qt to l": (qt_to_l, "Quarts: ", "Liters"), "l to qt": (l_to_qt, "Liters: ", "Quarts"),
    "floz to ml": (floz_to_ml, "Fluid ounces: ", "Milliliters"), "ml to floz": (ml_to_floz, "Milliliters: ", "Fluid ounces"),
}
def weather():
    locations = json.loads(requests.get("https://raw.githubusercontent.com/keanscripts/Toolbox/main/Toolbox/locations.json").text)
    city = input("Select a location: ").lower()
    lat, lon = locations[city]["lat"], locations[city]["lon"]
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=6a303cdc50428b6f68a130943e1297c6"
    data = requests.get(url).json()
    print(f"Temperature: {((data['main']['temp'] - 273.15) * 9/5 + 32):.2f} °F")
    print(f"Pressure: {data['main']['pressure']} hPa")
    print(f"Humidity: {data['main']['humidity']} %")
    print(f"Visibility: {data['visibility']} m")
    print(f"Wind speed: {data['wind']['speed']} m/s")
    print(f"Weather: {data['weather'][0]['description']}")
def converter():
    conversion = conversions[toolbox]
    convert_func, prompt_msg, unit = conversion
    val = float(input(prompt_msg))
    result = convert_func(val)
    print("Result:", result, unit)
toolbox = ""
while toolbox not in ["end", "stop", "quit"]:
    toolbox = input("Toolbox: ")
    if toolbox.lower() == "help":
        print("Visit our documentation on github!")
    elif re.match(r'^\s*\d+(\.\d+)?\s*([+\-*/]\s*\d+(\.\d+)?\s*)+$', toolbox):
        result = eval(toolbox)
        print("Result: ", result)
    elif toolbox.lower() in conversions:
        converter()
    elif toolbox.lower() == "weather":
        weather()
    elif toolbox.lower() == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif toolbox.startswith("dir" + " "):
        dir_var = toolbox[4:]
        if dir_var == "access":
            try:
                os.chdir("/")
                print("Directory access has been permitted.")
                dir_access = True
            except Exception as e:
                print(f"Failed to grant access to all directories: {str(e)}")
        elif dir_var == "list":
            cwd = os.getcwd()
            contents = os.listdir(cwd)
            print(contents)
    elif toolbox.startswith("file move"):
        import shutil
        parts = toolbox.split()
        if len(parts) != 7:
            print("Invalid command. Please use the format 'file move [file name] in [source directory] to [destination directory]'")
        else:
            file_name = parts[2]
            operation = "mv"
            source_path = parts[4]
            destination_path = parts[6]
            file_path = os.path.join(os.path.abspath(source_path), file_name)
            source_dir = os.path.abspath(source_path)
            destination_dir = os.path.abspath(destination_path)
            if not os.path.exists(file_path):
                print(f"Error: The file '{file_name}' does not exist in the directory '{source_path}'.")
            else:
                print(f"Are you sure you want to move '{file_name}' from '{source_dir}' to '{destination_dir}'? (y/n)")
                confirm = input()
                if confirm.lower() == 'y':
                    try:
                        if operation == "i":
                            shutil.copy2(file_path, source_dir)
                        elif operation == "mv":
                            shutil.move(file_path, destination_dir)
                        print(f"Moved '{file_name}' to '{destination_dir}'.")
                    except Exception as e:
                        print(f"Error: {str(e)}")
                else:
                    print("Action canceled.")
    elif toolbox.startswith("file delete"):
        parts = toolbox.split()
        if len(parts) != 5:
            print("Invalid command. Please use the format 'file delete [file name] in [directory]'")
        else:
            file_name = parts[2]
            directory = parts[4]
            file_path = os.path.join(os.path.abspath(directory), file_name)
            if not os.path.exists(file_path):
                print(f"Error: The file '{file_name}' does not exist in the directory '{directory}'.")
            else:
                print(f"Are you sure you want to delete '{file_name}' from '{directory}'? (y/n)")
                confirm = input()
                if confirm.lower() == 'y':
                    try:
                        os.remove(file_path)
                        print(f"Deleted '{file_name}' from '{directory}'.")
                    except Exception as e:
                        print(f"Error: {str(e)}")
                else:
                    print("Action canceled.")
    else:
        if toolbox not in ["end", "stop", "quit"]:
            print("Invalid input, type 'help' for a list of commads")
