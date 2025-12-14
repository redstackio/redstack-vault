---
id: proc-pressable-leak-credentials
tags:
  - leak
  - credentials
  - pressable
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:33:24.396Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Receive Error Response Leaking Credentials

## Summary

This procedure sends the modified IDOR request to provoke an error response that inadvertently leaks the victim's Client ID and Client Secret due to poor error handling in the Pressable API.

## Description

The endpoint returns an error for missing 'name' but renders the full application page for the targeted ID, exposing sensitive credentials. This is a critical flaw in the authorization and error handling of the Ruby on Rails backend, allowing full API access post-leak.

## Requirements

1. Modified POST request ready
2. Proxy to view response
3. Target ID confirmed

## Defense

Defensive measures and detection strategies:

- Avoid rendering full pages in error responses; return generic errors
- Scrub sensitive data from all responses, especially errors
- Implement content security policies

## Objectives

1. Trigger 'Name must be provided' error
2. Extract Client ID and Client Secret
3. Confirm leak via response inspection

## Instructions

### Step 1: Forward Modified Request

**Context**: Send the request to receive the leaking response.

No specific command; forward in proxy:

- In Burp, forward the modified POST to /api/applications
- Inspect the HTML response

> Response shows error but includes <div> with Client ID: xxx and Client Secret: yyy. Copy these values.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[leak]]
- [[Credentials]]
- [[pressable]]
