import click.testing
import pytest
import requests

from modern_python_valbaca import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()

@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("modern_python_valbaca.wikipedia.random_page")

def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    # better to have a single assert per test, but this is fine for now
    assert result.exit_code == 0
    assert "Lorem Ipsum" in result.output
    assert mock_requests_get.called
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]

def test_main_fails_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1

def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output

def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")