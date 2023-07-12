import pytest
from Docker.modules.BARD_writer import bard
import io
from unittest.mock import patch


# Testing for bard
# @pytest.mark.skip
def test_bard():
  assert bard() == None

@pytest.mark.skip
def test_bard_sample():
    expected_text = "Sample Resume Text"  # Replace with the expected resume text
    expected_question = "Write a cover letter for this resume:\nSample Resume Text"

    # Mock the environment variables and Chatbot object
    with patch.dict("os.environ", {"_BARD_API_KEY": "YOUR_API_KEY"}), \
            patch("BARD_writer.Chatbot") as mock_chatbot:

        captured_output = io.StringIO()
        print = captured_output.write

        # Create a mock instance of the Chatbot
        chatbot_instance = mock_chatbot.return_value

        # Simulate the bot response
        chatbot_instance.ask.return_value = {"content": "Mocked response"}

        # Call the bard() function
        bard()

        # Verify the question and response
        chatbot_instance.ask.assert_called_once_with(expected_question)
        assert expected_question in captured_output.getvalue()

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])







