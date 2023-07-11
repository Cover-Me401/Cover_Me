import pytest
from Docker.modules.linkedIn_soup import get_linkedIn_search_url, LinkedJobsSpider

def test_get_linkedIn_search_url():
  assert get_linkedIn_search_url() == None

def test_start_requests():
    expected_num_jobs = 100
    actual_num_requests = len(LinkedJobsSpider().start_requests())
    assert expected_num_jobs == actual_num_requests

def test_parse_job():
    expected_job_title = "Python Developer"
    expected_company_name = "Google"
    expected_job_location = "Mountain View, CA"

    job_item = LinkedJobsSpider().parse_job(response)

    assert job_item['job_title'] == expected_job_title
    assert job_item['company_name'] == expected_company_name
    assert job_item['job_location'] == expected_job_location

def test_parse_job_error():
    response = scrapy.http.Response("")

    with pytest.raises(Exception):
        LinkedJobsSpider().parse_job(response)