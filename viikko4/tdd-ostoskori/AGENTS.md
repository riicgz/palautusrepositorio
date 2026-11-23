# Repository guidance

- Requires Python 3.14 (`.python-version`, `pyproject.toml`); use `uv` for the project environment and its `dev` dependency group (`pytest`).
- Run tests from the repository root with `PYTHONPATH=src uv run pytest src/tests/ostoskori_test.py`. Tests import application modules directly from `src`, not as a package.
- Application code is in `src/`; tests are in `src/tests/`. `Ostoskori` (`src/ostoskori.py`) is the shopping-cart implementation and uses `Tuote` and `Ostos` from sibling modules.
- No lint, formatter, type-check, or build command is configured in `pyproject.toml`.
- Tests executed with uv run pytest
- Code of ostos.py and tuote.py should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass