
import ovh

# Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
# to get your credentials
ck = ovh.consumer_key
client = ovh.Client(
    endpoint='ovh-eu',
    application_key='vv9BSskHyMiyYhJz',
    application_secret='0RqZwvLkAt3vNdBN8MHDbCcn1LLLOftB',
    consumer_key=ck,
)

# Print nice welcome message
print("Welcome", client.get('/me')['firstname'])
"""

import json
import ovh

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='vv9BSskHyMiyYhJz',    # Application Key
    application_secret='0RqZwvLkAt3vNdBN8MHDbCcn1LLLOftB', # Application Secret
    consumer_key=ovh.consumer_key(),       # Consumer Key
)

result = client.post('/me/subAccount/{id}/createConsumerKey')

# Pretty print
print json.dumps(result, indent=4)"""