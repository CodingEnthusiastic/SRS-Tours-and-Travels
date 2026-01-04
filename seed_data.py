import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
django.setup()

from sample.models import (
    Buses, Flights, Tours, VisitingData, TravelsData, 
    SeasonsData, TouristPlaces, Distances
)

# Clear existing data (optional)
Buses.objects.all().delete()
Flights.objects.all().delete()
Tours.objects.all().delete()
VisitingData.objects.all().delete()
TravelsData.objects.all().delete()
SeasonsData.objects.all().delete()
TouristPlaces.objects.all().delete()
Distances.objects.all().delete()

print("Creating seed data...")

# Bus Data (30 buses)
bus_travels = ['RedBus', 'GoIbibo', 'FirstFlight', 'TravelXpress', 'ScanIndian']
bus_data = [
    ('Bangalore', 'Chennai', 2, 30, 5, 45, 200, 35),
    ('Bangalore', 'Hyderabad', 3, 45, 7, 15, 250, 40),
    ('Mumbai', 'Goa', 4, 0, 8, 30, 350, 32),
    ('Delhi', 'Agra', 2, 15, 4, 45, 180, 38),
    ('Bangalore', 'Mysore', 2, 0, 3, 45, 150, 36),
    ('Chennai', 'Bangalore', 5, 30, 8, 0, 220, 34),
]

bus_count = 0
for i in range(5):
    for dep_place, arr_place, dur, dep_h, arr_h, arr_m, fare, seats in bus_data:
        if bus_count >= 30:
            break
        bus = Buses.objects.create(
            travels=bus_travels[i % len(bus_travels)],
            departure_timeHours=str(8 + i % 12).zfill(2),
            departure_timeMinutes=str(i * 15 % 60).zfill(2),
            departure_palce=dep_place,
            arrival_timeHours=str(arr_h).zfill(2),
            arrival_timeMinutes=str(arr_m).zfill(2),
            arrival_place=arr_place,
            duration=f"{dur}h 30m",
            fare=str(fare),
            seats_available=seats,
            ac_sleeper='AC' if i % 2 == 0 else 'Sleeper',
            bus_num=f"KA{i:02d}BN{5000+i:04d}",
            date="15/01/2026",
            day=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'][i % 5]
        )
        bus_count += 1

print(f"✓ Created {bus_count} buses")

# Flight Data (25 flights)
flights = ['Air India', 'IndiGo', 'SpiceJet', 'Vistara', 'GoAir']
flight_data = [
    ('Bangalore', 'Delhi', 3, 0, 2, 30, 5000, 150),
    ('Mumbai', 'Bangalore', 1, 45, 1, 15, 3500, 180),
    ('Delhi', 'Goa', 2, 15, 1, 45, 4200, 160),
    ('Chennai', 'Delhi', 2, 30, 2, 0, 4800, 140),
    ('Bangalore', 'Chennai', 1, 0, 0, 45, 2800, 170),
]

flight_count = 0
for i in range(5):
    for dep_place, arr_place, dur, dep_h, arr_h, arr_m, fare, seats in flight_data:
        if flight_count >= 25:
            break
        flight = Flights.objects.create(
            flight=flights[i % len(flights)],
            departure_timeHours=str(dep_h).zfill(2),
            departure_timeMinutes=str(i * 12 % 60).zfill(2),
            departure_palce=dep_place,
            arrival_timeHours=str(arr_h).zfill(2),
            arrival_timeMinutes=str(arr_m).zfill(2),
            arrival_place=arr_place,
            duration=f"{dur}h {arr_m}m",
            fare=str(fare),
            seats_available=seats,
            date="15/01/2026",
            day=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'][i % 5]
        )
        flight_count += 1

print(f"✓ Created {flight_count} flights")

