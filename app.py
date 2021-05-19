from projeto import app, db
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, login_required, logout_user
from projeto.models import User
from projeto.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    #flash('Logout realizado com sucesso!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    #if form.validate_on_submit():
    if form.validate_on_submit():
        # Grab the user from our User Models table

        user = User.query.filter_by(email=form.email.data).first()
        if user is None or user.password != form.password.data:
            return redirect(url_for('login'))
        #if user.email == form.email.data and user.password == form.password.data:
            #return redirect(url_for('home'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        user = User(name=form.name.data,
                    address=form.address.data,
                    number=form.number.data,
                    city=form.city.data,
                    state=form.state.data,
                    country_code=form.country_code.data,
                    phone=form.phone.data,
                    email=form.email.data,
                    username=form.username.data,
                    password=form.password.data,
                    #pass_confirm=form.pass_confirm.data
                    pass_confirm=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
