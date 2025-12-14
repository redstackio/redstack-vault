---
tags:
  - setup
  - poc
  - rails
type: procedure
tools:
  - '[[tools/ruby]]'
  - '[[tools/rails]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ruby-version-check]]'
  - '[[commands/rails-new-poc]]'
  - '[[commands/cd-rails-server]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:43.934Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d8cc888f-6132-4c53-9018-66f908095fa0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Ruby-on-Rails-POC-Environment

## Summary

This procedure verifies the Ruby environment and creates a minimal Rails 7.1 application to demonstrate the XSS vulnerability in the translate method.

## Description

In a local development setup, check Ruby version for compatibility (requires >=3.0 for Rails 7), generate a new Rails app skipping unnecessary components for a lightweight PoC, and navigate into the project directory. This establishes the base for configuring the vulnerable endpoints.

## Requirements

1. Ruby 3.0+ installed
2. Rails 7.1.2 gem available
3. Local machine with bash shell

## Defense

Defensive measures and detection strategies:

- Use dependency checkers like bundler-audit to verify gem versions
- Monitor for outdated Rails installations via vulnerability scanners like brakeman

## Objectives

1. Confirm environment readiness
2. Generate clean Rails app
3. Prepare directory for configuration

## Instructions

### Step 1: Verify Ruby Version

**Context**: Ensure Ruby is compatible with Rails 7 for the PoC.

**Command** ([[commands/ruby-version-check]]):
```bash
ruby -v
```

> Displays installed Ruby version, e.g., ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin22]. If incompatible, install/update Ruby.

### Step 2: Create New Rails Application

**Context**: Generate a minimal app skipping generators for asset pipeline, mailer, ORM, etc.

**Command** ([[commands/rails-new-poc]]):
```bash
rails new rails_server -G -M -O -C -A -J -T
```

> Creates directory structure for 'rails_server' app. Expected: No errors, app files generated.

### Step 3: Navigate to Application Directory

**Context**: Enter the project to edit files and run server.

**Command** ([[commands/cd-rails-server]]):
```bash
cd rails_server
```

> Changes working directory. Expected: Prompt shows inside rails_server/.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/ruby-version-check]]
- [[commands/rails-new-poc]]
- [[commands/cd-rails-server]]

## Tools Used

- [[tools/ruby]]
- [[tools/rails]]

## Tags

- setup
- poc
- rails
