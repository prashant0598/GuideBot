from wit import Wit

access_token ="7CCSRDII4RL7S637DTJB2SKCRLFYRCYQ"

client = Wit(access_token = access_token)

message_text = "i want sports news"

resp = client.message(message_text)

print(resp)