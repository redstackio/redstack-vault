---
tags:
  - nosql-injection
  - email-enumeration
  - automation-script
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/run-mongodb-injection-exploit]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:51.977Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ccc45ac0-c911-4234-b410-5842a3bd33ee
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Execute-Blind-Email-Enumeration-Script

## Summary

This procedure automates the blind MongoDB injection attack using a Python script to enumerate all customer and admin emails by recursively querying the login endpoint with $regex payloads until the full database is reconstructed.

## Description

The script targets the customer login first, then adapts for admin, sending hundreds of requests to guess emails character by character. It handles blind responses by comparing error messages or status codes. For express-cart v1.1.7, this leaks all emails, impacting privacy and enabling attacks. Prerequisites: Working payload crafter and target URL. Run in a controlled environment to avoid DoS.

## Requirements

1. Python 2.7.12 or compatible with requests library installed
2. Target endpoint URL and confirmed injection
3. Sufficient network bandwidth for repeated requests

## Defense

Defensive measures and detection strategies:

- Deploy WAF rules to block $regex in JSON payloads
- Use CAPTCHA or anomaly detection on login failures
- Regularly audit MongoDB query logs for injection patterns

## Objectives

1. Automate full enumeration of customer emails
2. Extend to admin emails for targeted attacks
3. Output a complete list for exfiltration or phishing

## Instructions

### Step 1: Prepare the Exploit Script

**Context**: Write or obtain the recursive Python script (exploit.py) that implements the guessing logic.

No command; script includes functions for sending payloads and recursing on matches.

> Expected: Script file ready with target URL configured.

### Step 2: Execute the Enumeration Script

**Context**: Run the script to start blind enumeration on customer endpoint.

Execute [[commands/run-mongodb-injection-exploit]]:

```bash
python exploit.py
```

> The script will output progress like "Guessing position 1: a matched" and final emails. Expected: Full list after ~1000-5000 requests depending on database size.

### Step 3: Repeat for Admin Endpoint

**Context**: Modify target URL or endpoint in script for admin login and re-run.

```bash
python exploit.py --admin
```

> Expected: Separate list of admin emails, e.g., admin@company.com.

### Step 4: Validate Output

**Context**: Cross-check enumerated emails against any known samples.

Manually test a few with legitimate logins or external sources.

> Expected: High accuracy; incomplete if rate-limited.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/run-mongodb-injection-exploit]]

## Tools Used

- [[tools/Python]]

## Tags

- nosql-injection
- email-enumeration
- automation-script
