from flask import Flask, render_template, request
import handler
from validators import url, ValidationFailure
import json

import db

app = Flask(__name__)

@app.route("/search", methods=["GET"])
@app.route("/search.html", methods=["GET"])
@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():

    
    search = request.form["search"]

    result = handler.handler(search)
    

    data = []
    for element in result["result"]:
        metadata_nested = json.loads(element["metadata"])

        token_id = "NULL"
        contract_type = "NULL"
        block_number_minted = "NULL"
        minter_address = "NULL"
        name = "no name"
        image = "/static/broken_image.png"
        description = "No description"
        token_uri = "#"

        
        if("token_id" in element and element["token_id"] is not None):
            token_id = element["token_id"]


        if("contract_type" in element and element["contract_type"] is not None):
            contract_type = element["contract_type"]

        if("block_number_minted" in element and element["block_number_minted"] is not None):
            block_number_minted = element["block_number_minted"]

        if("minter_address" in element and element["minter_address"] is not None):
            minter_address = element["minter_address"]

        if("name" in metadata_nested and metadata_nested["name"] is not None):
            name = metadata_nested["name"]


        if("image" in metadata_nested and metadata_nested["image"] is not None):
            parsed = metadata_nested["image"]
        elif("image_url" in metadata_nested and metadata_nested["image_url"] is not None):
            parsed = metadata_nested["image_url"]
        elif("image_url_cdn" in metadata_nested and metadata_nested["image_url_cdn"] is not None):
            parsed = metadata_nested["image_url_cdn"]
        elif("image_url_png" in metadata_nested and metadata_nested["image_url_png"] is not None):
            parsed = metadata_nested["image_url_png"]
        

        if("description" in metadata_nested and metadata_nested["description"] is not None):
            description = metadata_nested["description"]


        if("token_uri" in metadata_nested and metadata_nested["token_uri"] is not None):
            token_uri = element["token_uri"]


        try:
            if(url(parsed)):
                image = parsed
        except ValidationFailure as e:
            print("couldn't parse a valid url for this token: " + token_uri)
            
        
        new_element = {
            "token_id": token_id,
            "contract_type": contract_type,
            "block_number_minted": block_number_minted,
            "minter_address": minter_address,
            "name": name,
            "image": image,
            "description": description,
            "token_uri": token_uri
        }


        data.append(new_element)


    db.save(data)

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()