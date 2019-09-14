def test_logout(self):
    try:
        print("tried")
        login_object = LoginPage()
        login_object.logout(self)
    except Exception:
        pytest.fail("Logout failed, user not logged in")
