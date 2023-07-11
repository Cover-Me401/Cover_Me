import pytest
from Docker.modules.monster_soup import get_monster_search_url

def test_get_monster_search_url():
  assert get_monster_search_url() == None