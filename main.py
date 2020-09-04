# from googleapiclient.discovery import build
# from google.oauth2 import service_account


# # credentials = service_account.Credentials.from_service_account_file(django.conf.settings.GOOGLE_ACCOUNT_KEYS)
# path = '/Users/enrique/Desktop/key.json'
# credentials = service_account.Credentials.from_service_account_file(path,scopes=['https://www.googleapis.com/auth/androidpublisher'],)
# str_dict = str(credentials.__dict__)
# #Build the "service" interface to the API you want
# service = build("androidpublisher", "v3", credentials=credentials)
# str_dict2 = str(service.__dict__)
# # result = service.inappproducts().get(packageName="cam.app.volumeup", sku="testprod01").execute()
# # import pdb
# # pdb.set_trace()
# packageName = 'cam.app.volumeup'
# productId = 'testprod01'
# token = 'iifakklhamfniekjnijgheji.AO-J1OzR-eaVISzrqxHYSfWzki7SLYJ2ZCQ7X_SZgLvHfpy2sbw7CR4wwOHJKWQTn8mE778gpUfOw9upnTPcK-EM-ROc7MzH5pzvrW18I1CdIXkLNhTo3sE'
# # #Use the token your API got from the app to verify the purchase
# # result2 = service.purchases().subscriptions().get(packageName="your.app.package.id", subscriptionId="sku.name", token="token-from-app").execute()
# import pdb
# pdb.set_trace()
# result2 = service.purchases.products.get(packageName=packageName, productId=productId, token=token).execute()
# #
# str_dict2 = str(service.__dict__)
# print(str_dict2)
import httplib2
import googleapiclient.errors
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/enrique/Desktop/key.json', scopes='https://www.googleapis.com/auth/androidpublisher')

http = httplib2.Http()
http = credentials.authorize(http)

service = build("androidpublisher", "v3", http=http)
purchases = service.purchases()
products = purchases.products()
packageName = 'cam.app.volumeup'
productId = 'testprod01'
token = '1iifakklhamfniekjnijgheji.AO-J1OzR-eaVISzrqxHYSfWzki7SLYJ2ZCQ7X_SZgLvHfpy2sbw7CR4wwOHJKWQTn8mE778gpUfOw9upnTPcK-EM-ROc7MzH5pzvrW18I1CdIXkLNhTo3sE'
get = products.get(
    packageName=packageName,
    productId=productId,
    token=token
)
try:
    result = get.execute()
    print(result)
except googleapiclient.errors.HttpError as e:
    print(e.content)
    pass
