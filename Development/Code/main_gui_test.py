
from logging import root
import subprocess
import pytest
import logingui
import os

class TestMainGui:

    # Tests that the function destroys the login_success_screen, login_screen, and root windows
    def test_destroy_windows(self):
        logingui.main_gui()
        assert logingui.login_success_screen.winfo_exists() == False
        assert logingui.login_screen.winfo_exists() == False
        assert root.winfo_exists() == False

    # Tests that the function runs the main_gui.py script using the subprocess module
    def test_run_subprocess(self):
        logingui.main_gui()
        subprocess.run.assert_called_with(["python", "main_gui.py"], check=True)

    # Tests that the function handles an error when running the subprocess
    def test_subprocess_error(self):
        subprocess.run.side_effect = subprocess.CalledProcessError(1, "python", "Error")
        logingui.main_gui()
        assert subprocess.run.called
        assert "Error running the script" in logingui.capsys.readouterr().out