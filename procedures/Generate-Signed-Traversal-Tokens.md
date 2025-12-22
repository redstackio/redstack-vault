---
tags:
  - token-crafting
  - rails
  - messageverifier
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Rails]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rails-runner-traversal]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.390Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6737e75e-63d7-461c-bfef-8cc664aaa212
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-Signed-Traversal-Tokens

## Summary

This procedure crafts signed tokens using ActiveSupport::MessageVerifier with path traversal payloads in the 'key' parameter, enabling subsequent read and write exploits in ActiveStorage Disk service.

## Description

By running a custom Ruby script (traversal.rb) within the Rails context, tokens are generated for blob keys containing '../' sequences. These tokens are signed with the app's secret_key_base, bypassing validation when used in /rails/active_storage/disk/{token} endpoints. The script outputs ready-to-use curl commands for exploitation.

## Requirements

1. Running Rails app in production with known secret_key_base
2. traversal.rb script prepared with MessageVerifier usage
3. Bundler for gem loading
4. Local access to the app directory

## Defense

Defensive measures and detection strategies:

- Validate and sanitize blob keys to prevent traversal
- Use secure random secret_key_base and protect it
- Log token generation and verification attempts
- Implement rate limiting on ActiveStorage endpoints

## Objectives

1. Create valid signed tokens for traversal payloads
2. Prepare exploitation commands for file read/write
3. Enable arbitrary access outside storage directory

## Instructions

### Step 1: Execute Traversal Script

**Context**: Run the script to generate tokens using Rails' MessageVerifier.

**Command** ([[commands/rails-runner-traversal]]):
```bash
RAILS_ENV=production bundle exec rails runner traversal.rb
```

> Outputs serializer type, read token for master.key, curl for read, write target path, write token, and curl for write. Includes payloads like '././../config/master.key'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/rails-runner-traversal]]

## Tools Used

- [[tools/Ruby]]
- [[tools/Rails]]

## Tags

- token-crafting
- rails
- messageverifier
