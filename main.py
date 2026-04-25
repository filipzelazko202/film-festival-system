from database.db import Base, engine, Session
from models.festival import Festival
from models.film import Film
from models.employee import Employee
from models.location import Location


def create_db():
    Base.metadata.create_all(bind=engine)
def add_data():
    session = Session()

    # sprawdzamy czy już są dane
    if session.query(Festival).first():
        print("Festiwale już istnieją")
        session.close()
        return

    festivals = [
        Festival(name="Warszawski Festiwal Filmowy", city="Warszawa", latitude=52.23, longitude=21.01),
        Festival(name="Krakowski Festiwal Filmowy", city="Kraków", latitude=50.06, longitude=19.94),
        Festival(name="Wrocławski Festiwal Filmowy", city="Wrocław", latitude=51.11, longitude=17.03),
        Festival(name="Poznański Festiwal Filmowy", city="Poznań", latitude=52.40, longitude=16.92),
        Festival(name="Gdański Festiwal Filmowy", city="Gdańsk", latitude=54.35, longitude=18.65),
    ]

    for fest in festivals:
        session.add(fest)

    session.commit()
    session.close()


import webbrowser
import os


def open_map():


    create_map()

    path = os.path.abspath("mapa.html")
    webbrowser.open(f"file://{path}")

    print("✔ Otworzono mapę")



def update_data(fest_id):
    session = Session()

    fest = session.query(Festival).filter(Festival.id == fest_id).first()

    if fest:
        print("\n--- Edycja festiwalu ---")

        print(f"Obecna nazwa: {fest.name}")
        print(f"Obecne miasto: {fest.city}")
        print(f"Obecne współrzędne: {fest.latitude}, {fest.longitude}")

        # 👉 jeśli ENTER → zostaje stara wartość
        name = input(f"Nowa nazwa ({fest.name}): ") or fest.name
        city = input(f"Nowe miasto ({fest.city}): ") or fest.city

        try:
            lat_input = input(f"Nowa szerokość ({fest.latitude}): ")
            lon_input = input(f"Nowa długość ({fest.longitude}): ")

            latitude = float(lat_input) if lat_input else fest.latitude
            longitude = float(lon_input) if lon_input else fest.longitude

        except ValueError:
            print("❌ Błędne współrzędne!")
            session.close()
            return

        fest.name = name
        fest.city = city
        fest.latitude = latitude
        fest.longitude = longitude

        session.commit()
        print("✔ Zaktualizowano festiwal")

    else:
        print("❌ Nie znaleziono festiwalu")

    session.close()

def show_data():
    session = Session()

    festivals = session.query(Festival).all()

    if not festivals:
        print("Brak festiwali w bazie")

    for fest in festivals:
        print(fest.id, fest.name, fest.city, fest.latitude, fest.longitude)

    session.close()

def delete_data(fest_id):
    session = Session()

    fest = session.query(Festival).filter(Festival.id == fest_id).first()

    if fest:
        session.delete(fest)
        session.commit()
        print("Usunięto festiwal")
    else:
        print("Nie znaleziono festiwalu")

    session.close()



def add_locations():
    session = Session()

    # sprawdzamy czy już są lokalizacje
    if session.query(Location).first():
        print("Lokalizacje już istnieją")
        session.close()
        return

    locations = [
        # Warszawa
        Location(name="Kino Warszawa Centrum", city="Warszawa", latitude=52.23, longitude=21.01, festival_id=1),
        Location(name="Kino Wisła", city="Warszawa", latitude=52.25, longitude=21.00, festival_id=1),
        Location(name="Kino Luna", city="Warszawa", latitude=52.22, longitude=21.02, festival_id=1),

        # Kraków
        Location(name="Kino Pod Baranami", city="Kraków", latitude=50.06, longitude=19.94, festival_id=2),
        Location(name="Kino Kijów", city="Kraków", latitude=50.05, longitude=19.93, festival_id=2),
        Location(name="Kino Mikro", city="Kraków", latitude=50.07, longitude=19.95, festival_id=2),

        # Wrocław
        Location(name="Kino Nowe Horyzonty", city="Wrocław", latitude=51.11, longitude=17.03, festival_id=3),
        Location(name="Kino Helios Wrocław", city="Wrocław", latitude=51.10, longitude=17.05, festival_id=3),
        Location(name="Kino DCF", city="Wrocław", latitude=51.12, longitude=17.02, festival_id=3),

        # Poznań
        Location(name="Kino Muza", city="Poznań", latitude=52.40, longitude=16.92, festival_id=4),
        Location(name="Kino Rialto", city="Poznań", latitude=52.41, longitude=16.93, festival_id=4),
        Location(name="Kino Apollo", city="Poznań", latitude=52.39, longitude=16.91, festival_id=4),

        # Gdańsk
        Location(name="Kino Kameralne Cafe", city="Gdańsk", latitude=54.35, longitude=18.65, festival_id=5),
        Location(name="Kino Helios Gdańsk", city="Gdańsk", latitude=54.36, longitude=18.64, festival_id=5),
        Location(name="Kino Neptun", city="Gdańsk", latitude=54.34, longitude=18.66, festival_id=5),
    ]

    for loc in locations:
        session.add(loc)

    session.commit()
    session.close()

