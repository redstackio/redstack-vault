---
id: proc-build-vulnerable-rails-app
tags:
  - xss
  - docker
  - rails-poc
type: procedure
tools:
  - '[[tools/Docker]]'
  - '[[tools/Ruby]]'
  - '[[tools/Rails]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/docker-build-rails-poc]]'
  - '[[commands/docker-run-rails-poc]]'
  - '[[commands/rails-generate-poc1-controller]]'
  - '[[commands/rails-precompile-assets]]'
  - '[[commands/rails-start-server]]'
verified: false
platforms:
  - Ruby on Rails
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:25.767Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Build-Sample-Vulnerable-Rails-Application-with-Docker

## Summary

This procedure constructs a Dockerized Rails application with controllers and views that use the vulnerable SafeListSanitizer, allowing demonstration of reflected XSS via user input parameters.

## Description

A new Rails app is generated, controllers like Poc1 and Poc2 are created to assign and sanitize params[:name] with vulnerable tags (svg+style or math+style), and routes are set for /poc1 and /poc2. Dockerfile uses Ruby 3.1.2 base, precompiles assets, and runs in production. This isolates the PoC for safe testing.

## Requirements

1. Docker installed
2. Ruby 3.1.2 and Rails gems
3. build-rails-app.sh and Makefile for automation

## Defense

Defensive measures and detection strategies:

- Containerize apps with security scanning (e.g., Trivy)
- Review generated code for sanitization misuse
- Use multi-stage Docker builds to minimize attack surface
- Scan for vulnerable gems with bundler-audit

## Objectives

1. Set up Rails app with vulnerable sanitization
2. Expose endpoints for payload injection
3. Run in container for reproducibility

## Instructions

### Step 1: Generate Controllers and Routes

**Context**: Use Rails generators and cat to create PoC files in build-rails-app.sh.

**Command** ([[commands/rails-generate-poc1-controller]]):
```bash
bin/rails generate controller Poc1 index --skip-routes
```

> Generates controller and view stubs. Expected: Files in app/controllers and views.

Then write routes with cat:
```bash
cat << EOF > ./config/routes.rb
Rails.application.routes.draw do
  get '/poc1', to: 'poc1#index'
  get '/poc2', to: 'poc2#index'
end
EOF
```

And controller code:
```bash
cat << EOF > ./app/controllers/poc1_controller.rb
class Poc1Controller < ApplicationController
  def index
    @name = sanitize(params[:name], tags: %w[svg style])
  end
end
EOF
```

Similar for view with <%= sanitize @name %>.

### Step 2: Build Docker Image

**Context**: Compile the app into a container image.

**Command** ([[commands/docker-build-rails-poc]]):
```bash
docker build -t local/railspoc:latest .
```

> Builds from Dockerfile. Expected: Success logs.

### Step 3: Precompile Assets

**Context**: Prepare static assets for production.

**Command** ([[commands/rails-precompile-assets]]):
```dockerfile
RUN RAILS_ENV=production rails assets:precompile
```

> Runs in Dockerfile. Expected: Precompiled files.

### Step 4: Run Container

**Context**: Start the server.

**Command** ([[commands/docker-run-rails-poc]]):
```bash
docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```

> Maps ports. Expected: Server startup.

**Command** ([[commands/rails-start-server]]):
```dockerfile
CMD ["./bin/rails", "server", "-b", "0.0.0.0", "-e", "production"]
```

> Default CMD. Expected: Binds to 0.0.0.0:3000.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-build-rails-poc]]
- [[commands/docker-run-rails-poc]]
- [[commands/rails-generate-poc1-controller]]
- [[commands/rails-precompile-assets]]
- [[commands/rails-start-server]]

## Tools Used

- [[tools/Docker]]
- [[tools/Rails]]

## Tags

- [[xss]]
- [[poc]]
