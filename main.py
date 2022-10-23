import psycopg2
from flask import Flask
import argparse
import requests


def main(): 
    parser = argparse.ArgumentParser(prog="nftinfo", description="A tool to get information about NFT tokens")
    search_methods = parser.add_mutually_exclusive_group()

    search_methods.add_argument(
        "-b", "--block",
        help="Get NFT transfers by block",
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-a", "--address-nfts",
        help="Get NFTs by wallet",
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-At", "--address-nft-transfers",
        help="Get NFT transfers by wallet",
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-Ac", "--address-nft-collections",
        help="Get collections by wallet",
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-AT", "--address-nft-trades",
        help="Get trades from opensea marketplace",
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-Al", "--address-nft-lprice",
        help="Get lowest price",
        type=str,
        nargs=1
    )

    search_methods.add_argument(
        "-s", "--search",
        help="Search for a NFT token",
        type=str,
        nargs="+"
    )

    args = parser.parse_args()
    
    """
    conn = psycopg2.connect(dbname="nftdb", user="postgres", 
                            password="root", host="localhost", port=5432)

    cursor = conn.cursor()
    """

main()