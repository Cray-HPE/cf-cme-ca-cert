# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Dependencies
- Bump `tj-actions/changed-files` from 37 to 40 ([#30](https://github.com/Cray-HPE/cf-cme-ca-cert/pull/30), [#32](https://github.com/Cray-HPE/cf-cme-ca-cert/pull/32))
- Bump `stefanzweifel/git-auto-commit-action` from 4 to 5 ([#31](https://github.com/Cray-HPE/cf-cme-ca-cert/pull/31))
- Bump `actions/checkout` from 3 to 4 ([#29](https://github.com/Cray-HPE/cf-cme-ca-cert/pull/29))

## [2.6.1] - 2023-08-10
### Changed
- Disabled concurrent Jenkins builds on same branch/commit
- Added build timeout to avoid hung builds
- RPM OS type changed to `noos`.

## [2.6.0] - 2023-06-22
### Added
- Build SLES SP5 RPM
### Changed
- RPM builds type changed from `x86_64` to `noarch`
### Removed
- Removed defunct files leftover from previous versioning system

## [2.5.1] - 2022-12-20
### Added
- Add Artifactory authentication to Jenkinsfile

## [2.4.0] - 2022-07-14
### Added
- Migrated over to new DST servers for build artifacts
- Support for SLES SP4

### Changed
- Convert to gitflow/gitversion.