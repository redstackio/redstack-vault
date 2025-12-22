---
id: proc-infogram-create-xss-001
tags:
  - api-injection
  - stored-xss
type: procedure
tools:
  - '[[tools/Infogram-Java-API-Library]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/Initialize-Infogram-API-Client]]'
  - '[[commands/Send-POST-Request-to-Infographics]]'
  - '[[commands/Handle-Successful-API-Response]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:10.716Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Create-Infographic-via-API-to-Inject-Stored-XSS

## Summary

This procedure uses the Infogram Java API to submit a POST request to /infographics with a malicious 'content' payload, storing XSS that executes upon dashboard viewing.

## Description

Exploiting lack of input sanitization, the API accepts and stores unsanitized JSON, reflecting it in user views. This targets the creation endpoint, requiring auth via key/secret. In attack scenarios, it allows persistent JS execution for session theft or phishing. Prerequisites: Prepared parameters and initialized client. Outcomes: Infographic created with ID, ready for triggering.

## Requirements

1. Valid API key and secret
2. Java code with parameters map from prior step
3. Network access to Infogram API

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all JSON fields in API inputs, rejecting unsafe HTML/JS
- Implement server-side escaping for reflected content
- Audit API responses for anomalous payloads and alert on suspicious creations

## Objectives

1. Successfully create infographic with injected XSS
2. Confirm storage via 201 response
3. Enable subsequent dashboard-based execution

## Instructions

### Step 1: Initialize API Client

**Context**: Authenticate the library instance.

Execute [[commands/Initialize-Infogram-API-Client]]:

```java
InfogramAPI infogram = new InfogramAPI([API-Key], [API-Secret]);
```

> Replace placeholders with actual credentials. Expected: Authenticated instance.

### Step 2: Submit POST Request

**Context**: Send parameters to creation endpoint.

Execute [[commands/Send-POST-Request-to-Infographics]]:

```java
Response response = infogram.sendRequest("POST", "infographics", parameters);
```

> Uses the map with XSS content. Expected: Response object.

### Step 3: Verify and Print Response

**Context**: Check success and extract details.

Execute [[commands/Handle-Successful-API-Response]]:

```java
if (response.isSuccessful()) { InputStream is = response.getResponseBody(); System.out.print(getStringFromInputStream(is).replace(",", ",\n")); }
```

> Prints formatted body. Expected: 201 status and infographic JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/Initialize-Infogram-API-Client]]
- [[commands/Send-POST-Request-to-Infographics]]
- [[commands/Handle-Successful-API-Response]]

## Tools Used

- [[tools/Infogram-Java-API-Library]]

## Tags

- api-exploit
- xss-injection
