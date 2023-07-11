import pytest
from Docker.modules.indeed_soup import get_linkedIn_search_url

def test_get_linkedIn_search_url():
  assert get_linkedIn_search_url() == None