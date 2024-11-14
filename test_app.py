from app import app

def test_home():
    # 测试主页是否返回 200 状态码
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data == b"Hello, CI/CD!"
