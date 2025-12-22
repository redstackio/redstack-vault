---
type: command
executor: bash
data: cat $_INPUT_FILE | ./Aquatone/aquatone -ports large -out $_OUTPUT_DIR
tags:
  - scanning
  - web-discovery
platforms:
  - Linux
verified: true
validated: true
---

# aquatone-scan-subdomains-from-file

## Command

```bash
cat $_INPUT_FILE | ./Aquatone/aquatone -ports large -out $_OUTPUT_DIR
```

## Description

This command pipes a list of subdomains from a file to Aquatone for active scanning, targeting a large set of ports to detect HTTP/HTTPS services and generate visual reports with screenshots.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the file containing subdomains, one per line (e.g., /tmp/subresult.txt) | Yes |
| $_OUTPUT_DIR | Directory for HTML output reports (e.g., /tmp/aquatone_results) | Yes |
| -ports large | Scan a large set of common ports (e.g., 80, 443, 8080, etc.) | Built-in |

## Examples

### Basic Usage

```bash
cat /tmp/subdomains.txt | ./Aquatone/aquatone -ports large -out /tmp/report
```

### Advanced Usage

```bash
cat /tmp/subdomains.txt | ./Aquatone/aquatone -ports large -out /tmp/report --headless
```

## Expected Output

Creates an HTML report in $_OUTPUT_DIR with index.html showing a dashboard of scanned hosts, including URLs, screenshots, HTTP status, and technology details. Console may show progress like "[INFO] Scanning 10 URLs".

## Related

- [[procedures/Subdomain-Enumeration-and-Scan-with-Aquatone]]
- [[tools/Aquatone]]
