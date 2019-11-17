# Leaking Phone Number
The api at https://www.flipkart.com/api/6/user/signup/status on signup allows attacker to check existence of more than 1 phone numbers (10 at max), thus it enables attacker to leak thousands of phone numbers present in flipkart database in mere hundreds of requests.
The domain is not rate limited so it becomes very easy to leak phone numbers of users.
So with some iteration we can leak around 300 numbers per minute, thus can potentially leak their whole database in one night.

I have added two scripts which take 2 different approach to leak, one used random int to generate phone number other iterates through to generate phone number.

## Installation
The script runs on both python2 and python3, it requires requests and json as external modules
```
pip install requests json
```
