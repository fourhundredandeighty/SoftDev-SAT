import pytest
import logingui
from logingui import register_user
import os



class TestLoginVerify:

    # Tests that the function verifies login credentials with correct username and password.
    def test_login_with_correct_credentials(self):
        logingui.username_verify.set("correct_username")
        logingui.password_verify.set("correct_password")
        logingui.login_verify()
        assert logingui.login_success_screen is not None

    # Tests that the function handles empty username and password fields.
    def test_login_with_empty_fields(self):
        logingui.username_verify.set("")
        logingui.password_verify.set("")
        logingui.login_verify()
        assert logingui.user_not_found_screen is not None

    # Tests that the function handles an empty username field.
    def test_login_with_empty_username(self):
        logingui.username_verify.set("")
        logingui.password_verify.set("password")
        logingui.login_verify()
        assert logingui.user_not_found_screen is not None

    # Tests that the function handles an empty password field.
    def test_login_with_empty_password(self):
        logingui.username_verify.set("username")
        logingui.password_verify.set("")
        logingui.login_verify()
        assert logingui.password_not_recog_screen is not None

    # Tests that the function handles a non-existent username.
    def test_login_with_nonexistent_username(self):
        logingui.username_verify.set("nonexistent_username")
        logingui.password_verify.set("password")
        logingui.login_verify()
        assert logingui.user_not_found_screen is not None