# Tourist Places (35 places)
tourist_places_data = [
    ('Taj Mahal', 500, 3, 'Uttar Pradesh'),
    ('Gateway of India', 200, 2, 'Maharashtra'),
    ('Jaipur City Palace', 350, 2, 'Rajasthan'),
    ('Goa Beaches', 300, 2, 'Goa'),
    ('Mysore Palace', 400, 2, 'Karnataka'),
    ('Ooty Botanical Gardens', 250, 1, 'Tamil Nadu'),
    ('Manali Mountains', 600, 3, 'Himachal Pradesh'),
    ('Darjeeling Tea Gardens', 550, 2, 'West Bengal'),
    ('Varanasi Ghats', 200, 1, 'Uttar Pradesh'),
    ('Cochin Backwaters', 450, 2, 'Kerala'),
    ('Khajuraho Temples', 350, 2, 'Madhya Pradesh'),
    ('Hagia Sophia', 300, 2, 'Delhi'),
    ('Red Fort', 250, 2, 'Delhi'),
    ('Ajanta Caves', 400, 3, 'Maharashtra'),
    ('Ellora Caves', 420, 3, 'Maharashtra'),
    ('Amer Fort', 500, 2, 'Rajasthan'),
    ('Hawa Mahal', 200, 1, 'Rajasthan'),
    ('Charminar', 150, 1, 'Telangana'),
    ('Meenakshi Temple', 300, 2, 'Tamil Nadu'),
    ('Victoria Memorial', 200, 1, 'West Bengal'),
    ('Statue of Unity', 350, 1, 'Gujarat'),
    ('Jaisalmer Fort', 400, 2, 'Rajasthan'),
    ('Udaipur City Palace', 500, 2, 'Rajasthan'),
    ('Maldives Atolls', 1000, 4, 'Maldives'),
    ('Bangkok Grand Palace', 800, 2, 'Thailand'),
    ('Angkor Wat', 900, 2, 'Cambodia'),
    ('Bali Temples', 700, 2, 'Indonesia'),
    ('Singapore Gardens', 600, 1, 'Singapore'),
    ('Phuket Beaches', 550, 2, 'Thailand'),
    ('Dubai Burj Khalifa', 1500, 1, 'UAE'),
]

for i, (place, cost, time, state) in enumerate(tourist_places_data[:30]):
    TouristPlaces.objects.create(
        place=place,
        cost=cost,
        time=time,
        state=state
    )

print(f"✓ Created 30 tourist places")

# Tours (20 packages)
tours_data = [
    ('Rajasthan', 'Jaipur, Udaipur, Jodhpur', '5 Star Resort', 25000),
    ('Goa', 'Beaches, Markets', 'Beach Resort', 15000),
    ('Kerala', 'Backwaters, Tea Gardens', 'Houseboat', 20000),
    ('Himachal', 'Manali, Shimla', 'Mountain Resort', 18000),
    ('Uttarakhand', 'Nainital, Mussoorie', 'Hill Station Hotel', 16000),
    ('Northeast India', 'Assam, Meghalaya', 'Local Hotels', 22000),
    ('South India', 'Bangalore, Chennai, Mysore', 'City Hotels', 19000),
    ('Kashmir', 'Srinagar, Leh-Ladakh', 'Premium Hotels', 35000),
    ('Andaman', 'Islands Tour', 'Beach Resorts', 28000),
    ('Egypt Tour', 'Cairo, Giza Pyramids', 'Luxury Hotels', 50000),
    ('Thailand', 'Bangkok, Phuket', 'Beach Resorts', 32000),
    ('Singapore', 'City Tour', 'City Hotels', 25000),
    ('Bali', 'Temples, Beaches', 'Resort', 30000),
    ('Malaysia', 'Kuala Lumpur, Penang', 'City Hotels', 28000),
    ('Vietnam', 'Hanoi, Ho Chi Minh', 'Budget Hotels', 20000),
    ('Indonesia', 'Jakarta, Bandung', 'Comfort Hotels', 22000),
    ('Cambodia', 'Angkor Wat, Siem Reap', 'Budget Hotels', 24000),
    ('Bhutan', 'Thimphu, Paro', 'Local Resorts', 40000),
    ('Europe Special', 'Paris, London, Amsterdam', 'Star Hotels', 80000),
    ('Switzerland', 'Alps, Interlaken', 'Mountain Resorts', 75000),
]

