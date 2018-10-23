import requests


 

while 1 :

    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    test = r.json()
     


    if test.get('bpi').get('USD').get('rate') > '7000' :

       
        print("wow Price is too much  : ")
  
  
    print("bitcoin Price is :" + test.get('bpi').get('USD').get('rate')+" $")
