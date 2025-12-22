---
type: code
language: xml
verified: true
platforms:
  - web
tags:
  - xxe
  - xml
  - entity
validated: true
---

# xml-internal-entity-definition

## Code

```xml
<!ENTITY entity_name "entity_value">
```

## Description

Defines an internal XML entity within a DOCTYPE declaration. This replaces &entity_name; references with "entity_value" during parsing, useful for testing basic entity expansion before escalating to external entities in XXE attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| entity_name | The name of the entity to reference (e.g., test) | test |
| entity_value | The literal string value to substitute | sensitive_data |

## Usage

Insert into an XML document's DOCTYPE, e.g., <!DOCTYPE root [<!ENTITY test "hello">]><root>&test;</root>. Submit to the target endpoint to verify if entities are processed. In XXE context, use as a non-malicious test before external file reads.

## Detection

- XML parser logs showing entity expansion.
- Response body containing substituted values instead of raw entities.
- WAF rules blocking DTD declarations.

## Related

- [[procedures/Perform-XML-External-Entity-XXE-Attack]]
- [[codes/xml-external-entity-definition]]
