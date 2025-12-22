---
id: proc-modify-csrf-token-null
tags:
  - csrf
  - token-bypass
  - false-positive
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.636Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Modify-Authenticity-Token-to-Null

## Summary

This procedure involves editing the generated CSRF PoC HTML to set the authenticity_token parameter to an empty (null) value, simulating a token bypass attempt while preserving other form parameters for testing unauthorized site configuration changes in Files.com.

## Description

Ruby on Rails applications use authenticity_tokens for CSRF protection, embedded in forms and validated on submission. By nullifying the token in the PoC, this tests if the server accepts the request without validation, potentially allowing changes to sensitive settings like site name, email, subdomain, SSL requirements, and password policies. In this case, the modification targeted the first token in a duplicate pair, creating an illusion of bypass since the second unmodified token was validated, leading to a false positive.

## Requirements

1. Generated CSRF PoC HTML file from Burp Suite.
2. Text editor (e.g., VS Code, Notepad++) to modify the file.
3. Understanding of HTML forms and multipart/form-data structure.

## Defense

Defensive measures and detection strategies:

- Ensure CSRF tokens are unique and validated strictly, rejecting null or empty values.
- Avoid duplicate tokens; use single, properly bound tokens per form.
- Log and alert on requests with missing or invalid tokens.
- Implement custom headers (e.g., Origin, Referer) checks for cross-site requests.

## Objectives

1. Simulate token bypass to test CSRF protection efficacy.
2. Modify payload parameters to verify impact if bypass succeeds.
3. Prepare PoC for submission testing.
4. Expected outcome: Modified PoC that appears to evade protection (but fails in reality due to duplicates).

## Instructions

### Step 1: Open PoC File

**Context**: Locate the authenticity_token in the HTML form or JavaScript body.

**Instructions**: Open the generated HTML in a text editor and search for "authenticity_token".

### Step 2: Nullify Token Value

**Context**: Replace the token value with an empty string to attempt bypass.

**Instructions**: In the multipart body string (within the submitRequest() function or form fields), change the line for authenticity_token from something like "authenticity_token=actual_token_value" to "authenticity_token=\r\n\r\n" (empty value). Leave the second duplicate token (if present) unmodified.

### Step 3: Alter Payload Parameters

**Context**: Update site settings in the PoC to test for unauthorized changes.

**Instructions**: Modify parameters such as site[name] to 'gamingtoooorrrrr' and site[email] to 'hmahmoud@promex.me', while keeping others like site[subdomain]=gaming2, site[language]=en, etc.

> The full body will resemble: "-----------------------------boundary\r\nContent-Disposition: form-data; name=\"authenticity_token\"\r\n\r\n\r\n\r\n" for the empty token.

**Expected Output**: Updated HTML PoC with null token and modified settings ready for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-bypass]]
- [[false-positive]]
- [[web]]
