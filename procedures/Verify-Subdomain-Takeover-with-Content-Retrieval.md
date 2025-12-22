---
tags:
  - verification
  - curl-fetch
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-content-retrieval]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:39.981Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: fbf185d3-165f-4359-8ff9-d56de16a56ce
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-Subdomain-Takeover-with-Content-Retrieval

## Summary

This procedure fetches content from the taken-over subdomain to confirm attacker control and successful hijacking.

## Description

After upload, retrieve the file via HTTP to the subdomain, verifying it serves custom content instead of errors. Uses tools like curl for simple GET requests. Applicable post-S3 takeover; confirms impact like arbitrary serving. No auth needed if public; outcomes validate the exploit chain.

## Requirements

1. Taken-over subdomain accessible
2. Uploaded content in place
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Implement content security policies (CSP) on relying apps
- Monitor subdomain traffic for unexpected payloads
- Use certificate transparency logs for rogue TLS

## Objectives

1. Confirm custom content delivery
2. Validate takeover completeness
3. Document proof for reporting

## Instructions

### Step 1: Fetch Subdomain Content

**Context**: Request the uploaded file to check if the subdomain serves it.

**Command** ([[commands/curl-content-retrieval]]):
```bash
curl images.crossinstall.com/index.html
```

> This retrieves the HTML; expected output: <!-- hackerone/ian bugcrowd/iangcarroll -->, proving control.

### Step 2: Check Headers if Needed

**Context**: Inspect response headers for S3 origins or errors.

**Command** (Extended curl):
```bash
curl -I images.crossinstall.com/index.html
```

> Verify 200 OK and Server: AmazonS3 header.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-content-retrieval]]

## Tools Used

- [[tools/curl]]

## Tags

- [[takeover-verification]]
- [[http-fetch]]
