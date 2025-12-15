---
tags:
  - php
  - backend
  - api
type: procedure
tools:
  - '[[tools/php]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-server-start]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.229Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 20d2be57-b75c-410e-8654-6a072b231d52
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start-PHP-Backend-API

## Summary

Starts a PHP development server to host the backend API that processes multipart form data from Node.js requests, vulnerable to tampering of fields like customer_id.

## Description

order.php handles POST requests, parsing multipart fields (price, customer_id, item_id, description) and simulating order processing. Running on port 2000, it receives requests from the Node.js server. The vulnerability allows tampered fields to bypass controls, leading to unauthorized modifications. This procedure simulates a backend API in a web environment.

## Requirements

1. PHP runtime installed
2. Port 2000 available
3. order.php in current directory

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all multipart fields server-side
- Use secure random for any backend randomness
- Log and alert on anomalous field values (e.g., unexpected customer_id changes)

## Objectives

1. Host the API endpoint for order processing
2. Enable reception of potentially tampered multipart data
3. Demonstrate impact of boundary prediction on field integrity

## Instructions

### Step 1: Launch PHP Server

**Context**: Bind and start the server on localhost port 2000.

**Command** ([[commands/php-server-start]]):
```bash
php -S 127.0.0.1:2000
```

> Starts the server. Expected output: PHP server running, ready to handle /order.php.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/php-server-start]]

## Tools Used

- [[tools/php]]

## Tags

- development-server
- form-processing
