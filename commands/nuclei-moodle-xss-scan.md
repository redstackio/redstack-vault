---
id: cmd-nuclei-xss-2024
data: 'nuclei -u https://target.com -t cves/2022/CVE-2022-35653.yaml -v'
tags:
  - scanning
  - xss
  - nuclei
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.425Z'
verified: false
validated: true
submitted: true
---
# nuclei-moodle-xss-scan

## Command

```bash
nuclei -u https://target.com -t cves/2022/CVE-2022-35653.yaml -v
```

## Description

This command uses Nuclei to scan a Moodle instance for the reflected XSS vulnerability in the LTI module by sending a POST request with a malicious payload and checking for reflections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL (e.g., https://target.com) | Yes |
| `-t` | Path to the CVE-2022-35653 YAML template | Yes |
| `-v` | Verbose output for detailed logging | No |

## Examples

### Basic Usage

```bash
nuclei -u https://target.com -t cves/2022/CVE-2022-35653.yaml
```

### Advanced Usage

```bash
nuclei -u https://target.com -t cves/2022/CVE-2022-35653.yaml -v -o results.txt
```

## Expected Output

If vulnerable, output includes: [CVE-2022-35653] [http] [medium] https://target.com/mod/lti/auth.php with matched indicators like reflected payload and 'moodle-editor'.

## Related

- [[Related Procedure: Scan-for-Moodle-LTI-Reflected-XSS-Using-Nuclei]]
