import pytest
from Docker.menu_run import menu_run

# Testing for menu_run (menu_run module)
@pytest.mark.skip
def test_menu_run():
  assert menu_run() == None
