import json
import os

import requests

abs_path = os.path.abspath("fixtures/testers.json")
with open(abs_path) as file:
    testers = json.load(file)
tester_account = testers[5]['marky']['prod_main']
print(tester_account)
catch_otp_url = "https://api.kumuapi.com/v1/sms/retrieve-otp-codes"
api_key = os.environ.get('OTP_API_KEY')
print(api_key)
response = requests.get(catch_otp_url,
                        headers={"otp-secret-key": api_key},
                        params={"cellphone": tester_account,
                                "country_code": "63",
                                "rate_limit": 2})
response_json = response.json()
print(response_json)
# otp_value = response_json['data'][0]['verification_code']
