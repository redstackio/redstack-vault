---
id: 4e5f3876-c347-44ec-a363-51895fc89d49
name: obfuscate-vba-code-with-docker
type: command
executor: bash
data: cat $_VBA_FILE | docker run -i --rm bonnetn/vba-obfuscator /dev/stdin
output: null
created_at: '2023-04-06T03:56:23.756736+00:00'
updated_at: '2023-04-10T20:36:59.136282+00:00'
platforms:
  - Linux
  - macOS
tags:
  - docker
  - obfuscation
  - vba
verified: true
validated: true
---

# obfuscate-vba-code-with-docker

## Command

```bash
cat $_VBA_FILE | docker run -i --rm bonnetn/vba-obfuscator /dev/stdin
```

## Description

This command pipes the contents of a VBA file into the vba-obfuscator Docker image to obfuscate the code. It applies transformations like variable renaming and string obfuscation to evade detection, outputting the result to stdout for redirection to a new file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_VBA_FILE` | Path to the input VBA file (e.g., malicious_macro.vba) | Yes |
| `bonnetn/vba-obfuscator` | Docker image name for the obfuscator | Yes |
| `-i` | Interactive mode for stdin input | Built-in |
| `--rm` | Remove container after run | Built-in |
| `/dev/stdin` | Standard input device in container | Built-in |

## Examples

### Basic Usage

```bash
cat malicious_macro.vba | docker run -i --rm bonnetn/vba-obfuscator /dev/stdin > obfuscated.vba
```

### Advanced Usage

For multiple files, loop or chain:
```bash
for file in *.vba; do cat $file | docker run -i --rm bonnetn/vba-obfuscator /dev/stdin > obfuscated_${file}; done
```

## Expected Output

Obfuscated VBA code printed to stdout, e.g.:
Sub Auto_Open()
Dim a As String: a = Chr(83) & Chr(104) & Chr(101) & Chr(108) & Chr(108)...
End Sub

The output appears garbled with encoded strings and renamed elements but remains syntactically valid VBA.

## Related

- [[procedures/Obfuscate-VBA-Macros-Using-vba-obfuscator]]
