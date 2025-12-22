---
id: 38d65acf-8234-4ffc-b4bd-6ee6dcd11626
name: Extract-XSLT-Processor-Vendor-and-Version-via-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.460340+00:00'
updated_at: '2023-04-10T20:24:48.976986+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - xslt-injection
  - vendor-enumeration
  - version-detection
  - web-exploit
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Extract-XSLT-Processor-Vendor-and-Version-via-Injection

## Summary

This procedure demonstrates how to exploit an XSLT injection vulnerability to extract the vendor, version, and vendor URL of the underlying XSLT processor. By injecting specially crafted XSLT payloads into user-controlled input fields processed by the application, an attacker can query system properties to gather this information, which is useful for identifying potential vulnerabilities specific to the processor in use.

## Description

XSLT Injection occurs when an application unsafely processes user input as part of an XSLT stylesheet transformation, allowing attackers to inject malicious XSLT code. This can lead to information disclosure, such as system properties of the XSLT processor (e.g., Saxon, Xalan, or libxslt), without requiring direct code execution. The technique relies on the XSLT `system-property()` function, which is supported by most processors and returns details like 'xsl:vendor', 'xsl:version', and 'xsl:vendor-url'. This information enables tailoring further attacks, such as exploiting known CVEs in specific processor versions. The target environment is typically a web application that dynamically applies XSLT transformations to XML data from user input, such as search fields, URL parameters, or form submissions. Expected outcomes include successful extraction of processor details, confirming the injection point, and no server-side errors that might alert defenders.

## Requirements

1. Valid access to the vulnerable web application with an identified XSLT injection point (e.g., a parameter that influences XSLT processing).
2. Knowledge of the input format expected by the application (e.g., XML structure or stylesheet parameters).
3. A tool for sending HTTP requests, such as a browser, curl, or Burp Suite, to test and deliver the payloads.
4. Basic understanding of XML and XSLT syntax to craft and adjust payloads.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to strip or escape XSLT-specific elements (e.g., `<xsl:stylesheet>`, `system-property()`) from user inputs.
- Use parameterized XSLT transformations where user input is limited to data nodes, not stylesheet logic.
- Apply web application firewalls (WAFs) with rules to detect anomalous XSLT patterns or `system-property()` calls.
- Regularly update and patch the XSLT processor library to mitigate known information disclosure issues.
- Enable logging of XSLT transformation errors and monitor for unusual queries to system properties.

## Objectives

1. Identify and confirm an XSLT injection vulnerability in the target application.
2. Extract the vendor, version, and vendor URL of the XSLT processor to inform further exploitation.
3. Assess potential for escalating the injection to more severe impacts, such as arbitrary code execution if the processor supports extensions.

## Instructions

### Step 1: Identify the Injection Point and Test Basic Payload

**Context**: Locate a user input field (e.g., a search parameter or XML upload) that the application processes via XSLT transformation. Test for injection by injecting a simple XSLT element to observe if it alters the output, confirming the vulnerability without disclosing sensitive info yet.

Inject a basic test payload like `<xsl:comment>Test Injection</xsl:comment>` into the input and observe if it appears in the response or causes a transformation error.

> If the comment appears or the output changes unexpectedly, the point is vulnerable. Proceed to extraction payloads.

### Step 2: Inject Vendor Extraction Payload

**Context**: Use a targeted XSLT stylesheet to query the 'xsl:vendor' system property. This step focuses on extracting the processor vendor (e.g., 'Apache Software Foundation' for Xalan) to narrow down the target software.

Deliver the payload via the identified injection point, ensuring the input XML matches the expected structure (e.g., root element 'fruits' as in the example). Reference the payload code:

**Code** ([[codes/XSLT-Vendor-Extraction-Payload]]):

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/fruits">
    <xsl:value-of select="system-property('xsl:vendor')"/>
  </xsl:template>
</xsl:stylesheet>
```

> Submit this as the stylesheet or embedded in the input XML. The transformation will output the vendor string directly if successful. Adjust the 'match' attribute if the application's XML root differs from '/fruits'.

### Step 3: Inject Full Processor Information Payload

**Context**: Extend the extraction to retrieve version and vendor URL for complete fingerprinting. This provides actionable intel, such as checking for CVEs in the specific version (e.g., libxslt 1.1.32 vulnerabilities).

Inject the comprehensive payload into the same point, ensuring the response renders the HTML output correctly.

**Code** ([[codes/XSLT-Processor-Info-Extraction-Payload]]):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<body>
<br />Version: <xsl:value-of select="system-property('xsl:version')" />
<br />Vendor: <xsl:value-of select="system-property('xsl:vendor')" />
<br />Vendor URL: <xsl:value-of select="system-property('xsl:vendor-url')" />
</body>
</html>
```

> The response should display lines like 'Version: 1.0', 'Vendor: Saxonica', and 'Vendor URL: http://saxon.sf.net/'. If the output is malformed, verify the namespace declarations match the processor's expectations.

### Step 4: Verify and Document Results

**Context**: Confirm the extracted information is accurate and not filtered. Cross-reference with known processor signatures to validate.

Compare the output against public lists of XSLT processors. If discrepancies occur (e.g., empty output), the processor may restrict system-property access—test alternative functions or injection points.

> Success is indicated by consistent, non-generic output (e.g., not 'Unknown'). Use this data to search for version-specific exploits.
