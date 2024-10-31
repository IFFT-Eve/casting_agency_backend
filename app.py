# import os
from flask import Flask, request, jsonify, abort

# from sqlalchemy import exc
from flask_cors import CORS

from model.model import setup_db, Actor, Movie
from dateutil import parser

from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


# ROUTES
@app.route("/actors", methods=["GET"])
@requires_auth("get:actors")
def getAllActors(payload):
    # try:
        actors = Actor.query.all()
        print()
        format_actors = [actor.format() for actor in actors]
        return jsonify({"success": True, "data": format_actors})
    # except:
    #     abort(404)


@app.route("/actors/<int:id>", methods=["GET"])
@requires_auth("get:actors")
def getActorDetail(payload, id):
    try:
        actor = Actor.query.filter(Actor.id == id).first()
        return jsonify({"success": True, "data": actor.format()})
    except:
        abort(404)


@app.route("/create-actor", methods=["POST"])
@requires_auth("post:actors")
def createActor(payload):
    try:
        body = request.json
        name = body["name"]
        age = body["age"]
        gender = body["gender"]
        actor = Actor(name=name, age=age, gender=gender)
        actor.insert()
        return jsonify({"success": True, "data": {"update_count": 1}})
    except:
        abort(404)


@app.route("/update-actor", methods=["PATCH"])
@requires_auth("patch:actors")
def updateActor(payload):
    try:
        body = request.json
        id = body["id"]
        name = body["name"]
        age = body["age"]
        gender = body["gender"]
        actor = Actor.query.filter(Actor.id == id).first()
        if actor == None:
            abort(404)
        else:
            actor.name = name
            actor.age = age
            actor.gender = gender
            actor.update()
            return jsonify({"success": True, "data": {"update_count": 1}})
    except:
        abort(404)


@app.route("/actors/<int:id>", methods=["DELETE"])
@requires_auth("delete:actors")
def deleteActor(payload, id):
    try:
        actor = Actor.query.filter(Actor.id == id).first()
        if actor == None:
            abort(404)
        else:
            actor.delete()
        return jsonify({"success": True, "data": {"delete_count": 1}})
    except:
        abort(404)


# ROUTES
@app.route("/movies", methods=["GET"])
@requires_auth("get:movies")
def getAllMovies(payload):
    try:
        movies = Movie.query.all()
        format_movies = [movie.format() for movie in movies]
        return jsonify({"success": True, "data": format_movies})
    except:
        abort(404)


@app.route("/movies/<int:id>", methods=["GET"])
@requires_auth("get:movies")
def getMovieDetail(payload, id):
    try:
        movie = Movie.query.filter(Movie.id == id).first()
        return jsonify({"success": True, "data": movie.format()})
    except:
        abort(404)


@app.route("/create-movie", methods=["POST"])
@requires_auth("post:movies")
def createMovie(payload):
    try:
        body = request.json
        title = body["title"]
        release_date = parser.parse(body["release_date"])
        movie = Movie(title=title, release_date=release_date)
        movie.insert()
        return jsonify({"success": True, "data": {"update_count": 1}})
    except:
        abort(404)


@app.route("/update-movie", methods=["PATCH"])
@requires_auth("patch:movies")
def updateMovie(payload):
    try:
        body = request.json
        id = body["id"]
        title = body["title"]
        release_date = body["release_date"]
        movie = Movie.query.filter(Movie.id == id).first()
        if movie == None:
            abort(404)
        else:
            movie.title = title
            movie.release_date = release_date
            movie.update()
            return jsonify({"success": True, "data": {"update_count": 1}})
    except:
        abort(404)


@app.route("/movies/<int:id>", methods=["DELETE"])
@requires_auth("delete:movies")
def deleteMovie(payload, id):
    try:
        movie = Movie.query.filter(Movie.id == id).first()
        if movie == None:
            abort(404)
        else:
            movie.delete()
        return jsonify({"success": True, "data": {"delete_count": 1}})
    except:
        abort(404)


# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({"success": False, "error": 422, "message": error.description}), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False, "error": 404, "message": error.description}), 404


@app.errorhandler(400)
def not_found(error):
    return jsonify({"success": False, "error": 400, "message": error.description}), 400


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
