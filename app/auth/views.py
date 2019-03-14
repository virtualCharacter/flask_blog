from flask import render_template,flash, redirect,url_for, session
from ..models import  db
from . import auth
from .forms import LoginForm, ReigisterForm
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        telephone = loginForm.telephone.data
        password = loginForm.password.data
        user = User.query.filter_by(telephone=telephone, password=password).first()
        #登录
        if user:
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        else:
            flash('用户名或密码错误，请重新输入')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', loginForm=loginForm)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = ReigisterForm()
    if registerForm.validate_on_submit():
        telephone = registerForm.telephone.data
        user = User.query.filter_by(telephone=telephone).first()
        #确认电话号码的唯一性
        if user:
            flash("该号码已经被注册")
            return redirect(url_for('auth.register'))

        username = registerForm.username.data
        password = registerForm.password1.data
        #注册新用户
        newUser = User(telephone=telephone, username=username, password=password)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registerForm=registerForm)

@auth.route('/logout')
def logout():
    del session['user_id']
    return redirect(url_for('main.index'))
