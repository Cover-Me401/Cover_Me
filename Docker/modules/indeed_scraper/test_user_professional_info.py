import pytest
from modules.user_professional_info import user_professional_info
import io
from unittest.mock import patch

# Testing for user_professional_info
# @pytest.mark.skip
def test_user_professional_info():
    expected_years_experience = "5"
    expected_prev_jobs_keywords = "Python, Django, PostgreSQL"
    expected_tech_languages = "JavaScript, HTML, CSS"
    expected_professional_interests = "Machine learning, Data analysis"

    # Simulate user input for testing
    with patch("rich.prompt.Prompt.ask", side_effect=[expected_years_experience, expected_prev_jobs_keywords, expected_tech_languages, expected_professional_interests]):
        captured_output = io.StringIO()
        captured_output.write

        # Call the user_professional_info() function
        user_professional_info("5", "Python, Django, PostgreSQL", "JavaScript, HTML, CSS", "Machine learning, Data analysis")

        # Verify the inputs
        output = captured_output.getvalue()
        assert expected_years_experience in output
        assert expected_prev_jobs_keywords in output
        assert expected_tech_languages in output
        assert expected_professional_interests in output

@pytest.mark.skip
def test_user_professional_info_types():
    # Ensure that the years of experience is a number
    with pytest.raises(TypeError):
        user_professional_info("five", "Python", "JavaScript", "Machine learning")

    # Ensure that the keywords are strings
    with pytest.raises(TypeError):
        user_professional_info(5, 12345, "JavaScript", "Machine learning")

@pytest.mark.skip
def test_user_professional_info_lengths():
    # Ensure that the years of experience is a positive number
    with pytest.raises(ValueError):
        user_professional_info(-1, "Python", "JavaScript", "Machine learning")

    # Ensure that the keywords are not too long
    with pytest.raises(ValueError):
        user_professional_info(5, "This is a very long keyword", "JavaScript", "Machine learning")

@pytest.mark.skip
def test_user_professional_info_validity():
    # Ensure that the tech languages are actual programming languages
    with pytest.raises(ValueError):
        user_professional_info(5, "Python", "JavaScript", "This is not a programming language")

    # Ensure that the professional interests are not offensive
    with pytest.raises(ValueError):
        user_professional_info(5, "Python", "JavaScript", "I hate everyone")

@pytest.mark.skip
def test_user_professional_info_error_handling():
    # Ensure that the program gracefully handles invalid input
    try:
        user_professional_info("five", "Python", "JavaScript", "This is not a programming language")
    except ValueError as e:
        assert str(e) == "The years of experience must be a positive number."



# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
