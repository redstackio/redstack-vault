---
id: proc-craft-malicious-swagger-json
tags:
  - xss
  - json-injection
  - swagger-ui
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.380Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Swagger-JSON

## Summary

This procedure involves modifying a Swagger API specification JSON file to inject a JavaScript XSS payload into a renderable field, enabling arbitrary code execution when loaded in a vulnerable Swagger UI instance.

## Description

In the context of exploiting reflected XSS in older Swagger UI versions, such as on the Zomato developers portal, user-supplied data in the API spec JSON is not sanitized. By injecting payloads into properties like 'photoUrls' in the 'Pet' definition, the rendering process executes the script in the browser. This targets documentation pages that dynamically load and parse external Swagger specs.

## Requirements

1. Access to a base Swagger JSON file (e.g., Petstore sample)
2. Text editor capable of handling JSON
3. Knowledge of valid JSON structure to avoid parsing errors

## Defense

Defensive measures and detection strategies:

- Upgrade to latest Swagger UI versions with input sanitization
- Validate and escape all user-supplied data in API specs before rendering
- Implement Content Security Policy (CSP) to block inline scripts

## Objectives

1. Embed XSS payload in JSON without invalidating the spec
2. Ensure payload targets a field that Swagger UI renders as HTML/JS
3. Prepare for hosting and loading in target UI

## Instructions

### Step 1: Obtain Base Swagger JSON

**Context**: Start with a standard Swagger file to maintain compatibility.

Download or copy the sample Petstore Swagger JSON from the official Swagger repository.

### Step 2: Inject XSS Payload

**Context**: Modify a string property in the schema to include the script tag, leveraging lack of sanitization.

Edit the 'Pet' definition under 'definitions'. Append the payload to 'photoUrls': change it to "photoUrls<script>alert(document.cookie)</script>". For more advanced payloads, use data exfiltration like sending cookies to an attacker-controlled server.

> Ensure the JSON remains valid; test parsing with a JSON validator.

### Step 3: Validate Injection

**Context**: Confirm the modified JSON parses correctly.

Use an online JSON validator or a tool like jq to parse the file. Look for no syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[json-injection]]
