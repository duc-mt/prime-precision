# Contributing Guidelines

Thank you for your interest in contributing to prime-precision!

## How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-new-feature`)
3. Install development dependencies (`pip install -e ".[dev]"`)
4. Make your changes
5. Run tests (`pytest`) and linters (`ruff check .`, `mypy .`)
6. Commit your changes (`git commit -am 'Add some feature'`)
7. Push to the branch (`git push origin feature/my-new-feature`)
8. Create a new Pull Request

## Development Setup

This project uses `pyproject.toml` for dependency management.
We use `pytest` for testing, `ruff` for linting/formatting, and `mypy` for static type checking.
