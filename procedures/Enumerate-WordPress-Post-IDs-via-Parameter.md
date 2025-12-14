---
tags:
  - enumeration
  - wordpress
  - post-id
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:24:56.482Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9a3973a0-88c3-428c-b5de-7cf6d54ac428
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Enumerate-WordPress-Post-IDs-via-Parameter

## Summary

This procedure involves systematically querying a WordPress site's 'p' GET parameter with sequential IDs to identify valid posts, triggering 301 redirects that disclose full paths to hidden pages, enabling further discovery of sensitive endpoints.

## Description

In WordPress, the 'p' parameter is used to access posts by ID. Due to predictable sequential IDs and improper handling of invalid requests, attackers can enumerate from 1 to a large range (e.g., 10000) to find valid entries. Successful requests return 301 redirects with Location headers revealing the actual URL paths, such as /event/ or /non-profit/, which may include or lead to unprotected resources. This technique exploits the site's public-facing nature and lack of rate limiting or obfuscation, applicable to any WordPress instance without custom protections.

## Requirements

1. Access to a public WordPress site via HTTP/HTTPS
2. Tool for sending HTTP requests (e.g., curl, browser dev tools, or scripting language like Python)
3. Basic scripting knowledge to automate iteration over ID ranges

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on parameter-based requests to prevent enumeration
- Use non-sequential or obfuscated post IDs
- Monitor access logs for sequential ?p= queries and block suspicious IPs
- Redirect invalid post requests to a generic error page without exposing paths

## Objectives

1. Identify valid post IDs and their corresponding hidden paths
2. Map the site's structure for potential sensitive endpoints
3. Gather intelligence on unpublished or restricted content

## Instructions

### Step 1: Prepare Enumeration Script

**Context**: Set up an automated way to query the parameter, as manual testing is inefficient for large ranges.

Use curl in a loop to request each ID and capture the Location header:

```bash
for id in {1..10000}; do
  response=$(curl -s -w "%{http_code} %{redirect_url}" -o /dev/null "https://target.org/?p=$id")
  if [[ $response == 301* ]]; then
    echo "Valid ID $id: ${response#* }"
  fi
done > enumerated_paths.txt
```

> This command sends HEAD-like requests (using -I for efficiency) and filters for 301 responses, extracting the redirect URL. Expected output: Lines like "Valid ID 1657: https://target.org/event/ijebu-2019/".

### Step 2: Analyze Responses

**Context**: Review the collected paths to identify patterns indicating export or data pages.

Manually inspect enumerated_paths.txt for paths containing keywords like 'export', 'download', or timestamps (e.g., /do_action-export-1498557984/).

**Expected Output**: A filtered list of potentially sensitive endpoints ready for further testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[enumeration]]
- [[wordpress]]
- [[Reconnaissance]]
