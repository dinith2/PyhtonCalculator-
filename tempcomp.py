import psutil

def get_cpu_temperature():
    try:
        sensors_temperatures = psutil.sensors_temperatures()
        if "coretemp" in sensors_temperatures:
            core_temps = sensors_temperatures["coretemp"]
            if core_temps:
                return core_temps[0].current
    except Exception as e:
        print("Error:", e)
    return None

def is_too_hot(temperature, threshold):
    if temperature is not None:
        return temperature > threshold
    return False

def main():
    threshold = 80  
    cpu_temperature = get_cpu_temperature()

    if cpu_temperature is not None:
        print(f"CPU Temperature: {cpu_temperature}°C")
        
        if is_too_hot(cpu_temperature, threshold):
            print("Warning: CPU temperature is too hot!")
        else:
            print("CPU temperature is within acceptable range.")
    else:
        print("Unable to retrieve CPU temperature.")

if __name__ == "__main__":
    main()
