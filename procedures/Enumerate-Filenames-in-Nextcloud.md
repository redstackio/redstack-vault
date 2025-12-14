---
id: proc-nextcloud-filename-enum-2017
tags:
  - information-disclosure
  - nextcloud
  - filename-enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:37.545Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Enumerate-Filenames-in-Nextcloud

## Summary

This procedure exploits a filename enumeration vulnerability in Nextcloud Server (CVE-2017-0885) to unauthorizedly discover existing filenames and potentially sensitive file paths without proper access controls, enabling further reconnaissance or targeted attacks.

## Description

Nextcloud Server, a popular file hosting service, contains a vulnerability where error responses or endpoint behaviors allow attackers to infer the existence of specific filenames through differential responses. This information disclosure occurs in public sharing or file access endpoints, where guessing filenames leads to leaks via HTTP status codes, response times, or error messages. The attack targets web-accessible Nextcloud instances and requires no authentication if exploiting public features. Expected outcomes include a list of discoverable files, which could reveal sensitive data structures for subsequent exploitation. Prerequisites include network reachability to the target and basic web request tools.

## Requirements

1. Direct network access to the Nextcloud web server (HTTP/HTTPS on ports 80/443).
2. Knowledge of Nextcloud's URL structure, particularly file sharing or apps/files endpoints.
3. Ability to send and analyze HTTP requests/responses.

## Defense

Defensive measures and detection strategies:

- Implement consistent error responses (e.g., generic 404 for all non-existent resources) to prevent information leakage.
- Rate-limit requests to file access endpoints to hinder enumeration attempts.
- Monitor access logs for patterns of sequential filename guesses or high request volumes from single IPs.

## Objectives

1. Discover unauthorized filenames and directory hints in Nextcloud.
2. Gather intelligence for potential follow-on attacks like targeted DoS or access attempts.
3. Validate the presence of sensitive files without triggering alerts.

## Instructions

### Step 1: Identify Target Endpoints

**Context**: Locate vulnerable endpoints in Nextcloud, such as public file shares or the files app, where filename guesses can be tested.

Navigate to the Nextcloud instance and inspect URLs for patterns like `/index.php/apps/files/?dir=/&filename=example.txt` or public preview links.

### Step 2: Probe for Filename Existence

**Context**: Send requests with guessed filenames and analyze responses for differences indicating existence.

Use a web browser or command-line tool to test common filenames (e.g., config.php, backup.sql, private.docx):

```bash
curl -s -w "%{http_code}" "https://target-nextcloud.com/index.php/apps/files_sharing/public?token=abc&path=/guessedfile.txt" -o /dev/null
```

> A 200 or custom error with filename mention indicates existence; a standard 404 suggests non-existence. Iterate with wordlists of common filenames.

### Step 3: Automate Enumeration

**Context**: Scale the probing to cover multiple possibilities efficiently.

Script repeated requests against a list of potential names, logging response anomalies:

```bash
while read filename; do
  response=$(curl -s -w "%{http_code}:%{time_total}" "https://target-nextcloud.com/index.php/apps/files/?filename=$filename" -o /dev/null)
  echo "$filename: $response" >> enum_results.txt
  sleep 1  # Avoid rate limits

done < filenames_wordlist.txt
```

> Successful automation yields a filtered list of confirmed filenames based on response patterns.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- nextcloud
- filename-enumeration
