from flask import Blueprint, render_template
from flask_login import current_user

main_bp = Blueprint(
    "main",
    __name__
)


@main_bp.route("/")
def index():
    return render_template(
        "index.html"
    )


@main_bp.route("/dashboard")
def dashboard():

    if not current_user.is_authenticated:
        return render_template(
            "dashboard.html",
            stats=None
        )

    return render_template(
        "dashboard.html",
        stats=current_user.stats
    )