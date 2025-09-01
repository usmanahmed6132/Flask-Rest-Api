from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

videos = {}

class Video(Resource):
    def get(self, video_id):
        if video_id not in videos:
            return {"error": "Video not found"}, 404
        return {"id": video_id, **videos[video_id]}, 200

    def post(self, video_id):
        if video_id in videos:
            return {"error": "Video id already exists"}, 409
        data = request.get_json() or {}
        required = {"name", "likes", "views"}
        missing = [k for k in required if k not in data]
        if missing:
            return {"error": f"Missing fields: {', '.join(missing)}"}, 400
        videos[video_id] = {
            "name": str(data["name"]),
            "likes": int(data["likes"]),
            "views": int(data["views"]),
        }
        return {"message": "created", "id": video_id, **videos[video_id]}, 201

    def put(self, video_id):
        if video_id not in videos:
            return {"error": "Video not found"}, 404
        data = request.get_json() or {}
        v = videos[video_id]
        if "name" in data:  v["name"]  = str(data["name"])
        if "likes" in data: v["likes"] = int(data["likes"])
        if "views" in data: v["views"] = int(data["views"])
        return {"message": "updated", "id": video_id, **v}, 200

    def delete(self, video_id):
        if video_id not in videos:
            return {"error": "Video not found"}, 404
        del videos[video_id]
        return {"message": f"Video {video_id} deleted"}, 200


class VideoList(Resource):
    def get(self):
        return {"videos": [{"id": vid, **data} for vid, data in videos.items()]}, 200

api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(VideoList, "/videos")

if __name__ == "__main__":
    app.run(debug=True)