def show_locations():
    session = Session()

    locations = session.query(Location).all()

    if not locations:
        print("Brak kin w bazie")

    for loc in locations:
        print(loc.id, loc.name, loc.city, loc.latitude, loc.longitude)

    session.close()

def add_one_location():
    session = Session()

    print("\n--- Dodawanie kina ---")

    print("\nDostępne festiwale:")
    show_data()

    name = input("\nNazwa kina: ")
    city = input("Miasto: ")

    try:
        lat = float(input("Szerokość (np. 52.23): "))
        lon = float(input("Długość (np. 21.01): "))
        fest_id = int(input("ID festiwalu: "))
    except ValueError:
        print("Błędne dane!")
        session.close()
        return

    loc = Location(
        name=name,
        city=city,
        latitude=lat,
        longitude=lon,
        festival_id=fest_id
    )

    session.add(loc)
    session.commit()
    session.close()

    print("✔ Dodano kino")

def add_one_festival():
    session = Session()

    print("\n--- Dodawanie festiwalu ---")

    name = input("Nazwa festiwalu: ")
    city = input("Miasto: ")

    try:
        lat = float(input("Szerokość (np. 52.23): "))
        lon = float(input("Długość (np. 21.01): "))
    except ValueError:
        print("Błędne współrzędne!")
        session.close()
        return

    fest = Festival(
        name=name,
        city=city,
        latitude=lat,
        longitude=lon
    )

    session.add(fest)
    session.commit()
    session.close()

    print("✔ Dodano festiwal")

def delete_location(loc_id):
    session = Session()

    loc = session.query(Location).filter(Location.id == loc_id).first()

    if loc:
        session.delete(loc)
        session.commit()
        print("Usunięto kino")
    else:
        print("Nie znaleziono kina")

    session.close()

def update_location(loc_id):
    session = Session()

    loc = session.query(Location).filter(Location.id == loc_id).first()

    if loc:
        loc.name = input("Nowa nazwa: ")
        loc.city = input("Nowe miasto: ")

        try:
            loc.latitude = float(input("Nowa szerokość: "))
            loc.longitude = float(input("Nowa długość: "))
        except ValueError:
            print("Błędne współrzędne")

        session.commit()
        print("Zaktualizowano kino")
    else:
        print("Nie znaleziono kina")

    session.close()

def add_one_employee():
    session = Session()

    print("\n--- Lista kin ---")
    show_locations()

    try:
        location_id = int(input("Podaj ID kina: "))
    except ValueError:
        print("Błędne ID")
        return

    name = input("Imię i nazwisko: ")
    emp_role = input("Rola (np. technik): ")

    try:
        lat = float(input("Szerokość: "))
        lon = float(input("Długość: "))
    except ValueError:
        print("Błędne współrzędne")
        return

    emp = Employee(
        name=name,
        role=emp_role,
        latitude=lat,
        longitude=lon,
        location_id=location_id
    )

    session.add(emp)
    session.commit()
    session.close()

    print("✔ Dodano pracownika")

def show_employees():
    session = Session()

    employees = session.query(Employee).all()

    if not employees:
        print("Brak pracowników")

    for emp in employees:
        print(emp.id, emp.name, emp.role, emp.latitude, emp.longitude)

    session.close()

def delete_employee(emp_id):
    session = Session()

    emp = session.query(Employee).filter(Employee.id == emp_id).first()

    if emp:
        session.delete(emp)
        session.commit()
        print("✔ Usunięto pracownika")
    else:
        print("Nie znaleziono")

    session.close()

