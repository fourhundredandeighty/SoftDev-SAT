import pytest
import logingui
from logingui import register_user
import os



class TestRegister:

    # Tests that the register function successfully registers a user with valid credentials
    def test_register_valid_credentials(self):
        # Set up
        logingui.username_entry.insert(0, "test_user")
        logingui.password_entry.insert(0, "test_password")

        # Call the function
        register_user()

        # Assert
        assert os.path.exists("test_user")
        file = open("test_user", "r")
        contents = file.read()
        assert contents == "test_user\ntest_password"
        file.close()

        # Clean up
        os.remove("test_user")

    # Tests that the register function does not register a user when the username and password are empty
    def test_register_empty_credentials(self):
        # Set up
        logingui.username_entry.insert(0, "")
        logingui.password_entry.insert(0, "")

        # Call the function
        register_user()

        # Assert
        assert not os.path.exists("")

    # Tests that the register function does not register a user when the username already exists
    def test_register_existing_username(self):
        # Set up
        logingui.username_entry.insert(0, "existing_user")
        logingui.password_entry.insert(0, "test_password")
        file = open("existing_user", "w")
        file.write("existing_user\nexisting_password")
        file.close()

        # Call the function
        register_user()

        # Assert
        assert os.path.exists("existing_user")
        file = open("existing_user", "r")
        contents = file.read()
        assert contents == "existing_user\nexisting_password"
        file.close()

        # Clean up
        os.remove("existing_user")

    # Tests that the register function does not register a user when the password is too short
    def test_register_short_password(self):
        # Set up
        logingui.username_entry.insert(0, "test_user")
        logingui.password_entry.insert(0, "short")

        # Call the function
        register_user()

        # Assert
        assert not os.path.exists("test_user")

    # Tests that the register function does not register a user when the password is too long
    def test_register_long_password(self):
        # Set up
        logingui.username_entry.insert(0, "test_user")
        logingui.password_entry.insert(0, "this_password_is_too_long_to_be_registered")

        # Call the function
        register_user()

        # Assert
        assert not os.path.exists("test_user")

    # Tests that the register function successfully registers a user with a username and password containing special characters
    def test_register_special_characters(self):
        # Set up
        logingui.username_entry.insert(0, "!@#$%^&*")
        logingui.password_entry.insert(0, "!@#$%^&*")

        # Call the function
        register_user()

        # Assert
        assert os.path.exists("!@#$%^&*")
        file = open("!@#$%^&*", "r")
        contents = file.read()
        assert contents == "!@#$%^&*\n!@#$%^&*"
        file.close()

        # Clean up
        os.remove("!@#$%^&*")