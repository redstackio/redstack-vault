---
id: proc-hackerone-csv-enumeration
tags:
  - access-control
  - information-disclosure
  - enumeration
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:47.120Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Account Discovery]]'
---
# Distinguish-HackerOne-Program-Types-via-CSV-Endpoint

## Summary

This procedure exploits improper access control on HackerOne's /terms_acceptance_data.csv endpoint to differentiate between sandboxed (public) and private bug bounty programs. By accessing the endpoint with various program handles using a logged-in account, attackers can observe response differences—successful CSV downloads for sandboxed programs versus distinct errors for private ones—enabling enumeration and confirmation of private program existence, which leaks confidentiality.

## Description

The vulnerability stems from the advanced vetting page's CSV download feature, intended for sandboxed programs. Logged-in users can access https://hackerone.com/{handle}/terms_acceptance_data.csv for any handle. For sandboxed programs, it returns a downloadable CSV with default content; for private programs, it returns a unique error (not a standard 404), confirming the program's existence without granting access. This allows attackers to guess handles (e.g., from public leaks or patterns) and systematically enumerate private programs, compromising the platform's privacy model. Discovered by testing the endpoint directly in a browser after examining the vetting interface. Impact includes broad information disclosure for all private HackerOne programs.

## Requirements

1. Active logged-in HackerOne account (any user permissions suffice).
2. Web browser for manual probing or scripting tool (e.g., curl) for automation.
3. List of potential program handles to test (guessed or sourced externally).
4. Basic understanding of HTTP responses and URL manipulation.

## Defense

Defensive measures and detection strategies:

- Implement uniform error responses (e.g., consistent 404 for all non-existent or restricted resources) to prevent response-based oracle attacks.
- Rate-limit endpoint access per user/IP to detect and block enumeration attempts.
- Audit logs for repeated /terms_acceptance_data.csv requests with varying handles; alert on anomalies.
- Restrict endpoint to authorized users only via proper authentication checks, regardless of program type.

## Objectives

1. Confirm sandboxed program accessibility via successful CSV download.
2. Identify private programs through distinct error responses on failed access.
3. Enumerate and verify existence of guessed private handles, achieving information disclosure.

## Instructions

### Step 1: Log In and Prepare Test Handles

**Context**: Ensure authenticated access and have a list of handles ready—one known sandboxed (e.g., `test_pie77`) and several guessed private ones.

Log in to HackerOne via your browser at https://hackerone.com.

> Expected: Session established; you can access user dashboard.

### Step 2: Probe Sandboxed Program Endpoint

**Context**: Test the baseline response for an accessible program to understand success indicators.

Navigate directly to `https://hackerone.com/test_pie77/terms_acceptance_data.csv` in your browser.

> Expected: Browser prompts download of a CSV file with default terms acceptance data (e.g., empty or placeholder rows). HTTP status: 200 OK.

### Step 3: Probe Private Program Endpoint

**Context**: Use a suspected private handle to observe the differential response, confirming existence without access.

Replace the handle and access `https://hackerone.com/{guessed_private_handle}/terms_acceptance_data.csv` (e.g., `https://hackerone.com/private_example/terms_acceptance_data.csv`).

> Expected: Error page or message (e.g., "Access denied" or custom HackerOne error, not 404), indicating the program exists but is private. No CSV download.

### Step 4: Automate Enumeration (Optional Scaling)

**Context**: For bulk testing, script repeated requests to guess handles and log responses.

Use a tool like curl to iterate over a list of handles:

```bash
for handle in $(cat handles.txt); do
  curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" "https://hackerone.com/$handle/terms_acceptance_data.csv"
done
```

> Expected: 200 for sandboxed (potential download), non-404 errors for private (e.g., 403 or 422), 404 for non-existent. Parse to identify privates.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control
- information-disclosure
- enumeration
- hackerone
