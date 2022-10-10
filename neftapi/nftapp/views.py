from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json

def index(request):
    url = "https://api.verbwire.com/v1/nft/userOps/deployedContracts"
  

    payload={}
    headers = {
    'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
    'accept': 'application/json'
    }
    response = requests.request("GET", url , headers=headers, data=payload)
    # data = json.loads(response.text)
    return HttpResponse (response)
    # print(response.contractName)
    
    # return JsonResponse(response, safe=False) 
    

def address_to_allowlist(request):

    
    url = "https://api.verbwire.com/v1/nft/update/addToAllowList"

    payload='chain=rinkeby&contractAddress=india&addresses=0x33145a8499e89b6E0839d237A3056A3735cCaeD5%2C%20%200x54D404D5870Bdf67B2CFcE5f800D253E9A8B686e%2C%200x3B834EDe1a8c1f130c056a92eb5f1483cF4e8517%2C%200x36D549D8450Bdf67B2CFcE5f800D296E9A8B639f&mintSlots=11%2C%2013%2C7%2C%2088'
    headers = {
    'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return HttpResponse (response.text)

def deploy_contract(request):
    
    url = "https://api.verbwire.com/v1/nft/update/initCollectionContract"

    payload={'metadataFrozen': 'false',
    'chain': 'rinkeby',
    'contractAddress': '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d',
    'maxMintPerAddress': '5',
    'totalReserveQty': '500',
    'totalAllowlistQty': '100',
    'maxSupply': '1000',
    'maxMintableBatchSize': '5',
    'royaltiesInBps': '100',
    'royaltiesAddress': '1.048089544248271e+48',
    'ownerAddress': '1.048089544248271e+48',
    'baseTokenURI': 'https://ikzttp.mypinata.cloud/ipfs/QmQFkLSQysj94s5GvTHPyzTxrawwtjgiiYS2TBLgrvw8CW/40',
    'allowListMintStartTime': '1658167690',
    'publicSaleStartTime': '1658167690',
    'allowlistMintPriceInWei': '11',
    'publicPriceInWei': '1'}
    files=[

    ]
    headers = {
    'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
    'accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    return HttpResponse(response)

# def mint_image(request):
  
#     url = "https://api.verbwire.com/v1/nft/mint/quickMintFromFile"

#     payload={'allowPlatformToOperateToken': 'true',
#     'chain': 'rinkeby',
#     'name': 'SampleNFTName',
#     'description': 'Sample Description',
#     'recipientAddress': 'tt'}
#     files=[
#     ('filePath',('pexels-ovan-57690 (1).jpg',open('/C:/Users/Dell/Downloads/pexels-ovan-57690 (1).jpg','rb'),'image/jpeg'))
#     ]
#     headers = {
#     'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
#     'accept': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload, files=files)

#     print(response.text)
#     return HttpResponse(response)


def custom_contract(request):
    url = "https://api.verbwire.com/v1/nft/deploy/deployCustomContract"

    payload={'chain': 'rinkeby',
    'contractSymbol': 'ILL',
    'contractName': 'illuminati Owls',
    'recipientAddress': '0x33145a6258e89b6E0796d237A3048A3852cCaeQ7'}
    files=[

    ]
    headers = {
    'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
    'accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    return HttpResponse(response)


