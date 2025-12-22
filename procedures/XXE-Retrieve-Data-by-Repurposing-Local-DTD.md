---
id: cf5a2f9e-7234-4917-8265-2480962698dd
name: XXE-Retrieve-Data-by-Repurposing-Local-DTD
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T19:13:50.343273+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - owasp
  - owasp top 10
  - Web Applications
  - xxe
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# XXE-Retrieve-Data-by-Repurposing-Local-DTD

## Summary

This procedure exploits an XML External Entity (XXE) vulnerability in a web application by repurposing a local Document Type Definition (DTD) file to trigger an error message that discloses sensitive server-side files, such as /etc/passwd. It involves modifying an intercepted XML request to define parameter entities that import and redefine elements from an existing local DTD, causing the application to include file contents in the error output.

## Description

XXE vulnerabilities allow attackers to define external entities in XML documents that the parser processes, potentially leading to file disclosure, SSRF, or denial of service. In this technique, the attacker targets a web application that processes XML for operations like stock checks (e.g., in a product catalog system). By intercepting the request with a proxy tool like Burp Suite, the attacker inserts a custom DOCTYPE declaration that references a known local DTD file on the server (e.g., /usr/share/yelp/dtd/docbookx.dtd in a Yelp-related application). This DTD is then manipulated by redefining a parameter entity (ISOamso) to include a reference to a target file like /etc/passwd. When the parser evaluates the entity, it attempts to load a nonexistent file, generating an error that embeds the contents of the target file. This method is effective against applications that do not disable external entity processing and have accessible local DTDs. It requires knowledge of the server's file system and potential DTD locations, often discovered through reconnaissance or common paths.

## Requirements

1. Access to a web application endpoint that accepts and parses XML input (e.g., a stock check or API endpoint).
2. A proxy tool like [[tools/Burp-Suite]] to intercept and modify HTTP requests.
3. Knowledge of a local DTD file path on the target server (e.g., /usr/share/yelp/dtd/docbookx.dtd; may require prior enumeration).
4. Target file path for disclosure (e.g., /etc/passwd on Linux servers).
5. The application must process external parameter entities and not sanitize XML input.

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set 'disallow-doctype-decl' to true in libxml2).
- Use JSON or other non-XML formats for API inputs where possible.
- Implement web application firewalls (WAFs) to block XXE payloads, such as those containing <!DOCTYPE or %entity definitions.
- Monitor server logs for XML parsing errors and anomalous file access attempts.
- Validate and sanitize all XML inputs, rejecting any with DOCTYPE declarations.
- Run applications in containers with restricted file system access to limit disclosure impact.

## Objectives

1. Intercept and modify an XML-based request to inject a malicious DOCTYPE.
2. Repurpose a local DTD to reference and disclose sensitive files via entity expansion.
3. Extract server-side file contents from the resulting error message.
4. Confirm successful data exfiltration without alerting the application.

## Instructions

### Step 1: Intercept the Original XML Request

**Context**: Identify and capture the legitimate XML request sent by the application to understand its structure and ensure the modification targets the correct endpoint. This step establishes a baseline for injecting the XXE payload without breaking the request format.

Navigate to the vulnerable endpoint (e.g., a product page with a 'check stock' feature) in your browser. Trigger the action that sends the XML request, such as clicking 'check stock'. Use [[tools/Burp-Suite]] to intercept the HTTP POST request containing the XML body.

**Expected Output**: The intercepted request shows a clean XML structure, such as:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
  <productId>123</productId>
</stockCheck>
```

### Step 2: Inject the Malicious DOCTYPE Declaration

**Context**: Modify the XML to include a DOCTYPE that defines parameter entities. This imports the local DTD and redefines an entity to embed the target file contents into an error-triggering construct. The payload must be inserted precisely between the XML declaration and the root element to avoid parsing errors.

In the Burp Suite Repeater or Proxy, edit the request body. Insert the following DOCTYPE declaration immediately after the <?xml ...?> line and before the <stockCheck> element. Use the [[codes/XXE-Entity-Definition-for-Local-DTD-Repurposing]] code snippet, substituting the local DTD path and target file as needed.

```xml
<!DOCTYPE message [
  <!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
  <!ENTITY % ISOamso ' 
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % eval "<!ENTITY % error SYSTEM 'file:///nonexistent/%file;'>">
  %eval;
  %error;
  '>
  %local_dtd;
]>
```

Forward the modified request to the server.

**Expected Output**: The server processes the XML, imports the DTD, and attempts to resolve the entities, leading to an error response.

### Step 3: Analyze the Error Response for Disclosed Data

**Context**: The redefined entity causes the parser to include the target file's contents in an error message when trying to load a nonexistent path. This step verifies the exfiltration by inspecting the response for the embedded data.

Review the server's HTTP response in Burp Suite. Look for error messages in the body that include the contents of the target file (e.g., lines from /etc/passwd).

If the error does not appear, adjust the nonexistent path (e.g., file:///nonexistent/%file;) or try alternative local DTD paths. Repeat the request if necessary.

**Expected Output**: An XML or HTML error response containing fragments like:

```xml
<error>Entity 'error' not defined: file:///nonexistent/root:x:0:0:root:/root:/bin/bash ... (full /etc/passwd contents embedded)</error>
```

**Success Indicators**:
- Error message includes readable contents of the target file (e.g., user entries from /etc/passwd).
- No authentication or parsing errors prevent entity resolution.
- Response size increases due to embedded file data.
