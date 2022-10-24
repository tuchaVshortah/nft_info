import nft_info
import db
from json import *

def handler(search: str) -> dict:
    result = nft_info.nft_info("search", search)

    #add functionality to save the result if it wasn't already saved in the database
    result_data = loads(result)
    return result_data

handler("boots")