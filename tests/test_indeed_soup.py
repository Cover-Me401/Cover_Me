import pytest
from Docker.modules.indeed_soup import get_indeed_search_url


# Testing for get_indeed_search_url (indeed_soup module)
def test_get_indeed_search_url():
  assert get_indeed_search_url() == None