
'''
Problem no 3 - calculating Vehical costs
'''

def calc_vehicle_detail(v_type, basic_price, weight):
    if v_type == 'P':
        vehicle_tax = 0.05 * basic_price
        weight_tax = 0.01 * weight
        insurance = 0.01 * basic_price

    elif v_type == 'B':
        vehicle_tax = 0.10 * basic_price
        weight_tax = 0.03 * weight
        insurance = 0.02 * basic_price

    else:
        print("Invalid Vehicle Type")
        return None

    onroad_price = basic_price + vehicle_tax + weight_tax + insurance

    vehicle = {
        "type": v_type,
        "basic_price": basic_price,
        "vehicle_tax": vehicle_tax,
        "weight": weight,
        "insurance": insurance,
        "onroad": onroad_price
    }

    return vehicle


# storing all vehicles
vehicles = []

n = int(input("Enter Number of Vehicles: "))

for i in range(n):
    print("\nVehicle", i + 1)
    v_type = input("Enter Type (P/B): ").upper()
    price = float(input("Enter Basic Price: "))
    weight = float(input("Enter Weight: "))

    vehicle_data = calc_vehicle_detail(v_type, price, weight)
    if vehicle_data is not None:
        vehicles.append(vehicle_data)


print("\n--- Vehicle Details ---")
for v in vehicles:
    print(v)


# Highest on-road price
highest = vehicles[0]
for v in vehicles:
    if v['onroad'] > highest['onroad']:
        highest = v

print("\nVehicle with highest on-road price:")
print(highest)


# Least weight
least = vehicles[0]
for v in vehicles:
    if v['weight'] < least['weight']:
        least = v

print("\nVehicle with least weight:")
print(least)


# Average on-road price
total = 0
for v in vehicles:
    total += v['onroad']

average = total / n
print("\nAverage on-road price:", average)


# Vehicles above average price
count = 0
for v in vehicles:
    if v['onroad'] > average:
        count += 1

print("Vehicles above average price:", count)


# Vehicles above given weight
limit = float(input("\nEnter weight limit: "))
count = 0
for v in vehicles:
    if v['weight'] > limit:
        count += 1

print("Vehicles above given weight:", count)


# Vehicles within budget
budget = float(input("\nEnter budget: "))
count = 0
for v in vehicles:
    if v['onroad'] <= budget:
        count += 1

print("Vehicles within budget:", count)

