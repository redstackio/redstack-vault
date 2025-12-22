---
id: 8ad33483-e45a-4ead-8d27-9346f3b97c86
name: XSLT-Injection-for-File-Read-and-SSRF
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.497456+00:00'
updated_at: '2023-04-10T20:24:50.379204+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/XSLT-Injection]]'
  - '[[tags/SSRF]]'
  - '[[tags/File-Read]]'
commands:
  - '[[commands/curl-send-xslt-payload]]'
platforms:
  - Web
  - Linux
  - Windows
tools: []
validated: true
---

# XSLT-Injection-for-File-Read-and-SSRF

## Summary

This procedure demonstrates how to exploit XSLT injection vulnerabilities to read sensitive local files and perform Server-Side Request Forgery (SSRF) by injecting malicious XSLT code into an application's XML processing pipeline. It targets web applications that dynamically apply user-supplied XSLT stylesheets to XML data, allowing attackers to use the document() function to access internal files or make unauthorized internal/external requests.

## Description

XSLT Injection occurs when an application processes user-controlled input as part of an XSLT stylesheet without proper validation, enabling attackers to inject arbitrary XSLT elements. This procedure focuses on leveraging the document() function within the injected XSLT to load and include content from local files (e.g., /etc/passwd on Linux or win.ini on Windows) or remote URLs for SSRF. The attack assumes the target application transforms XML input using the injected stylesheet, outputting the results in HTML or another format. This technique is effective against legacy systems or misconfigured XML parsers in web apps, leading to data exfiltration or internal network pivoting. Prerequisites include identifying an endpoint that accepts XML with XSLT parameters, such as a search or report generation feature.

## Requirements

1. Network access to a vulnerable web application endpoint that processes user-supplied XSLT (e.g., via POST requests with XML payloads).
2. Knowledge of the target's file system paths for local file reads (e.g., /etc/passwd for Linux users, c:/winnt/win.ini for Windows config).
3. Attacker-controlled server for SSRF callbacks (e.g., to receive internal requests).
4. Tools like curl for sending payloads or Burp Suite for interception and modification.
5. Basic understanding of XML/XSLT syntax to craft payloads without breaking the transformation.

## Defense

Defensive measures and detection strategies:

- Disable or restrict the document() function in XSLT processors (e.g., via secure processing mode in libxslt).
- Validate and sanitize all XML/XSLT inputs, whitelisting allowed elements and functions only.
- Implement network controls to block SSRF, such as firewall rules denying internal requests from web servers.
- Monitor application logs for anomalous XSLT processing, unusual file access, or outbound connections to attacker IPs.
- Use Web Application Firewalls (WAFs) with rules to detect XSLT injection patterns like <xsl:copy-of> or document() usage.

## Objectives

1. Inject malicious XSLT to read and exfiltrate sensitive local files from the server.
2. Perform SSRF to access internal network resources or metadata services on behalf of the server.
3. Maintain stealth by embedding the injection within legitimate XML processing flows.
4. Verify successful injection through output inspection or callback reception.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an application feature that accepts XML input and applies a user-controllable XSLT stylesheet, such as a data export or formatting endpoint. Test for injection by appending XSLT elements to input fields.

Use reconnaissance tools or manual testing to confirm the endpoint (e.g., /transform or /report). No specific command here; observe responses for XSLT processing errors or successful transformations.

**Expected Output**: Confirmation of XSLT usage, such as transformed HTML output or error messages referencing XSLT namespaces.

### Step 2: Craft Malicious XSLT Payload

**Context**: Create the injected XSLT using the document() function to target local files and remote URLs. This step embeds the payload within a legitimate XML structure to bypass basic filters. Reference the standalone code snippet for the core payload.

Embed [[codes/XSLT-Injection-Payload-for-File-Read-and-SSRF]] into your XML request body, adjusting paths as needed for the target environment.

**Expected Output**: A valid XSLT stylesheet that compiles without syntax errors when tested locally (e.g., using xsltproc).

### Step 3: Send Payload and Trigger Injection

**Context**: Deliver the crafted XML with the injected XSLT to the vulnerable endpoint. This executes the document() calls during transformation, including file contents or SSRF requests in the output.

**Command** ([[commands/curl-send-xslt-payload]]):
```bash
curl -X POST http://target.com/transform -H "Content-Type: application/xml" -d @payload.xml
```

> This command sends the XML payload containing the injected XSLT to the target endpoint. Replace http://target.com/transform with the actual URL, and payload.xml with a file containing the full XML (e.g., <fruits><fruit><name>apple</name><description>red</description></fruit></fruits>) wrapped around the stylesheet reference. The server processes it, applying the malicious XSLT and returning transformed output with embedded file/SSRF data.

**Expected Output**: HTTP response with the transformed content, including copied file contents (e.g., user list from /etc/passwd) or SSRF results (e.g., response from internal service) mixed with legitimate data like fruit listings.

### Step 4: Analyze Output and Verify Success

**Context**: Inspect the response for injected content to confirm file read or SSRF. If SSRF targets an attacker server, check logs there for incoming requests.

Save the response to a file and grep for known file markers (e.g., root:x:0:0).

**Command** (basic verification, not linked as new):
```bash
grep -i "root:" response.html
```

> This extracts evidence of successful file inclusion. For SSRF, monitor your listener (e.g., nc -lvp 25) for connections from the target server.

**Expected Output**: Matches indicating file contents or network logs showing SSRF callback.

### Step 5: Iterate and Escalate

**Context**: If partial success, refine paths or functions (e.g., use unparsed-text() for alternatives). Escalate by chaining to further exfiltration or pivots.

Adjust payload based on output and resend using the same command. Test additional targets like /proc/self/environ for process info.

**Expected Output**: Enhanced data leakage or confirmed internal access.
