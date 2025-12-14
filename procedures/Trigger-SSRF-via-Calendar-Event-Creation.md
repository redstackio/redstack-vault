---
id: 00000000-0000-0000-0000-000000000004
name: Trigger-SSRF-via-Calendar-Event-Creation
type: procedure
verified: false
submitted: true
created_at: '2023-12-14T00:00:00Z'
updated_at: '2025-12-14T04:08:48.769Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - ssrf
  - calendar
  - dav
  - exploitation
platforms:
  - Web
  - PHP
commands:
  - '[[commands/nextcloud-ssrf-exploit]]'
tools:
  - '[[tools/nextcloud_ssrf.py]]'
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

# Trigger-SSRF-via-Calendar-Event-Creation

## Summary

This procedure injects a malicious WebCal URL into a Nextcloud calendar event using the DAV API, triggering the server-side RefreshWebcalJob to perform SSRF and fetch internal resources like files on localhost.

## Description

Exploiting the SSRF in /apps/dav/lib/BackgroundJob/RefreshWebcalJob.php, an authenticated user creates an ICS event with the bypass URL. The job fetches the URL, removing brackets and validating with filter_var, but failing to detect the embedded private IP, allowing the server to request internal endpoints with its privileges, leading to data exfiltration.

## Requirements

1. Authenticated session to Nextcloud
2. Malicious WebCal URL crafted (e.g., targeting /secret.ics on 127.0.0.1)
3. Python environment with requests library for the POC script
4. Target Nextcloud URL and credentials

## Defense

Defensive measures and detection strategies:

- Patch Nextcloud to validate IPv6 embeddings properly (e.g., parse and check all IP components)
- Disable or monitor WebCal subscriptions in Calendar app
- Implement request logging for DAV endpoints and alert on private IP fetches
- Use web application firewall (WAF) rules to block suspicious IPv6 patterns

## Objectives

1. Create a calendar event that embeds the SSRF URL in ICS format
2. Trigger server-side fetch to internal resource
3. Exfiltrate or observe data from localhost services

## Instructions

### Step 1: Prepare ICS Payload

**Context**: Embed the malicious URL in a VCALENDAR structure for the event.

**Command** (Manual or Script Prep):

Create ICS content: `BEGIN:VCALENDAR ... URL:http://[0:0:0:0:0:ffff:127.0.0.1]:80/secret.ics ... END:VCALENDAR`

> The URL is subscribed as a WebCal source, prompting the job to fetch it.

### Step 2: Execute Exploitation Script

**Context**: Use the Python tool to authenticate and submit the event via DAV API.

**Command** ([[commands/nextcloud-ssrf-exploit]]):
```bash
python nextcloud_ssrf.py http://192.168.0.105/nextcloud/nextcloud/ admin "[password]" http://[0:0:0:0:0:ffff:127.0.0.1]:80/secret.ics
```

> Authenticates, creates the event, and the job runs, fetching the internal file. Check calendar or logs for results.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/nextcloud-ssrf-exploit]]

## Tools Used

- [[tools/nextcloud_ssrf.py]]

## Tags

- ssrf
- calendar
- dav
- exploitation