def update_employee(emp_id):
    session = Session()

    emp = session.query(Employee).filter(Employee.id == emp_id).first()

    if emp:
        print("\n--- Edycja pracownika ---")

        print(f"Obecne dane: {emp.name}, {emp.role}")

        name = input(f"Nowe imię ({emp.name}): ") or emp.name
        emp_role = input(f"Nowa rola ({emp.role}): ") or emp.role

        try:
            lat_input = input(f"Szerokość ({emp.latitude}): ")
            lon_input = input(f"Długość ({emp.longitude}): ")

            latitude = float(lat_input) if lat_input else emp.latitude
            longitude = float(lon_input) if lon_input else emp.longitude

        except ValueError:
            print("Błędne współrzędne")
            session.close()
            return

        emp.name = name
        emp.role = emp_role
        emp.latitude = latitude
        emp.longitude = longitude

        session.commit()
        print("✔ Zaktualizowano pracownika")

    else:
        print("Nie znaleziono")

    session.close()



def create_map():
    import folium

    session = Session()

    festivals = session.query(Festival).all()
    locations = session.query(Location).all()
    employees = session.query(Employee).all()

    mapa = folium.Map(location=[52.0, 19.0], zoom_start=6)

    # 🔴 FESTIWALE
    fest_layer = folium.FeatureGroup(name="Festiwale")

    for fest in festivals:
        folium.Marker(
            location=[fest.latitude, fest.longitude],
            popup=f"{fest.name} ({fest.city})",
            icon=folium.Icon(color="red", icon="star")
        ).add_to(fest_layer)

    # 🟢 KINA
    loc_layer = folium.FeatureGroup(name="Kina")

    for loc in locations:
        loc_employees = [e for e in employees if e.location_id == loc.id]

        emp_text = "<br>".join([f"{e.name} ({e.role})" for e in loc_employees])

        popup_text = f"{loc.name}<br>{emp_text}"

        folium.Marker(
            location=[loc.latitude, loc.longitude],
            popup=popup_text,
            icon=folium.Icon(color="green", icon="film")
        ).add_to(loc_layer)

    # ✅ DODANIE WARSTW
    fest_layer.add_to(mapa)
    loc_layer.add_to(mapa)

    folium.LayerControl().add_to(mapa)

    mapa.save("mapa.html")
    session.close()
def add_films():
    session = Session()

    if session.query(Film).first():
        print("Filmy już istnieją")
        session.close()
        return

    films = [
        Film(title="Film A", festival_id=1),
        Film(title="Film B", festival_id=1),
        Film(title="Film C", festival_id=2),
        Film(title="Film D", festival_id=3),
        Film(title="Film E", festival_id=4),
    ]

    for film in films:
        session.add(film)

    session.commit()
    session.close()

def show_films_for_festival(fest_id):
    session = Session()

    films = session.query(Film).filter(Film.festival_id == fest_id).all()

    if not films:
        print("Brak filmów dla tego festiwalu")

    for film in films:
        print(film.title)

    session.close()

def choose_role():
    print("\n--- Wybierz tryb ---")
    print("1 - Zaloguj jako admin")
    print("2 - Wejdź jako gość")

    choice = input("Wybierz: ")

    if choice == "1":
        return login()   # normalne logowanie

    elif choice == "2":
        print("Zalogowano jako gość")
        return "guest"

    else:
        print("Zła opcja")
        return None

def add_employees():
    session = Session()

    if session.query(Employee).first():
        print("Pracownicy już istnieją")
        session.close()
        return

    employees = [
        # Warszawa
        Employee(name="Jan Kowalski (technik)", latitude=52.23, longitude=21.01, location_id=1),
        Employee(name="Anna Nowak (koordynator)", latitude=52.24, longitude=21.02, location_id=2),
        Employee(name="Piotr Wiśniewski (obsługa)", latitude=52.22, longitude=21.00, location_id=3),

        # Kraków
        Employee(name="Katarzyna Wójcik (technik)", latitude=50.06, longitude=19.94, location_id=4),
        Employee(name="Michał Kamiński (koordynator)", latitude=50.05, longitude=19.93, location_id=5),
        Employee(name="Paweł Lewandowski (obsługa)", latitude=50.07, longitude=19.95, location_id=6),

        # Wrocław
        Employee(name="Tomasz Zieliński (technik)", latitude=51.11, longitude=17.03, location_id=7),
        Employee(name="Magdalena Szymańska (koordynator)", latitude=51.10, longitude=17.05, location_id=8),
        Employee(name="Krzysztof Woźniak (obsługa)", latitude=51.12, longitude=17.02, location_id=9),

        # Poznań
        Employee(name="Agnieszka Dąbrowska (technik)", latitude=52.40, longitude=16.92, location_id=10),
        Employee(name="Marcin Kaczmarek (koordynator)", latitude=52.41, longitude=16.93, location_id=11),
        Employee(name="Łukasz Piotrowski (obsługa)", latitude=52.39, longitude=16.91, location_id=12),

        # Gdańsk
        Employee(name="Ewa Grabowska (technik)", latitude=54.35, longitude=18.65, location_id=13),
        Employee(name="Damian Pawlak (koordynator)", latitude=54.36, longitude=18.64, location_id=14),
        Employee(name="Karol Michalski (obsługa)", latitude=54.34, longitude=18.66, location_id=15),
    ]

    for emp in employees:
        session.add(emp)

    session.commit()
    session.close()

