---
tags:
  - open-redirect
  - url-manipulation
  - shopify
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.552Z'
sub_techniques: []
id: 02f7c575-3b1e-41ed-a265-7ed8b306a0b4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Copy-and-Modify-Search-Result-URL

## Summary

This procedure details extracting a search result URL from the Shopify dev site and modifying the 'result_url' parameter by prepending '@' to an external domain, exploiting insufficient validation to enable open redirects.

## Description

Following a search on shopify.dev, this step involves copying a result link and editing its 'result_url' parameter. The vulnerability stems from the site's logic not properly handling the '@' character, treating the suffix as a new target URL and bypassing checks for shopify.dev domains only. This is typically done manually in a text editor or browser dev tools. The outcome is a crafted URL that, when accessed, redirects externally, useful for phishing setups requiring user clicks.

## Requirements

1. Copied search result URL from previous search
2. Text editor or browser address bar for modification
3. Knowledge of URL encoding (basic, as '@' is not encoded here)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize 'result_url' parameters strictly, rejecting '@' or similar bypass characters
- Use whitelisting for allowed domains/paths in redirects
- Log and alert on parameter modifications in search endpoints

## Objectives

1. Create a maliciously altered URL that evades redirect restrictions
2. Preserve other parameters to maintain functionality
3. Test the modified URL syntax for validity

## Instructions

### Step 1: Copy Result Link

**Context**: Select and extract the full URL of a search result for editing.

Right-click the first result (e.g., 'POS') and copy the link address.

> Copied URL example: https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=%2Ftools%2Fapp-bridge%2Factions%2Fpos&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false.

### Step 2: Identify and Edit Parameter

**Context**: Locate the 'result_url' and replace its value to inject the bypass.

In the URL, find &result_url= followed by its value, and change it to &result_url=@www.facebook.com (replace with desired external domain).

> Modified URL example: https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=@www.facebook.com&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false.

### Step 3: Validate Modification

**Context**: Ensure the URL is correctly formed before use.

Review the edited URL for proper syntax and parameter integrity.

> No errors in parsing; ready for access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-manipulation]]
- [[bypass]]
