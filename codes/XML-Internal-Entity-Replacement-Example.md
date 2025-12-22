---
id: e1cb116d-9108-4d0d-8746-97cde1260237
name: XML-Internal-Entity-Replacement-Example
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.075549+00:00'
updated_at: '2023-04-10T20:24:39.989657+00:00'
platforms:
  - Web
tags:
  - xml
  - entity
  - example
validated: true
---

# XML-Internal-Entity-Replacement-Example

## Code

```xml
<?xml version="1.0"?>
<!DOCTYPE replace [<!ENTITY example "Doe"> ]>
 <userInfo>
  <firstName>John</firstName>
  <lastName>&example;</lastName>
 </userInfo>
```

## Description

This XML snippet demonstrates internal entity declaration and replacement, where an entity 'example' is defined with value 'Doe' and referenced in the <lastName> element. When parsed, '&example;' expands to 'Doe'. This illustrates basic entity usage, which can be extended to XXE by making entities external (SYSTEM keyword).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| example | Internal entity name | example |
| Doe | Replacement value for the entity | Doe |

## Usage

Embed this in HTTP requests to XML endpoints for testing entity processing. Modify to external entities for XXE payloads, e.g., <!ENTITY example SYSTEM "file:///etc/passwd">. Useful in procedures like [[procedures/Detect-and-Mitigate-XXE-Injection]] for baseline XML validation.

## Detection

- XML parsers logging entity expansions.
- WAF rules blocking <!DOCTYPE> or <!ENTITY> patterns.
- Response analysis for unexpected entity values in output.

## Related

- [[procedures/Detect-and-Mitigate-XXE-Injection]]
