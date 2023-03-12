# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* Add shpinx documentation page(TODO).

## [1.1.1] - 2023-03-13

### Changed

* Remove subclass `str` from enums due to the update of `requests`.
* Resolve issue with missing `icon_format` in `rivens.list_items()`.

## [1.1.0] - 2022-03-26

### Added

* Add api for `orders`, `profile`, `liches` and `rivens`.
* Add `experimental` API, including `auctions`.
* Add `exceptions` wrapper.
* Add websocket support to `Session`.

### Changed

* Move `get_orders()` from `items` to `orders`, along with the related model definitions.

### Deprecated

* `items.get_orders()` would be deprecated.

## [1.0.0] - 2022-02-08

### Added

* Add part of api into `auth`, `items` and `statistics`.
* 🎉 From here, we started.
