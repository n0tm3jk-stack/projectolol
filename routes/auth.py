from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required
)

from extensions import db
from models import User, UserStats


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip().lower()

        password = request.form.get(
            "password",
            ""
        )

        if len(username) < 3:
            flash(
                "El usuario debe tener al menos 3 caracteres.",
                "error"
            )
            return redirect(
                url_for("auth.register")
            )

        if len(password) < 6:
            flash(
                "La contraseña debe tener mínimo 6 caracteres.",
                "error"
            )
            return redirect(
                url_for("auth.register")
            )

        existing_user = User.query.filter(
            (User.username == username)
            | (User.email == email)
        ).first()

        if existing_user:
            flash(
                "El usuario o correo ya está registrado.",
                "error"
            )

            return redirect(
                url_for("auth.register")
            )

        user = User(
            username=username,
            email=email
        )

        user.set_password(password)

        db.session.add(user)
        db.session.flush()

        statistics = UserStats(
            user_id=user.id
        )

        db.session.add(statistics)

        db.session.commit()

        flash(
            "Registro completado. Ya puedes iniciar sesión.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/register.html"
    )


@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )

        user = User.query.filter_by(
            username=username
        ).first()

        if not user or not user.check_password(password):

            flash(
                "Usuario o contraseña incorrectos.",
                "error"
            )

            return redirect(
                url_for("auth.login")
            )

        login_user(user)

        return redirect(
            url_for("game.game")
        )

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(
        url_for("main.index")
    )