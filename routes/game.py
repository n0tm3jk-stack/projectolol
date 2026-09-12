from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    session
)

from flask_login import (
    login_required,
    current_user
)
from extensions import db
from models import Attempt
from game_engine import GameEngine


game_bp = Blueprint(
    "game",
    __name__,
    url_prefix="/game"
)


@game_bp.route("/")
@login_required
def game():

    return render_template(
        "game.html"
    )


@game_bp.route(
    "/api/start",
    methods=["POST"]
)
@login_required
def start_game():

    data = request.get_json() or {}

    countries = data.get(
        "countries",
        []
    )

    target = GameEngine.choose_country(
        countries
    )

    if not target:
        return jsonify({
            "error": "No se recibieron países válidos."
        }), 400

    session["score"] = 0
    session["target_country"] = target

    current_user.stats.games_played += 1

    db.session.commit()

    return jsonify({
        "target": target,
        "score": 0
    })


@game_bp.route(
    "/api/round",
    methods=["POST"]
)
@login_required
def new_round():

    data = request.get_json() or {}

    countries = data.get(
        "countries",
        []
    )

    target = GameEngine.choose_country(
        countries
    )

    if not target:
        return jsonify({
            "error": "Lista de países vacía."
        }), 400

    session["target_country"] = target

    return jsonify({
        "target": target,
        "score": session.get(
            "score",
            0
        )
    })


@game_bp.route(
    "/api/answer",
    methods=["POST"]
)
@login_required
def check_answer():

    data = request.get_json() or {}

    clicked_country = data.get(
        "country",
        ""
    )

    target_country = session.get(
        "target_country"
    )

    if not target_country:

        return jsonify({
            "error": "No existe una ronda activa."
        }), 400

    correct = GameEngine.check_answer(
        target_country,
        clicked_country
    )

    current_score = session.get(
        "score",
        0
    )

    if correct:

        current_score += 1

        session["score"] = current_score

        current_user.stats.correct_answers += 1
        current_user.stats.total_score += 1

        if current_score > current_user.stats.best_score:
            current_user.stats.best_score = current_score

    else:

        current_user.stats.wrong_answers += 1

    attempt = Attempt(
        user_id=current_user.id,
        target_country=target_country,
        clicked_country=clicked_country,
        correct=correct
    )

    db.session.add(attempt)
    db.session.commit()

    return jsonify({

        "correct": correct,

        "clicked": clicked_country,

        "target": target_country,

        "score": current_score,

        "stats": current_user.stats.to_dict()
    })


@game_bp.route(
    "/api/stats",
    methods=["GET"]
)
@login_required
def stats():

    return jsonify(
        current_user.stats.to_dict()
    )