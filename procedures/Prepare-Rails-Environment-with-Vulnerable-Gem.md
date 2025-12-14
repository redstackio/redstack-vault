---
tags:
  - rails-setup
  - vulnerable-gem
type: procedure
tools:
  - '[[tools/rails]]'
  - '[[tools/bundle]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ruby-version-check]]'
  - '[[commands/rails-version-check]]'
  - '[[commands/rails-new-app]]'
  - '[[commands/cd-app-dir]]'
  - '[[commands/bundle-install]]'
  - '[[commands/rails-generate-scaffold]]'
  - '[[commands/rails-db-migrate]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.472Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5631bb38-3ec2-422b-b313-e59d57428935
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Rails-Environment-with-Vulnerable-Gem

## Summary

This procedure sets up a local Ruby on Rails development environment vulnerable to the actionpack-page_caching directory traversal issue by creating a new app, adding the gem, and preparing a scaffolded resource for testing page caching.

## Description

The actionpack-page_caching gem enables page caching in Rails but lacks path sanitization in cache_file and cache_path methods, allowing traversal attacks. This procedure creates a minimal Rails app with a Books scaffold to simulate a target application. It requires Ruby and Rails installed locally and assumes a development setup with SQLite. The outcome is a ready-to-run app where caching can be enabled for exploitation.

## Requirements

1. Ruby 2.5+ and Rails 5+ installed on a Linux/macOS system
2. Bundler gem available
3. Local access to run commands (no network required for setup)
4. SQLite for development database

## Defense

Defensive measures and detection strategies:

- Use dependency scanners like Bundler-audit to detect vulnerable gems
- Enable path normalization and validation in caching middleware
- Monitor for unexpected file writes outside web root via filesystem auditing

## Objectives

1. Establish a reproducible vulnerable environment
2. Install the actionpack-page_caching gem
3. Prepare a testable resource (Books model) for caching

## Instructions

### Step 1: Verify Ruby and Rails Versions

**Context**: Ensure prerequisites are met before creating the app.

**Command** ([[commands/ruby-version-check]]):
```bash
ruby -v
```

> Displays Ruby version, e.g., ruby 2.7.0. Expected: Compatible version info.

**Command** ([[commands/rails-version-check]]):
```bash
rails -v
```

> Displays Rails version, e.g., Rails 6.1.0. Expected: Compatible version info.

### Step 2: Create New Rails App

**Context**: Generate the base application structure.

**Command** ([[commands/rails-new-app]]):
```bash
rails new caching_traversal
```

> Creates directory caching_traversal with Rails skeleton. Expected: New app directory.

**Command** ([[commands/cd-app-dir]]):
```bash
cd caching_traversal
```

> Navigates into the app. Expected: Current dir changed.

### Step 3: Add Vulnerable Gem and Install

**Context**: Manually add gem to Gemfile (gem "actionpack-page_caching"), then install.

**Command** ([[commands/bundle-install]]):
```bash
bundle install
```

> Installs dependencies including the gem. Expected: Gems installed message.

### Step 4: Generate Scaffold and Migrate

**Context**: Create Books resource for testing.

**Command** ([[commands/rails-generate-scaffold]]):
```bash
rails generate scaffold book name:string
```

> Generates model, controller, views. Expected: Files created.

**Command** ([[commands/rails-db-migrate]]):
```bash
rails db:migrate
```

> Sets up database. Expected: Schema updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/ruby-version-check]]
- [[commands/rails-version-check]]
- [[commands/rails-new-app]]
- [[commands/cd-app-dir]]
- [[commands/bundle-install]]
- [[commands/rails-generate-scaffold]]
- [[commands/rails-db-migrate]]

## Tools Used

- [[tools/rails]]
- [[tools/bundle]]

## Tags

- rails-setup
- vulnerable-gem
