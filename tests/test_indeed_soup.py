import pytest
from Docker.modules.indeed_scraper.indeed_soup import get_indeed_search_url


# Testing for get_indeed_search_url (indeed_soup module)
@pytest.mark.skip
def test_get_indeed_search_url():
  assert get_indeed_search_url() == None

@pytest.mark.skip
def test_num_jobs_returned():
    expected_num_jobs = 100
    actual_num_jobs = len(jobs)
    assert expected_num_jobs == actual_num_jobs
    

@pytest.mark.skip
def test_job_title():
    expected_job_title = "Python Developer"
    actual_job_title = job_item['job_title']
    assert expected_job_title == actual_job_title

@pytest.mark.skip
def test_company_name():
    expected_company_name = "Google"
    actual_company_name = job_item['company_name']
    assert expected_company_name == actual_company_name
    

