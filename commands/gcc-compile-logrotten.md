---
data: cd /tmp/logrotten && gcc -o logrotten logrotten.c
tags:
  - compile
  - c-code
type: command
output: (no output if successful)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.980Z'
id: 19e538a3-420b-49d0-8124-137cdf11d744
verified: false
validated: true
submitted: true
---
# gcc-compile-logrotten

## Command

```bash
cd /tmp/logrotten && gcc -o logrotten logrotten.c
```

## Description

Changes to the logrotten directory and compiles the C source into an executable binary.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| cd /tmp/logrotten | Change directory | Yes |
| -o logrotten | Output executable name | Yes |
| logrotten.c | Source file | Yes |

## Examples

### Basic Usage

```bash
cd /tmp/logrotten && gcc -o logrotten logrotten.c
```

### Advanced Usage

```bash
cd /tmp/logrotten && gcc -Wall -o logrotten logrotten.c
```

## Expected Output

No output on success; errors if compilation fails.

## Related

- [[commands/git-clone-logrotten]]
- [[procedures/Compile-and-Execute-Logrotten-Exploit]]
