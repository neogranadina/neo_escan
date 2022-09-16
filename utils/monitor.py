

def promedio_captura():
    """Calcula el promedio de captura de acuerdo con las últimas 10 capturas"""
    # import log file

    log =  open("logs/neoscan_log.log", "r")
    lines = log.readlines()
    # get lines where is substring "Tiempo total proceso descarga"
    lines = [line for line in lines if "Tiempo total proceso descarga" in line]
    # get last 10 lines
    lines = lines[-10:]
    # get time
    times = [line.split(":")[-1].strip() for line in lines]
    # get average
    average = sum([float(time) for time in times]) / len(times)

    return round(average, 2)


if __name__ == "__main__":
    print(promedio_captura())