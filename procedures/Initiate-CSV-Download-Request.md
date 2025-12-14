---
id: proc-initiate-download-001
tags:
  - web
  - idor
  - download
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.199Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Initiate-CSV-Download-Request

## Summary

This procedure triggers the CSV download functionality on the quiz reports page, generating an HTTP GET request to the vulnerable endpoint that includes the USERID parameter.

## Description

Targeting the /reports/quizzes-taken-by-user.csv/USERID endpoint in the Drupal 8-based training portal, clicking the download button sends a request tied to the authenticated user's ID. This step is crucial for interception and modification in IDOR attacks. It assumes prior access to the reports page and a proxied connection. Successful execution results in a downloadable CSV for the user's own data, but sets up exploitation.

## Requirements

1. Active session on the reports page
2. Burp Suite proxy enabled
3. No ad blockers interfering with the download link

## Defense

Defensive measures and detection strategies:

- Rate-limit download requests per user to prevent abuse.
- Log all CSV export attempts with USERID for anomaly detection.

## Objectives

1. Generate the interceptable HTTP request.
2. Confirm the endpoint's parameter exposure.
3. Prepare for parameter tampering.

## Instructions

### Step 1: Trigger Download

**Context**: Initiate the request to expose the USERID in the URL path.

No command; browser action:

- Click the "Download CSV" button on https://training.smartpay.gsa.gov/reports/quizzes-taken-by-user.

> This sends a GET to /reports/quizzes-taken-by-user.csv/1226357 (attacker's ID). The request should be intercepted by Burp if configured.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web]]
- [[idor]]
