def main():
    distance = input('Input distance (in meter): ')
    time = input('Input time (in second): ')

    print(f"La vitesse est de {(float(distance) / float(time)) * 3.6} km/h")
    print(f"La vitesse est de {(float(distance) / float(time)) * 3.6:.2f} km/h")


if __name__ == '__main__':
    main()
