---
id: cmd-uuid-004
data: |-
  cat > apache_dos_poc.sh << 'EOF'
  #!/bin/bash
  ...[full script as above]
  EOF
  chmod +x apache_dos_poc.sh
tags:
  - scripting
  - dos
type: command
output: Script created and executable.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.971Z'
verified: false
validated: true
submitted: true
---
# create-apache-dos-script

## Command

```bash
cat > apache_dos_poc.sh << 'EOF'
#!/bin/bash
TARGET="$1"
PORT=${2:-80}
...[script body]
EOF
chmod +x apache_dos_poc.sh
```

## Description

Creates the bash PoC script for automated DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| > apache_dos_poc.sh | Output file | Yes |
| chmod +x | Make executable | Yes |

## Examples

### Basic Usage

```bash
cat > script.sh << EOF
#!/bin/bash
echo hello
EOF
chmod +x script.sh
```

## Expected Output

File created successfully.

## Related

- [[Related Procedure]]
