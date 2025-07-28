# Practise_Selenium

This project contains end-to-end tests using Selenium and pytest.

## Setup

1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests

To run all tests and generate an HTML report:
```sh
pytest tests/ --html=report.html
```

## Project Structure

- `pages/` - Page Object Model classes
- `tests/` - Test cases
- `requirements.txt` - Python dependencies
- `conftest.py` - Pytest configuration

## Notes
- Make sure your virtual environment is activated before running tests.
- Adjust browser drivers as needed for your environment. 