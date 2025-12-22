---
type: command
executor: bash
data: python MMG.py configs/generic-cmd.json malicious.vba
output: null
created_at: '2023-04-06T03:56:23Z'
updated_at: '2023-04-10T20:36:49Z'
platforms:
  - Linux
tags:
  - generation
  - vba
verified: true
validated: true
---

# generate-vba-macro-with-mmg

## Command

```bash
python MMG.py configs/generic-cmd.json malicious.vba
```

## Description

Runs the Malicious Macro Generator to produce an obfuscated VBA macro file based on the provided JSON config, for embedding in Office documents to download and execute payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| configs/generic-cmd.json | Path to the JSON configuration file | Yes |
| malicious.vba | Output VBA file name | Yes |

## Examples

### Basic Usage

```bash
python MMG.py configs/generic-cmd.json malicious.vba
```

### With Custom Config and Output

```bash
python MMG.py configs/custom.json payload-macro.vba
```

## Expected Output

Processing config... Generating VBA... Output saved to malicious.vba. The file contains encoded VBA code for payload execution.

## Related

- [[procedures/Generate-Malicious-VBA-Macro-for-Payload-Download-and-Execution-Using-MMG]]
- [[tools/MaliciousMacroGenerator]]
