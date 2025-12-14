---
tags:
  - directory-traversal
  - path-traversal
  - rails
  - rce
  - ruby
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/rails]]'
  - '[[tools/bundle]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Rails-Environment-with-Vulnerable-Gem]]'
  - '[[procedures/Enable-Page-Caching-in-Rails-Application]]'
  - '[[procedures/Verify-Caching-Behavior-and-Create-Malicious-Payload]]'
  - '[[procedures/Exploit-Directory-Traversal-for-Arbitrary-File-Writing]]'
  - '[[procedures/Achieve-RCE-by-Overwriting-ERB-Template]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:27.477Z'
description: >-
  Multi-stage exploitation of directory traversal vulnerability in the
  actionpack-page_caching gem of Ruby on Rails, enabling arbitrary file writing
  and remote code execution via crafted URLs with encoded traversal sequences.
skill_level: intermediate
impact_level: high
id: cf11345d-b055-475a-a755-ca735d5caba8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Directory Traversal in Rails Page Caching Leading to Arbitrary File Write and RCE

Multi-stage attack chain demonstrating exploitation of a directory traversal vulnerability in the actionpack-page_caching gem of Ruby on Rails. The vulnerability allows unsanitized paths in cache_file and cache_path methods, enabling attackers to write cache files outside the intended public directory using encoded sequences like %2f (/) and %2e (.). This leads to arbitrary file writing, including overwriting ERB templates for remote code execution (RCE).

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
    A[Prepare Environment] --> B[Enable Caching]
    B --> C[Verify and Payload]
    C --> D[Traverse and Write Files]
    D --> E[Overwrite Template for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/rails]]
- [[tools/bundle]]
- [[tools/ls]]
- [[tools/cat]]

### Target Environment

- Ruby on Rails application with actionpack-page_caching gem
- Development environment with SQLite database
- Port 3000 open for local server
- Local network access to the Rails server

### Initial Access Requirements

- No credentials required (public-facing web app)
- Local or remote access to start the Rails server
- Ruby and Rails installed on the attacker's machine

## Detailed Attack Procedures

### Step 1: Prepare Rails Environment
procedure: [[procedures/Prepare-Rails-Environment-with-Vulnerable-Gem]]

**Objective**: Set up a vulnerable Rails application with the actionpack-page_caching gem to enable page caching.

**Instructions**: Verify Ruby and Rails versions, create a new app, add the gem, install dependencies, generate a scaffold, and migrate the database.

**Expected Output**: A functional Rails app directory with the vulnerable gem installed and database ready.

**Success Indicators**:
- Ruby and Rails versions displayed
- New app directory created
- Gems installed successfully
- Books table migrated

### Step 2: Enable Page Caching
procedure: [[procedures/Enable-Page-Caching-in-Rails-Application]]

**Objective**: Activate page caching in the development environment and configure the controller to cache the show action.

**Instructions**: Run the cache enable command and modify the BooksController to include caches_page :show.

**Expected Output**: Caching enabled in config/environments/development.rb.

**Success Indicators**:
- Cache configuration updated
- Controller modified without errors

### Step 3: Verify Caching Behavior and Create Malicious Payload
procedure: [[procedures/Verify-Caching-Behavior-and-Create-Malicious-Payload]]

**Objective**: Start the server, create a book with a malicious ERB payload, and confirm caching generates files in the public directory.

**Instructions**: Launch the server, create a book via the app, access the show page with curl, and inspect the cache file.

**Expected Output**: Cache file public/books/1.html created with escaped payload.

**Success Indicators**:
- Server running on localhost:3000
- Book created with payload <% `touch me` %>
- Cache file contains the escaped HTML

### Step 4: Exploit Directory Traversal for Arbitrary File Writing
procedure: [[procedures/Exploit-Directory-Traversal-for-Arbitrary-File-Writing]]

**Objective**: Use encoded traversal sequences in URLs to write cache files outside the public directory, demonstrating arbitrary write capability.

**Instructions**: Craft curl requests with %2f%2e%2e sequences to create test.html in root and overwrite README.md.

**Expected Output**: Files created or overwritten outside public dir.

**Success Indicators**:
- test.html appears in root directory
- README.md contents replaced with cache snippet

### Step 5: Achieve RCE by Overwriting ERB Template
procedure: [[procedures/Achieve-RCE-by-Overwriting-ERB-Template]]

**Objective**: Overwrite an ERB template with malicious code via traversal, then trigger execution to run system commands.

**Instructions**: Ensure show.text.erb exists, use traversal to overwrite it, then access .txt format to render and execute.

**Expected Output**: 'me' file created via touch command execution.

**Success Indicators**:
- Template overwritten with malicious ERB
- RCE executed, new file generated

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable Rails environment
2. Demonstration of directory traversal for file writes outside intended paths
3. Achievement of RCE by overwriting and executing ERB templates

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