def show_employees_for_location(loc_id):
    session = Session()

    employees = session.query(Employee).filter(Employee.location_id == loc_id).all()

    for emp in employees:
        print(emp.name)

    session.close()
def show_employees_for_festival(fest_id):
    session = Session()

    locations = session.query(Location).filter(Location.festival_id == fest_id).all()

    if not locations:
        print("Brak lokalizacji dla tego festiwalu")
        session.close()
        return

    found = False

    for loc in locations:
        employees = session.query(Employee).filter(Employee.location_id == loc.id).all()

        for emp in employees:
            print(emp.name, "-", loc.name)
            found = True

    if not found:
        print("Brak pracowników")

    session.close()

def login():
    user = input("Login: ")
    password = input("Hasło: ")

    if user == "admin" and password == "1234":
        print("Zalogowano jako admin")
        return "admin"

    elif user == "guest":
        print("Zalogowano jako gość")
        return "guest"

    else:
        print("Błąd logowania")
        return None


def menu(user_role):
    while True:
        print("\n--- MENU ---")
        print("1 - Pokaż festiwale")
        print("2 - Pokaż kina")
        print("3 - Pokaż pracowników")
        print("4 - Pokaż filmy")

        if user_role == "admin":
            print("5 - Dodaj festiwal")
            print("6 - Usuń festiwal")
            print("7 - Edytuj festiwal")
            print("8 - Dodaj kino")
            print("9 - Usuń kino")
            print("10 - Edytuj kino")
            print("11 - Dodaj pracownika")
            print("12 - Usuń pracownika")
            print("13 - Edytuj pracownika")
            print("14 - Otwórz mapę")

        print("0 - Wyjście")

        choice = input("Wybierz: ")

        if choice == "1":
            show_data()

        elif choice == "2":
            show_locations()

        elif choice == "3":
            show_data()
            try:
                fest_id = int(input("Podaj ID festiwalu: "))
                show_employees_for_festival(fest_id)
            except ValueError:
                print("Błędne ID")


        elif choice == "4":

            show_data()

            try:

                fest_id = int(input("Podaj ID festiwalu: "))

                show_films_for_festival(fest_id)

            except ValueError:

                print("Błędne ID")

        elif role == "admin" and choice == "5":
            add_one_festival()


        elif role == "admin" and choice == "6":

            print("\n--- Lista festiwali ---")

            show_data()

            try:

                fest_id = int(input("\nPodaj ID festiwalu do usunięcia: "))

                delete_data(fest_id)

            except ValueError:

                print("Błędne ID")


        elif role == "admin" and choice == "7":

            print("\n--- Lista festiwali ---")
            show_data()

            try:
                fest_id = int(input("\nPodaj ID festiwalu do edycji: "))
                update_data(fest_id)

            except ValueError:
                print("Błędne ID")

        elif role == "admin" and choice == "8":
            add_one_location()

        elif role == "admin" and choice == "9":
            loc_id = int(input("ID kina: "))
            delete_location(loc_id)

        elif role == "admin" and choice == "10":
            loc_id = int(input("ID kina: "))
            update_location(loc_id)

        elif role == "admin" and choice == "11":
            add_one_employee()

        elif role == "admin" and choice == "12":
            show_employees()
            emp_id = int(input("ID: "))
            delete_employee(emp_id)

        elif role == "admin" and choice == "13":
            show_employees()
            emp_id = int(input("ID: "))
            update_employee(emp_id)

        elif choice == "14":
            open_map()

        elif choice == "0":
            break

        else:
            print("Zła opcja")

if __name__ == "__main__":
    create_db()
    add_data()
    add_locations()
    add_employees()
    show_data()
    role = choose_role()

    if role:
        menu(role)