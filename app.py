from flask import Flask
from flask_restful import Api, Resource, reqparse

app=Flask(__name__)
api=Api(app)

anime=[
    {"id":1,"name":"One piece", "genere":"Adventure"},
    {"id":2,"name":"Dragon ball super", "genere":"Action"},
]

animeParser=reqparse.RequestParser()
animeParser.add_argument("name",type=str,help="Name of the Anime", location='form')
animeParser.add_argument("genere", type=str, help="Genere of the Anime", location='form')

class AnimeCollectionList(Resource):
    def get(self):
        return {"anime":anime}
    def post(self):
        doc=animeParser.parse_args()
        newAnime={
            "id":len(anime)+1,"name":doc['name'],"genere":doc["genere"]
        }
        anime.append(newAnime)
        return {"Anime":newAnime},201
    
class AnimeCollection(Resource):
    def get(self,id):
        singleAnime=next((item  for item in anime if item["id"] == id),None)
        if singleAnime:
            return {"anime":singleAnime}
        return {"error":"Not found"},404

    def put(self,id):
        singleAnime=next((item for item in anime if item["id"] ==id),None)
        if singleAnime:
            doc=animeParser.parse_args()
            singleAnime['name']=doc['name'] or singleAnime['name']
            singleAnime['genere']=doc['genere'] or singleAnime['genere']
            return{"anime":singleAnime}
        return {"error":"Not found"},404

    def delete(self,id):
        global anime
        anime=[item for item in anime if item["id"] != id]
        return {"message":"Anime deleted"}

api.add_resource(AnimeCollectionList,'/')
api.add_resource(AnimeCollection,'/<int:id>')

if __name__=='__main__':
    app.run(debug=True)