import psycopg2
from json import *
from flask import Flask
import argparse
import requests


def main(): 
    parser = argparse.ArgumentParser(prog="nftinfo", description="A tool to get information about NFT tokens")
    search_methods = parser.add_mutually_exclusive_group()

    parser.add_argument(
        "-k", "--moralis-api-key",
        help="Specify your API key for moralis.io",
        default=None,
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-b", "--block",
        help="Get NFT transfers by block",
        default=None,
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-a", "--address-nfts",
        help="Get NFTs by wallet",
        default=None,
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-At", "--address-nft-transfers",
        help="Get NFT transfers by wallet",
        default=None,
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-Ac", "--address-nft-collections",
        help="Get collections by wallet",
        default=None,
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-AT", "--address-nft-trades",
        help="Get trades from opensea marketplace",
        default=None,
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-Al", "--address-nft-lprice",
        help="Get lowest price",
        default=None,
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-s", "--search",
        help="Search for a NFT token",
        default=None,
        type=str,
        nargs="+"
    )

    args = parser.parse_args()

    headers = {
        "accept": "application/json",
        "X-API-Key": "test"
    }

    if(args.moralis_api_key is not None):

        moralis_api_key = args.moralis_api_key[0]

        headers["X-API-Key"] = moralis_api_key

    
    if(args.block is not None):
        block = args.block[0]

        url = "https://deep-index.moralis.io/api/v2/block/" + block + "/nft/transfers?chain=eth&limit=100"        
        response = requests.get(url, headers=headers)

        response_data = response.json()
        pretty_response = dumps(response_data, indent=2)
        
        response = pretty_response

        print(response)

    elif(args.address_nfts is not None):
        address = args.address_nfts[0]

        url = "https://deep-index.moralis.io/api/v2/" + address + "/nft?chain=eth&format=decimal"
        response = requests.get(url, headers=headers)

        response_data = response.json()
        pretty_response = dumps(response_data, indent=2)
        
        response = pretty_response

        print(response)

    elif(args.address_nft_transfers is not None):
        address = args.address_nft_transfers[0]

        url = "https://deep-index.moralis.io/api/v2/"+ address + "/nft/transfers"
        response = requests.get(url, headers=headers)

        response_data = response.json()
        pretty_response = dumps(response_data, indent=2)
        
        response = pretty_response

        print(response)

    elif(args.address_nft_collections is not None):
        address = args.address_nft_collections[0]

        url = "https://deep-index.moralis.io/api/v2/" + address + "/nft/collections"
        response = requests.get(url, headers=headers)

        response_data = response.json()
        pretty_response = dumps(response_data, indent=2)
        
        response = pretty_response

        print(response)

    elif(args.address_nft_trades is not None):
        address = args.address_nft_trades[0]

        url = "https://deep-index.moralis.io/api/v2/nft/" + address + "/trades"
        response = requests.get(url, headers=headers)

        response_data = response.json()
        pretty_response = dumps(response_data, indent=2)
        
        response = pretty_response

        print(response)

    elif(args.address_nft_lprice):
        address = args.address_nft_lprice[0]

        url = "https://deep-index.moralis.io/api/v2/nft/" + address + "/lowestprice"
        response = requests.get(url, headers=headers)

        response_data = response.json()
        pretty_response = dumps(response_data, indent=2)
        
        response = pretty_response

        print(response)

    elif(args.search is not None):
        search = args.search[0]

        url = "https://deep-index.moralis.io/api/v2/nft/search?chain=eth&format=decimal&q=" + search + "&filter=global"
        response = requests.get(url, headers=headers)

        response_data = response.json()
        pretty_response = dumps(response_data, indent=2)
        
        response = pretty_response

        print(response)
    

    """
    conn = psycopg2.connect(dbname="nftdb", user="postgres", 
                            password="root", host="localhost", port=5432)

    cursor = conn.cursor()
    """

main()