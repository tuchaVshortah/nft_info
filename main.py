import psycopg2
from flask import Flask
import argparse
import requests


def main(): 
    parser = argparse.ArgumentParser(prog="nftinfo", description="A tool to get information about NFT tokens")

    conn = psycopg2.connect(dbname="nftdb", user="postgres", 
                            password="root", host="localhost", port=5432)

    cursor = conn.cursor()

    print("OK")

