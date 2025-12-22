---
type: command
executor: bash
data: findomain -t $_TARGET_DOMAIN -o $_OUTPUT_FILE
tags:
  - reconnaissance
  - dns
  - enumeration
platforms:
  - Linux
verified: true
validated: true
---

# findomain-target-domain-scan

## Command

```bash
findomain -t $_TARGET_DOMAIN -o $_OUTPUT_FILE
```

## Description

This command uses Finddomain to enumerate subdomains for a given target domain by querying passive sources such as certificate transparency logs, search engines, and threat intelligence feeds. It outputs the results to a specified file, making it ideal for stealthy reconnaissance without direct DNS queries to the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t $_TARGET_DOMAIN | The target domain to enumerate (e.g., owasp.org) | Yes |
| -o $_OUTPUT_FILE | Output file path to save the list of subdomains (e.g., subdomains.txt) | Yes |
| --help | Display help message (alternative to full scan) | No |

## Examples

### Basic Usage

```bash
findomain -t owasp.org -o owasp_subdomains.txt
```

### Advanced Usage

```bash
findomain -t owasp.org -o owasp_subdomains.txt --format csv
```

This adds CSV formatting for easier parsing in tools like Excel.

## Expected Output

The command produces a plain text file with one subdomain per line, such as:

```
www.owasp.org
mail.owasp.org
api.owasp.org
...
```

No console output during execution unless errors occur; check the output file for results. Successful runs end with a message like "Subdomains saved to [file]".

## Related

- [[procedures/Basic-DNS-Enumeration-with-Finddomain]]
- [[tools/Finddomain]]
