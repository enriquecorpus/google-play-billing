import httplib2
import googleapiclient.errors
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class GooglePlay:
    def __init__(self):
        self.key = '/Users/enrique/Desktop/key.json'
        self.scopes = 'https://www.googleapis.com/auth/androidpublisher'
        self.credentials = credentials = ServiceAccountCredentials.from_json_keyfile_name(self.key, scopes=self.scopes)
    
    def validatePurchase(self,order_id:str, product_id:str,package_name:str,token:str):
        if not product_id or not package_name or not token:
            return False
        http = httplib2.Http()
        http = self.credentials.authorize(http)
        service = build("androidpublisher", "v3", http=http)
        purchases = service.purchases()
        products = purchases.products()
        get = products.get(
            packageName=package_name,
            productId=product_id,
            token=token
        )
        try:
            #https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products#ProductPurchase
            #purchaseState = 0 : Purchased 
            #consumptionState = 0 : To make sure its not yet consumed by the app. Consumption should be made after the backed verified the purchase
            result = get.execute()
            print(result)
            return result.get('orderId') == order_id and result.get('purchaseState') == 0 and result.get('consumptionState') == 0
        except googleapiclient.errors.HttpError as e:
            print(e.content)
        return false