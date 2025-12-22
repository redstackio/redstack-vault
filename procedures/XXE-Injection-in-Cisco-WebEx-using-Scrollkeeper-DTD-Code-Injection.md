---
id: b7441718-56b4-4cb9-bdd4-a884b635d931
name: XXE-Injection-in-Cisco-WebEx-using-Scrollkeeper-DTD-Code-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.479480+00:00'
updated_at: '2023-04-10T20:24:39.529287+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xxe
  - cisco-webex
  - dtd-injection
  - code-execution
  - xml-external-entity
commands:
  - '[[commands/curl-send-xxe-xml-payload]]'
platforms:
  - Web
  - Windows
tools:
  - '[[tools/Burp-Suite]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# XXE-Injection-in-Cisco-WebEx-using-Scrollkeeper-DTD-Code-Injection

## Summary

This procedure exploits the Scrollkeeper DTD Code Injection vulnerability in Cisco WebEx to achieve arbitrary code execution on the target system. By crafting a malicious XML file that references a local DTD entity on the server, the parser loads and executes embedded malicious code within the DTD, allowing remote attackers to bypass security controls and gain initial access.

## Description

The Scrollkeeper DTD Code Injection vulnerability in Cisco WebEx enables attackers to execute arbitrary code remotely. The attack involves submitting a specially crafted XML payload to a vulnerable endpoint in the WebEx application. This XML includes an external entity declaration that points to a local DTD file on the target's filesystem (e.g., within the Scrollkeeper documentation directory). When the application parses the XML, it resolves the entity by loading the DTD, which contains injected malicious instructions. These can include system commands or file operations leading to code execution. This technique is particularly effective against unpatched WebEx installations and requires no authentication if the endpoint is public-facing. The procedure assumes the target is a Windows-based WebEx server, and success results in remote command execution, potentially leading to persistence or data exfiltration.

## Requirements

1. Network access to the vulnerable Cisco WebEx application endpoint (e.g., HTTP/HTTPS port 80/443 open).
2. Knowledge of the target's filesystem structure, particularly the Scrollkeeper DTD location (typically in program files or app data directories on Windows).
3. Ability to craft and transmit XML payloads, using tools like Burp Suite for interception and modification.
4. A listening server on the attacker's side if the payload involves reverse connections (optional for basic exploitation).

## Defense

Defensive measures and detection strategies:

- Ensure the Cisco WebEx application is up-to-date with the latest security patches to mitigate known XXE vulnerabilities.
- Implement network segmentation to prevent remote access to critical systems and endpoints.
- Deploy a web application firewall (WAF) configured to detect and block XXE payloads, including external entity references in XML.
- Disable external entity processing in XML parsers (e.g., via libxml2 settings or application configuration).
- Monitor application logs for anomalous XML parsing errors or unexpected file access in Scrollkeeper directories.

## Objectives

1. Gain remote access to the target system via code execution.
2. Execute arbitrary commands on the target WebEx server.
3. Bypass authentication and security controls to establish a foothold.

## Instructions

### Step 1: Craft Malicious XML Payload

**Context**: Create the initial XML file that declares an external entity pointing to the local Scrollkeeper DTD on the target. This tricks the parser into loading the malicious DTD. Use the [[codes/Malicious-Scrollkeeper-DTD-for-XXE-Code-Injection]] code snippet as the basis for the DTD content, and embed the entity reference in your XML.

Replace placeholders in the XML with the actual path to the Scrollkeeper DTD (e.g., file:///C:/Program Files/Cisco/WebEx/scrollkeeper.dtd). Save this as an XML file for submission.

**Why**: This step sets up the entity resolution to load the attacker's injected DTD content.

### Step 2: Prepare and Inject the Payload

**Context**: Use a tool like Burp Suite to intercept and modify requests to the WebEx upload or processing endpoint. Submit the crafted XML, ensuring the external entity is processed.

**Command** ([[commands/curl-send-xxe-xml-payload]]):
```bash
curl -X POST -H "Content-Type: application/xml" --data @malicious.xml http://target-webex.example.com/vulnerable-endpoint
```

> This command sends the XML payload to the vulnerable endpoint. If using Burp, route the traffic through the proxy (e.g., 127.0.0.1:8080) by adding --proxy to curl. Expected output includes a successful HTTP 200 response or parsed XML acknowledgment; monitor for parser errors indicating entity resolution.

**Why**: Directly injects the payload to trigger the XXE, loading the DTD and executing the embedded code.

### Step 3: Verify Exploitation and Execute Code

**Context**: After submission, check for signs of execution, such as a reverse shell connection or file creation on the target (if the DTD includes such actions). If the DTD is set up for command execution, it may write output to a web-accessible directory or connect back to the attacker.

Use server logs or a listener (e.g., netcat) to confirm. If no immediate output, probe the target for artifacts like newly created files in temp directories.

**Why**: Validates successful code execution and allows further post-exploitation.

**Decision Point**: If the response shows XML parsing errors without entity expansion, the DTD path may be incorrect—adjust and retry. Otherwise, proceed to lateral movement.
