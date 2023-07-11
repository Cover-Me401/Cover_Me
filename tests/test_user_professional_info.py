import pytest
from Docker.modules.user_professional_info import user_professional_info
import io
from unittest.mock import patch

# Testing for user_professional_info
def test_user_professional_info():
    expected_years_experience = "5"
    expected_prev_jobs_keywords = "Python, Django, PostgreSQL"
    expected_tech_languages = "JavaScript, HTML, CSS"
    expected_professional_interests = "Machine learning, Data analysis"

    # Simulate user input for testing
    with patch("rich.prompt.Prompt.ask", side_effect=[expected_years_experience, expected_prev_jobs_keywords,
                                                      expected_tech_languages, expected_professional_interests]):
        captured_output = io.StringIO()
        console.print = captured_output.write

        # Call the user_professional_info() function
        user_professional_info()

        # Verify the inputs
        output = captured_output.getvalue()
        assert expected_years_experience in output
        assert expected_prev_jobs_keywords in output
        assert expected_tech_languages in output
        assert expected_professional_interests in output

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])