---
id: proc-uuid-002
tags:
  - nosql-injection
  - blind-injection
  - token-extraction
type: procedure
tools:
  - '[[tools/Python-Requests]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/blind-mongodb-injection-script]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:33:06.402Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
---
# Extract-Reset-Token-via-Blind-Injection

## Summary

This procedure exploits blind MongoDB injection in the /admin/verify endpoint to extract password reset tokens character-by-character using $regex operators, enabling unauthorized access to reset functionality.

## Description

The vulnerability stems from unsanitized req.query.t passed to User.findOne({ token: req.query.t }), allowing payloads like { $regex: '^a' } to test prefixes. By sending iterative requests and observing redirects (e.g., to /admin/sp/ on match), the full token is reconstructed. Similar injection applies to /forgotpassword for email enumeration. Targets Node.js/Express/Mongoose environments.

## Requirements

1. Running FlintCMS instance with known target email
2. Python 2.7+ with requests library
3. Access to /admin/verify endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize inputs using mongoose-sanitize or schema validation
- Use parameterized queries or ObjectId casting for tokens
- Log and alert on regex operator usage in queries

## Objectives

1. Blindly extract the full reset token
2. Enable subsequent password reset
3. Demonstrate NoSQL injection impact

## Instructions

### Step 1: Prepare Injection Payloads

**Context**: Define character sets for guessing (a-z, 0-9, etc.).

Create a Python script skeleton to loop through positions and characters.

### Step 2: Execute Blind Injection Script

**Context**: Send requests to test token prefixes and observe responses.

Execute [[commands/blind-mongodb-injection-script]] with target URL http://localhost:4000/admin/verify?t= and email context.

```bash
python blind_injection.py --url http://localhost:4000/admin/verify --target-email admin@localhost.com
```

> The script sends payloads like t[$regex]=^[a-m] for binary search or sequential, checking for 302 redirect to /admin/sp/ as success indicator. Reconstruct token from matches.

**Expected Output**: Printed token, e.g., "5f8e9a2b1c3d4e5f6789a0b1c2d3e4f5".

### Step 3: Validate Extraction

**Context**: Confirm token by direct access.

Visit http://localhost:4000/admin/sp/{token} to check for reset page access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/blind-mongodb-injection-script]]

## Tools Used

- [[tools/Python-Requests]]

## Tags

- [[nosql-injection]]
- [[blind-injection]]
