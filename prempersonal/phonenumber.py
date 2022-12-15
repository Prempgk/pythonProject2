import phonenumbers
from phonenumbers import carrier,geocoder,timezone
mobile_num=input('Enter your mobile number:')
mobile_num=phonenumbers.parse(mobile_num)
print(timezone.time_zones_for_number(mobile_num))
print(carrier.name_for_number(mobile_num,'en'))
print(geocoder.description_for_number(mobile_num,'en'))
print('valid mobile number:',phonenumbers.is_valid_number(mobile_num))
print('Checking Possibility of mobile number:',phonenumbers.is_possible_number(mobile_num))
