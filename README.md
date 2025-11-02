# TRG Website Automation Tests

Automated UI tests for [TRG International](https://www.trgint.com/) built with **Playwright + Pytest**.  
The project follows the Page Object Model (POM) pattern 

---
1. Write an automated test which will go to the TRG International website and navigate to
Careers → #Life At TRG page. Scroll down to the Core values section, save each core
value with its headline and description in JSON format file and then count how many
exclamation marks are there (“!”). Additionally, download all 4 images to your repository
and rename each file with related core value headlines.
2. Create a function which should return a random string we can use for testing purposes,
like creating a random Full Name for the “Book a demo” form. The name should have
two parts joined together, the first part should contain upper and lower 6 lettersword, and
the second part should contain a 3 digit random number (example: “sGeoRD256”).
When you join these two parts, reverse it (example: “652DRoeGs”) and return the value.

---

## ⚙️ Setup

```bash

git clone https://github.com/attuna/trg.git
cd trg
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
pre-commit install
```


## Running Tests

Run a specific test:
```bash

pytest tests/test_core_values.py -s
```
