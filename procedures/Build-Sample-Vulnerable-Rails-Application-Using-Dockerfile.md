---
tags:
  - docker
  - rails
  - poc
type: procedure
tools:
  - '[[tools/Docker]]'
  - '[[tools/Rails]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/apt-get-update-install-vim]]'
  - '[[commands/gem-install-rails-new-app]]'
  - '[[commands/sh-build-rails-app]]'
  - '[[commands/rails-assets-precompile]]'
  - '[[commands/rails-server-production]]'
  - '[[commands/generate-poc1-controller]]'
  - '[[commands/generate-poc2-controller]]'
  - '[[commands/docker-build-railspoc]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:16.349Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a8106ebc-8ac6-4bb6-81ab-3f77be33bf5a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Build-Sample-Vulnerable-Rails-Application-Using-Dockerfile

## Summary

This procedure builds a Docker image of a vulnerable Rails application configured with sanitize helpers allowing 'math+style' and 'svg+style' tags, including PoC endpoints to demonstrate the XSS flaw.

## Description

Using a Dockerfile, install Ruby, Rails, and the affected sanitizer gem. Generate controllers and views that use the sanitize method with vulnerable allowtags. A build script customizes routes and precompiles assets for production. This creates a self-contained environment for exploitation testing.

## Requirements

1. Docker installed on host
2. Access to Dockerfile and build-rails-app.sh script
3. Ruby 3.x and Rails 7.x compatibility

## Defense

Defensive measures and detection strategies:

- Scan Dockerfiles for vulnerable gem versions
- Use multi-stage builds to minimize attack surface
- Monitor container builds for custom sanitize configs

## Objectives

1. Set up base image with Ruby and tools
2. Create and configure Rails app with vulnerable endpoints
3. Build and tag the Docker image

## Instructions

### Step 1: Update and Install Packages

**Context**: Prepare the base image with necessary tools like vim.

**Command** ([[commands/apt-get-update-install-vim]]):
```bash
apt-get update && apt-get install -y vim
```

> Installs vim; expected: Package output without errors.

### Step 2: Install Rails and Create App

**Context**: Install gem and generate new app.

**Command** ([[commands/gem-install-rails-new-app]]):
```bash
gem install rails && rails new myapp
```

> Creates myapp; expected: App generation logs.

### Step 3: Customize App with Script

**Context**: Run script to add PoC controllers and routes.

**Command** ([[commands/sh-build-rails-app]]):
```bash
sh ./build-rails-app.sh
```

> Executes generates like [[commands/generate-poc1-controller]]; expected: Controller outputs.

### Step 4: Precompile Assets

**Context**: Prepare for production.

**Command** ([[commands/rails-assets-precompile]]):
```bash
RAILS_ENV=production rails assets:precompile
```

> Expected: Precompilation logs.

### Step 5: Build Docker Image

**Context**: Compile the full image.

**Command** ([[commands/docker-build-railspoc]]):
```bash
docker build -t local/railspoc:latest .
```

> Expected: Build success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/apt-get-update-install-vim]]
- [[commands/gem-install-rails-new-app]]
- [[commands/sh-build-rails-app]]
- [[commands/rails-assets-precompile]]
- [[commands/rails-server-production]]
- [[commands/generate-poc1-controller]]
- [[commands/generate-poc2-controller]]
- [[commands/docker-build-railspoc]]

## Tools Used

- [[tools/Docker]]
- [[tools/Rails]]

## Tags

- docker
- poc
