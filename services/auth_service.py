from models.user import User

class AuthService:
    def login(self, username: str, password: str) -> dict:
        if User.verify_user(username, password):
            return {
                'success': True,
                'message': '登录成功!'
            }
        return {
            'success': False,
            'message': '登录失败: 用户名或密码错误'
        }
    
    def register(self, username: str, password: str) -> dict:
        return User.create_user(username, password)