---
tags:
  - smtp
  - verification
  - log
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.608Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d5f4bdd0-47c0-4468-b41c-262a3fbe4dcd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-SMTP-Email-Delivery-via-Log

## Summary

This procedure checks the log on a test SMTP server to confirm that the SSRF exploit successfully sent an email from the vulnerable PlayStation EC2 instance.

## Description

After triggering the SSRF, the test SMTP server (e.g., test.smtp.org) logs incoming connections and commands. Accessing the /log endpoint reveals the session details, including the source IP (Sony EC2), SMTP commands executed, and email content. This validates the exploit's success and demonstrates the abuse of the victim's infrastructure for outbound SMTP requests.

## Requirements

1. Control over the test SMTP server with logging enabled
2. Web access to the log endpoint (http://test.smtp.org/log)
3. Prior execution of the SSRF trigger

## Defense

Defensive measures and detection strategies:

- Rate-limit and monitor SMTP connections to external servers
- Block unexpected outbound SMTP from application servers
- Correlate logs from web endpoints with network traffic for anomaly detection

## Objectives

1. Confirm email transmission from the victim's server
2. Validate payload execution in the SSRF chain
3. Identify source IP for attribution

## Instructions

### Step 1: Access SMTP Log

**Context**: Retrieve the log to inspect the recent SMTP session.

**Command** (HTTP GET):
```bash
curl http://test.smtp.org/log
```

> This fetches the log file. Expected output: Text log showing connection from EC2 IP, followed by HELO, MAIL FROM, RCPT TO, DATA, body, and .

### Step 2: Analyze Log Entries

**Context**: Review for matching payload and source.

> Look for entries like "Connected from <EC2 IP>", then the sequence of SMTP commands. Success if commands match the payload and email is processed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- smtp
- verification
- log
