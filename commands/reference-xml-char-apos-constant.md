---
id: 68d975cb-061e-450a-a027-2b502a8568ec
name: reference-xml-char-apos-constant
type: command
executor: bash
data: org.apache.batik.util.XMLConstants.XML_CHAR_APOS
output: null
created_at: '2023-04-06T03:56:33.438122+00:00'
updated_at: '2023-04-10T20:22:27.355781+00:00'
platforms:
  - Java
tags:
  - hql-injection
  - java-constants
verified: true
validated: true
---

# reference-xml-char-apos-constant

## Command

```bash
org.apache.batik.util.XMLConstants.XML_CHAR_APOS
```

## Description

This command references the XML_CHAR_APOS constant from the Apache Batik library, which defines a single apostrophe (') character. Use it during reconnaissance to identify quote representations in Java libraries for constructing HQL injection payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Direct constant path reference; no parameters needed | No |

## Examples

### Basic Usage

```bash
org.apache.batik.util.XMLConstants.XML_CHAR_APOS
```

### In Context (e.g., in a script or decompiler output)

```bash
echo "Potential quote constant: org.apache.batik.util.XMLConstants.XML_CHAR_APOS"
```

## Expected Output

The constant path itself, or in a Java context, it resolves to the character ' (apostrophe). When incorporated into code, it allows safe quote usage without literals.

## Related

- [[procedures/Exploit-HQL-Injection-via-Java-Constants]]
- [[commands/reference-single-quote-constant]]
