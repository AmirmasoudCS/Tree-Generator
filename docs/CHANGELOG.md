# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

---

## [0.3.0] - 2026-05-13

### Added
- Initial public release of **Tree Printer**
- Directory tree generation from the command line
- Optional file and directory icons (`--icons`)
- Sorting support (`--sort name | size | modified`)
- File metadata display (size and modified time)
- File and directory exclusion options

### Changed
- Designed a modular architecture consisting of `printer`, `formatter`, `icons`, and `cli` modules
- Improved CLI help and overall user experience
- Created a clean and extensible formatter design

### Documentation
- Added a comprehensive README
- Added usage examples
- Added a complete CLI options reference
- Added preview output examples

---

## [0.3.1] - 2026-05-14

### Added
- Added the `--version` (`-v`) command to display the current Tree Printer version

### Changed
- Improved package metadata
- Improved installation behavior

---

## [0.4.0] - 2026-07-03

### Added
- Comprehensive test suite using **pytest**
- Automated Continuous Integration (CI) using **GitHub Actions**
- Automated testing across supported Python versions
- Improved project metadata for PyPI
- Added project URLs, keywords, and classifiers to package metadata

### Changed
- Modernized packaging configuration
- Improved development workflow
- Enhanced project documentation
- Updated the project to follow modern Python packaging best practices