---
tags:
  - information-disclosure
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:58.346Z'
sub_techniques: []
id: cc5df272-950f-4fa9-87c5-86d7ce57fa74
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Access Information Disclosure Endpoint

## Summary

This procedure accesses an unauthenticated endpoint on the MASS platform to retrieve personally identifiable information (PII) for a user account, including names, mobile numbers, emails, and security pins, setting the stage for further enumeration and exploitation.

## Description

The MASS platform exposes a web endpoint that lacks authentication, allowing any unauthenticated user to access sensitive PII by providing a numeric user ID parameter. This is a classic information disclosure vulnerability, discovered on a U.S. Department of Defense system, enabling attackers to view critical data without restrictions. The procedure targets this endpoint directly via a web browser, revealing data that can be used in subsequent attack steps like password resets.

## Requirements

1. Web browser with internet access
2. Knowledge of the target URL structure (e.g., redacted `https://www.████████/███████?id=123`)
3. No authentication credentials needed

## Defense

Defensive measures and detection strategies:

- Implement authentication and authorization on all endpoints handling user data
- Use proper input validation and parameter sanitization to prevent direct object access
- Monitor access logs for anomalous requests to sensitive endpoints, such as repeated numeric parameter changes

## Objectives

1. Retrieve PII for a target user account
2. Confirm the vulnerability exists without authentication
3. Gather data for enumeration in follow-on procedures

## Instructions

### Step 1: Navigate to the Endpoint

**Context**: Directly access the vulnerable URL to fetch user data.

No specific command required; use a web browser to visit the endpoint, e.g., `https://www.████████/███████?id=123` (replace with actual redacted URL and a starting numeric ID).

> The response will display or return PII such as first name, last name, mobile number, email, and pin in JSON or HTML format. Verify the data is unredacted and sensitive.

### Step 2: Inspect the Response

**Context**: Examine the returned data to confirm disclosure.

Use browser developer tools (F12) to view the network response or page source.

> Look for fields like `first_name`, `email`, `pin`. Successful output includes complete user details without login prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[web-vuln]]
