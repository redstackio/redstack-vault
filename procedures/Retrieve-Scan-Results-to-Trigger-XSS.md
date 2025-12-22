---
tags:
  - xss
  - execution
  - results-retrieval
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
updated_at: '2025-12-14T03:15:41.787Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f780610b-de6a-4485-84ab-2393d669506c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Retrieve-Scan-Results-to-Trigger-XSS

## Summary

This procedure fetches the scan results from the Nextcloud API and views the results page, where the unescaped data.url is inserted via innerHTML, executing the stored XSS payload in the site's context.

## Description

After queuing, the /api/result/<UUID> returns JSON with data.url unescaped (unlike other fields). The frontend at /results/<UUID> uses innerHTML to display it, interpreting the path's HTML/JS. This leads to execution on scan.nextcloud.com, potentially bypassing CSP if subdomains are trusted.

## Requirements

1. UUID from queuing step
2. Browser for viewing results
3. Optional: curl for API fetch

## Defense

Defensive measures and detection strategies:

- Escape all JSON fields with escapeHTML
- Use DOM textContent for URL rendering
- Enforce strict CSP without unsafe-inline
- Monitor JS errors and unusual DOM insertions

## Objectives

1. Retrieve stored malicious URL
2. Trigger JS execution on results page
3. Demonstrate impact like alerts or theft

## Instructions

### Step 1: Fetch API Results

**Context**: Get the JSON containing the unescaped URL.

**Command** (curl):
```bash
curl https://scan.nextcloud.com/api/result/<UUID>
```

> Returns JSON with data.url including the payload. Expected output: {"data":{"url":"http://attacker.com/heh<script>alert(1)</script>/status.php",...}}.

### Step 2: View Results Page

**Context**: Load the page to trigger innerHTML insertion and execution.

**Instructions**: Navigate to https://scan.nextcloud.com/results/<UUID> in a browser.

> The payload executes on load, showing alert(1). Inspect DOM to confirm unescaped insertion.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- results-retrieval
