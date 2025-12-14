---
id: proc-claim-uptimerobot-subdomain
tags:
  - takeover
  - exploitation
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.676Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim and Takeover Subdomain on UptimeRobot

## Summary

This procedure demonstrates claiming control of a dangling subdomain by creating an account on UptimeRobot and configuring a monitor, allowing the attacker to host arbitrary content on the subdomain.

## Description

Once availability is confirmed, the attacker registers a test account and adds the subdomain as a monitor pointing to the service's stats domain. This hijacks the DNS resolution, enabling hosting of phishing pages or false status messages. The target is web/DNS environments with UptimeRobot integration; outcomes include full subdomain control and potential reputation damage.

## Requirements

1. Free UptimeRobot account
2. Identified dangling subdomain
3. Web access to the service dashboard

## Defense

Defensive measures and detection strategies:

- Remove dangling DNS records immediately
- Enable DNSSEC and monitor for unauthorized resolutions
- Use certificate transparency logs to detect takeovers

## Objectives

1. Gain control of the subdomain
2. Host malicious content
3. Demonstrate impact like phishing

## Instructions

### Step 1: Create Account and Add Monitor

**Context**: Register and configure the subdomain on UptimeRobot.

No command; via web interface: Sign up at uptimerobot.com, then add new monitor with type 'HTTP(s)', URL 'https://status0.stripo.email', and hostname matching the CNAME.

> This claims the subdomain. Expected output: Monitor created successfully, subdomain now resolves to UptimeRobot-hosted page.

### Step 2: Configure and Host Content

**Context**: Customize the claimed subdomain to serve arbitrary content.

No command; in the monitor settings or custom page feature, upload HTML for false messages or phishing.

> Verify by accessing the subdomain URL. Expected output: Attacker-controlled content loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- [[exploitation]]
- [[takeover]]
