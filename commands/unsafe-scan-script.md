---
id: cmd-025
data: >-
  #!/bin/bash

  echo "Scanning for unsafe functions..."

  UNSAFE_COUNT=$(grep -r "strcpy\|strcat\|sprintf" lib/ --exclude="*.safe" | wc
  -l)

  if [ $UNSAFE_COUNT -gt 0 ]; then
   echo "ERROR: Found $UNSAFE_COUNT unsafe function calls"
   exit 1
  fi
tags:
  - script
  - scan
type: command
output: Scan results or error if unsafe calls found
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.955Z'
verified: false
validated: true
submitted: true
---
# unsafe-scan-script

## Command

```bash
#!/bin/bash
echo "Scanning for unsafe functions..."
UNSAFE_COUNT=$(grep -r "strcpy\|strcat\|sprintf" lib/ --exclude="*.safe" | wc -l)
if [ $UNSAFE_COUNT -gt 0 ]; then
 echo "ERROR: Found $UNSAFE_COUNT unsafe function calls"
 exit 1
fi
```

## Description

Bash script to count and alert on unsafe string functions in lib/.

## Parameters

None

## Examples

### Basic Usage

```bash
chmod +x scan.sh; ./scan.sh
```

## Expected Output

Scanning... ERROR: Found X calls

## Related

- [[procedures/Static-Analysis-of-Unsafe-strcpy-Calls-in-cURL]]
