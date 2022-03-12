from instagram_private_api import Client, ClientCompatPatch, ClientError, ClientLoginError
import hashlib
# Without any authentication

# Some endpoints, e.g. user_following are available only after authentication

authed_web_api = Client(
    auto_patch=True, authenticate=True,
    username='dcsdcdscd', password='qasimov124')

following = authed_web_api.username_info('irshad')
print(following)

for user in following:
    print(user['username'])