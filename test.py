import google1

packageName = 'your.app.package.name'
productId = 'testprod01'
token_success = ''
token_failed = ''
token = 'ejfjpfihanmginjfiogihaeh.AO-J1OzSQgIdTGCU8N57g6lFT9Pxfn1bHZkLeZHQI5Wap63XwgREkzzOLl8v_bjioearxzwoKkgFSn7Ig2LtO25YYPFAJCKuxpP95CXKjfhPp-rOUIruZ5k'
order_id = 'GPA.3358-8881-3420-31614'
purchase = google1.GooglePlay()
is_valid = purchase.validatePurchase(order_id,productId,packageName,token)
print('Purchase is valid: {}'.format(is_valid))