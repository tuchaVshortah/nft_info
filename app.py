from flask import Flask, render_template, request
import handler
from validators import url, ValidationFailure
import json

app = Flask(__name__)

@app.route("/search.html")
@app.route("/")
def index():

    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():

    
    search = request.form["search"]

    result = handler.handler(search)
    

    data = []
    for element in result["result"]:
        metadata_nested = json.loads(element["metadata"])


        name = "no name"
        image = "/static/broken_image.png"
        description = "No description"
        token_uri = "#"


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
            token_uri = metadata_nested["token_uri"]


        try:
            if(url(parsed)):
                image = parsed
        except ValidationFailure as e:
            print("couldn't parse a valid url for this token: " + token_uri)
            
        
        new_element = {
            "name": metadata_nested["name"],
            "image": image,
            "description": description,
            "token_uri": token_uri
        }


        data.append(new_element)


    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()