from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    views = db.Column(db.Integer, nullable = False)

def __repr__(self):
    return f"Video(name= {name}, views={views}, likes={likes})"


#automatically parse through the request that's being sent 
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required = True)
video_put_args.add_argument("views", type=int, help="Views of the video", required = True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required = True)

#videos = {}

#def abort_if_video_id_doesnt_exist(video_id):
#    if video_id not in videos:
#        abort(404, message = "Could not find video..")

#def abort_if_video_exits(video_id):
#    if video_id in videos:
#        abort(409, message = "Video alreday exists with that ID.")

#resource_fields is to define how an object should be serialized
resource_fields = {'id': fields.Integer,
                    'name': fields.String,
                    'views': fields.Integer,
                    'likes': fields.Integer}



class Video(Resource):
    @marshal_with(resource_fields) #when we return value and serialize it using resource_fields
    def get(self, video_id):
        result = VideoModel.query.get(id=video_id)
        return result

    def put(self, video_id):
        args = video_put_args.parse_args()
        video = videoModel(id = video_id, name = args['name'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        return videos[video_id], 201 #201 stands for created 

    def delete(self, video_id):
        del videos[video_id]
        return '', 204 #204 stands for delted successfully
    

#this kind of represents what we call a Json format {key: value}
#<> is to define parameter that I want to be passed in
api.add_resource(Video, "/video/<int:video_id>")


#start server and start flask application
#debug=True gonna see all of that output and any logging information 
#so if anything wrong we will know why (should be put when develop)
if __name__ == "__main__":
    app.run(debug=True)  