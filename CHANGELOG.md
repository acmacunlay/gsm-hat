# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [Unreleased] - yyyy-mm-dd

### Added

- TODO

### Changed

- TODO

### Deprecated

- TODO

### Fixed

- TODO

### Removed

- TODO

### Security

- TODO
-->

## [0.5.0a0] - 2024-10-07

### Added

- `CHANGELOG.md`
- `.gitignore`
- [WIP] refactor SIM868 controller
- [WIP] unit tests
- implemented GitHub Action for automated CI workflow
- implemented linting using `ruff`
- implemented static type checking using `mypy`
- implemented unit testing using `pytest`

### Changed

- added copyright notice in `LICENSE` for the scope of this fork
- converted `setup.py` to `pyproject.toml` for PEP-517/518 compliance
- converted project structure to `src` layout
- moved forked implementation of the controller to `pywaveshare.boards.sim868`
- made minor changes in `README.md`

### Removed

- `setup.cfg`
