---
id: proc-uuid-002
tags:
  - token-extraction
  - information-gathering
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-extract-token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:44.933Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-Security-Token-from-Misc-Page

## Summary

This procedure retrieves a valid XOOPS security token from the unauthenticated /misc.php page in ImpressCMS, which can be reused to bypass authorization in other endpoints.

## Description

ImpressCMS generates security tokens in public pages like /misc.php?action=showpopups&type=friend (line 181 in source), embedding them in HTML as 'XOOPS_TOKEN_REQUEST'. Attackers can view source without auth to copy the token, exploiting the lack of protection on token generation. This enables chaining to restricted features, resulting in user data exposure.

## Requirements

1. Access to the public /misc.php endpoint
2. Browser dev tools or grep-capable tool like curl
3. Target domain resolved

## Defense

Defensive measures and detection strategies:

- Restrict token generation to authenticated sessions only
- Obfuscate or encrypt tokens in HTML output
- Monitor for anomalous token extractions via logs

## Objectives

1. Obtain a reusable security token
2. Validate token availability in public contexts
3. Prepare for authorization bypass

## Instructions

### Step 1: Access Misc Page

**Context**: Load the popup page to generate the token in HTML.

Use browser to visit http://target.com/misc.php?action=showpopups&type=friend.

> View source (Ctrl+U) and search for XOOPS_TOKEN_REQUEST.

### Step 2: Scripted Token Extraction

**Context**: Automate fetching and parsing the HTML for the token.

**Command** ([[commands/curl-extract-token]]):
```bash
curl "http://target.com/misc.php?action=showpopups&type=friend" | grep -o 'XOOPS_TOKEN_REQUEST[^<]*'
```

> Outputs the token string; copy the value after the equals sign.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-extract-token]]

## Tools Used


## Tags

- [[token-extraction]]
- [[information-gathering]]
