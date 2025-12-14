---
id: proc-identify-phpunit-vendor
tags:
  - recon
  - phpunit
  - dependency
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/find-phpunit]]'
verified: false
platforms:
  - Linux
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:27.807Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-PHPUnit-in-Vendor-Directory

## Summary

This procedure searches the extracted app package for the PHPUnit testing framework in the vendor directory, highlighting improper inclusion of development dependencies in production releases.

## Description

Nextcloud apps use Composer for dependency management, placing libraries in a vendor/ folder. Accidentally including PHPUnit—a tool for unit testing—exposes sensitive files like eval-stdin.php. This procedure uses file search commands to detect such inclusions, informed by known risks discussed in security articles.

## Requirements

1. Extracted tarball from previous procedure
2. find and ls commands available
3. Knowledge of Composer vendor structure

## Defense

Defensive measures and detection strategies:

- Configure composer.json to exclude dev dependencies in production (e.g., --no-dev flag)
- Use static analysis tools like PHPStan or security scanners to flag test code
- Audit release artifacts pre-deployment

## Objectives

1. Locate PHPUnit artifacts in the production package
2. Confirm presence of risky subdirectories
3. Cross-reference with external vulnerability reports

## Instructions

### Step 1: Search for PHPUnit Directories

**Context**: Use find to recursively locate PHPUnit-related paths in the vendor folder.

**Command** ([[commands/find-phpunit]]):
```bash
find . -name "*phpunit*" -type d
```

> Searches for directories matching phpunit. Expected output: Paths like ./vendor/phpunit/phpunit/.

### Step 2: List PHPUnit Contents

**Context**: Examine the identified directory for specific files.

**Command** (ls vendor):
```bash
ls vendor/phpunit/
```

> Lists files and subdirs. Expected output: src/, tests/, and Util/PHP/ folders.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/find-phpunit]]
- ls (built-in)

## Tools Used


## Tags

- recon
- phpunit
- dependency
