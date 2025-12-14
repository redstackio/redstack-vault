---
tags:
  - rails
  - setup
  - vulnerable-app
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Rails]]'
  - '[[tools/Bundler]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ruby-version-check]]'
  - '[[commands/rails-new-app]]'
  - '[[commands/rails-activestorage-install]]'
  - '[[commands/rails-db-migrate]]'
  - '[[commands/rails-server-start]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.400Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: da2484a6-7251-4670-ab41-6eaa9f244a4b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Vulnerable-Rails-Application

## Summary

This procedure sets up a Ruby on Rails 7.1.3 application configured with ActiveStorage using the Disk service in production mode, creating a vulnerable environment for path traversal exploitation.

## Description

The setup involves verifying Ruby compatibility, generating a minimal Rails app, installing ActiveStorage, migrating the database with SQLite, configuring the production environment to use JSON serialization for messages (to avoid Marshal issues), and starting the server. This replicates the vulnerable configuration where signed tokens can be crafted if secret_key_base is known, allowing path traversal in the 'key' parameter of Disk service blobs.

## Requirements

1. Ruby 3.2.3 installed on a Linux/macOS system
2. Rails 7.1.3 gem available via Bundler
3. Local development environment with write access to directories
4. No internet required beyond initial gem installation

## Defense

Defensive measures and detection strategies:

- Use path normalization and validation in ActiveStorage to reject '../' sequences
- Rotate secret_key_base regularly and avoid exposing it
- Monitor file system access logs for unexpected reads/writes outside storage dirs
- Enable Rails security features like strong parameters for blob keys

## Objectives

1. Establish a running vulnerable Rails app for testing
2. Ensure ActiveStorage Disk service is active in production
3. Prepare environment for token generation and exploitation

## Instructions

### Step 1: Verify Ruby Version

**Context**: Confirm Ruby version compatibility for Rails 7.1.

**Command** ([[commands/ruby-version-check]]):
```bash
ruby -v
```

> Displays the installed Ruby version. Expected: ruby 3.2.3 or similar.

### Step 2: Create New Rails App

**Context**: Generate a minimal app skipping unnecessary components.

**Command** ([[commands/rails-new-app]]):
```bash
rails new disk_traversal_7_1 -G -M -C -A -J -T
```

> Creates the app directory with flags to skip Git, minitest, CoffeeScript, Action Mailer, Spring, and tests.

### Step 3: Install ActiveStorage

**Context**: Add ActiveStorage migrations and configurations.

**Command** ([[commands/rails-activestorage-install]]):
```bash
bin/rails active_storage:install
```

> Generates necessary files for Disk service setup.

### Step 4: Migrate Database

**Context**: Apply schema changes for ActiveStorage tables using SQLite in production.

**Command** ([[commands/rails-db-migrate]]):
```bash
RAILS_ENV=production bin/rails db:migrate
```

> Runs migrations; defaults to SQLite if not specified otherwise.

### Step 5: Configure and Start Server

**Context**: Edit config/production.rb to set config.active_support.message_serializer = :json, then launch server.

**Command** ([[commands/rails-server-start]]):
```bash
RAILS_ENV=production bundle exec rails s
```

> Starts server on port 3000; ensure config change is made manually before running.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/ruby-version-check]]
- [[commands/rails-new-app]]
- [[commands/rails-activestorage-install]]
- [[commands/rails-db-migrate]]
- [[commands/rails-server-start]]

## Tools Used

- [[tools/Ruby]]
- [[tools/Rails]]
- [[tools/Bundler]]

## Tags

- rails
- setup
- vulnerable-app
