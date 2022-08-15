from flask import Blueprint
from app.users.controller import UserList, UserId, UserLogin

user_api = Blueprint('user_api', __name__)

user_api.add_url_rule(
    '/users',
    view_func=UserList.as_view('user_list'),
    methods=['GET', 'POST']
)

user_api.add_url_rule(
    '/users/<int:id>',
    view_func=UserId.as_view('user_id'),
    methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
)

user_api.add_url_rule(
    '/login',
    view_func=UserLogin.as_view('user_login'),
    methods=['POST']
)