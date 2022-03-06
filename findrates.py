# findrates.py
import easypost
easypost.api_key = "API_KEY"

# Get and verify to and from addresses

to_address = None
from_address = None

print()
print("Enter the \"To address\". It is recommended to provide as much\n"
	"information as possible. If not applicable, simply omit.\n")


while(True):
	try:
		to_address = easypost.Address.create(
			verify_strict=["delivery"],
			name = input("Name: "),
			street1 = input("Street 1: "),
			street2 = input("Street 2: "),
			city = input("City: "),
			state = input("State: "),
			zip = input("Zip: "),
			country = input("Country: "),
			company = input("Company: "),
			phone = input("Phone: "),
			email = input("Email: "),
			residential = input("Residential (t/f/null): "),
			carrier_facility = input("Carrier Facility: "),
			federal_tax_id = input("Federal Tax ID: "),
			state_tax_id = input("State Tax ID: "),
		)
	except easypost.Error as e:
		print()
		print(str(e))
		if e.param is not None:
			print(f"Invalid parameter: {e.param}")
		print("Please try again.\n")
	else:
		break

print()
print("Enter the \"From address\". It is recommended to provide as much\n"
	"information as possible. If not applicable, simply omit.\n")

while(True):
	try:
		from_address = easypost.Address.create(
			verify_strict=["delivery"],
			name = input("Name: "),
			street1 = input("Street 1: "),
			street2 = input("Street 2: "),
			city = input("City: "),
			state = input("State: "),
			zip = input("Zip: "),
			country = input("Country: "),
			company = input("Company: "),
			phone = input("Phone: "),
			email = input("Email: "),
			residential = input("Residential (t/f/null): "),
			carrier_facility = input("Carrier Facility: "),
			federal_tax_id = input("Federal Tax ID: "),
			state_tax_id = input("State Tax ID: "),
		)
	except easypost.Error as e:
		print()
		print(str(e))
		if e.param is not None:
			print(f"Invalid parameter: {e.param}")
		print("Please try again.\n")
	else:
		break

# Create parcel measurements

# Weight is always required, regardless of if parcel is predefined package or not
print()
weight = 0
while(True):
	try:
		# round input to one digit
		weight = round(float(input("Please enter the weight of the parcel (oz): ")),1)
	except ValueError:
		print("Please enter a valid weight.\n")
	else:
		break

# Specify if the package is a predefined size or not.
# For the sake of this demo, this is just a small list of the USPS options
print()
predefined = 0
length = 0
width = 0
height = 0

# Note: options are 1 based index
predefined_options = [
	"Card",
	"Letter",
	"Flat",
	"FlatRateEnvelope",
	"FlatRateLegalEnvelope",
	"FlatRatePaddedEnvelope",
	"FlatRateGiftCardEnvelope",
	"FlatRateWindowEnvelope",
	"FlatRateCardboardEnvelope",
	"SmallFlatRateEnvelope",
	"Parcel",
	"LargeParcel",
	"IrregularParcel",
	"SoftPack",
	"SmallFlatRateBox",
	"MediumFlatRateBox",
	"LargeFlatRateBox"
	]

print("Please enter the number that corresponds with your predefined package\n"
	"name. If your parcel is not a predefined package, enter 0.")
print("[0] N/A")
for i in range(len(predefined_options)):
	print(f"[{i+1}] {predefined_options[i]}")

print()
while(True):
	try:
		predefined = int(input("Please enter your number: "))
		if predefined < 0 or predefined > len(predefined_options):
			raise ValueError
	except ValueError:
		print("Please enter a valid number.\n")
	else:
		break

# Create Parcel

parcel = None

if predefined > 0:
	parcel = easypost.Parcel.create(
		predefined_package = predefined_options[predefined-1],
		weight = weight
		)
else:
	print()
	while(True):
		try:
			# round inputs to one digit
			length = round(float(input("Enter length (inches): ")),1)
			if length <= 0: raise ValueError

			width = round(float(input("Enter width (inches): ")),1)
			if width <= 0: raise ValueError

			height = round(float(input("Enter height (inches): ")),1)
			if height <= 0: raise ValueError

		except ValueError:
			print("Please enter a valid number.\n")
		else:
			break
	parcel = easypost.Parcel.create(
		length = length,
		width = width,
		height = height,
		weight = weight
		)

# Create a shipment
shipment = easypost.Shipment.create(
	to_address = to_address,
	from_address = from_address,
	parcel = parcel
	)

# Ideally, I'd have a full list of the possible currencies
# For the sake of this demo, I've only included a small handful
currency_symbol = {
	"USD" : "$",
	"GBP" : "£",
	"CNY" : "¥",
	"KRW" : "₩",
	"MXN" : "$",
	"JPY" : "¥",
	"CAD" : "$"
}

# Print rates, estimated delivery
for i, rate in enumerate(shipment.rates):
	print(f"[{i+1}]:")
	print(f"  Carrier: {rate.carrier}")
	print(f"  Currency: {rate.list_currency}")
	print(f"  Rate: {currency_symbol[rate.list_currency]}{rate.rate}")
	print(f"  Estimated Delivery Days: {rate.est_delivery_days}")
	print()
