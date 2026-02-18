# A dictionary can contain dictionaries, this is called nested dictionary.

my_certs = {
    "cert1": {"name": "CCNP DC", "year": 2024},
    "cert2": {"name": "AZ-700", "year": 2025},
    "cert3": {"name": "Palo-Alto", "year": 2025},
}
print(my_certs)


# We can create mutliple dictionaries, then create on dictionary that will contain the other multiple dictionaries.

my_org1 = {"name": "ORG-1", "year": 2023}

my_org2 = {"name": "ORG-2", "year": 2024}

my_org3 = {"name": "ORG-3", "year": 2025}

# Here we are creating one dictionary that contains the above 3 dictionaries.
exp = {"my_org1": my_org1, "my_org2": my_org2, "my_org3": my_org3}
print(exp)

# Accessing Items in Nested dictionaries.

print(my_certs["cert1"]["year"])

# Loop through Nested Dictionaries

for cert, vendor in my_certs.items():
    print(f" {cert} {vendor}")