for location, places, hotel, cost in tours_data:
    Tours.objects.create(
        location=location,
        touristplces_covered=places,
        hotel=hotel,
        cost=str(cost)
    )

print(f"✓ Created 20 tour packages")

# Visiting Data (15 places with population)
visiting_data = [
    ('Taj Mahal', 8000000),
    ('Goa Beaches', 5000000),
    ('Jaipur', 6000000),
    ('Kerala Backwaters', 4000000),
    ('Mysore', 3500000),
    ('Manali', 2500000),
    ('Darjeeling', 2000000),
    ('Varanasi', 5500000),
    ('Cochin', 2800000),
    ('Delhi Fort', 4200000),
    ('Ajanta Caves', 1800000),
    ('Udaipur', 3200000),
    ('Maldives', 1500000),
    ('Bangkok', 7000000),
    ('Bali', 4500000),
]

for place, population in visiting_data:
    VisitingData.objects.create(
        place=place,
        population=population
    )

print(f"✓ Created 15 visiting places data")

# Travels Data (8 travel companies)
travels_data = [
    ('RedBus', 8000000),
    ('GoIbibo', 7500000),
    ('FirstFlight', 6500000),
    ('TravelXpress', 5500000),
    ('MakeMyTrip', 9000000),
    ('Yatra', 4500000),
    ('Cleartrip', 3500000),
    ('EaseMyTrip', 2800000),
]

for travels, population in travels_data:
    TravelsData.objects.create(
        travels=travels,
        population=population
    )

print(f"✓ Created 8 travel companies data")

# Seasons Data (4 seasons)
seasons_data = [
    ('Summer (Mar-May)', 3500000),
    ('Monsoon (Jun-Sep)', 2500000),
    ('Post-Monsoon (Oct-Nov)', 6000000),
    ('Winter (Dec-Feb)', 7500000),
]

for season, population in seasons_data:
    SeasonsData.objects.create(
        season=season,
        population=population
    )

print(f"✓ Created 4 seasonal data")

# Distances between places (30 routes)
distances_data = [
    ('Bangalore', 'Chennai', 350),
    ('Bangalore', 'Hyderabad', 575),
    ('Bangalore', 'Mysore', 140),
    ('Mumbai', 'Goa', 595),
    ('Mumbai', 'Pune', 190),
    ('Delhi', 'Agra', 206),
    ('Delhi', 'Jaipur', 268),
    ('Chennai', 'Hyderabad', 670),
    ('Chennai', 'Coimbatore', 300),
    ('Kolkata', 'Darjeeling', 350),
    ('Jaipur', 'Udaipur', 410),
    ('Jaipur', 'Jodhpur', 334),
    ('Goa', 'Bangalore', 595),
    ('Hyderabad', 'Bangalore', 575),
    ('Mysore', 'Ooty', 280),
    ('Manali', 'Shimla', 250),
    ('Nainital', 'Mussoorie', 280),
    ('Varanasi', 'Gaya', 60),
    ('Cochin', 'Alleppey', 70),
    ('Udaipur', 'Mount Abu', 150),
    ('Jaisalmer', 'Jodhpur', 285),
    ('Ajanta', 'Ellora', 50),
    ('Khajuraho', 'Bhopal', 400),
    ('Pune', 'Lonavala', 60),
    ('Bangalore', 'Coorg', 260),
    ('Agra', 'Mathura', 60),
    ('Lucknow', 'Kanpur', 80),
    ('Indore', 'Ujjain', 55),
    ('Srinagar', 'Leh', 420),
    ('Thiruvananthapuram', 'Kovalam', 15),
]

for fromplace, toplace, distance in distances_data:
    Distances.objects.create(
        fromplace=fromplace,
        toplace=toplace,
        distance=distance
    )

print(f"✓ Created 30 distance routes")

total = (bus_count + flight_count + 30 + 20 + 15 + 8 + 4 + 30)
print(f"\n✅ Successfully seeded {total} records!")
print(f"Database is now ready with sample data.")
