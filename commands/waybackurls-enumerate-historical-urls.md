---
type: command
executor: bash
data: cat subdomains.txt | waybackurls > historical-urls.txt
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - url-enumeration
verified: true
validated: true
---

# waybackurls-enumerate-historical-urls

## Command

```bash
cat subdomains.txt | waybackurls > historical-urls.txt
```

## Description

This command pipes a list of subdomains from a file into the waybackurls tool, which queries the Internet Archive's Wayback Machine to retrieve all known historical URLs for those domains. The results are saved to an output file. It is used during passive reconnaissance to discover archived web paths without interacting with the live target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| subdomains.txt | Input file containing one subdomain per line (e.g., app.target.com) | Yes |
| historical-urls.txt | Output file to store the fetched URLs | Yes |
| waybackurls | The waybackurls binary (assumes it's in PATH) | Yes |

## Examples

### Basic Usage

```bash
cat subdomains.txt | waybackurls > historical-urls.txt
```

### Advanced Usage

For a single domain without a file:
```bash
echo "target.com" | waybackurls > urls.txt
```

Or append to existing output:
```bash
cat subdomains.txt | waybackurls >> all-urls.txt
```

## Expected Output

The command produces no stdout by default (redirected to file). The output file contains one URL per line, such as:
```
https://www.target.com/index.html
https://app.target.com/api/v1
http://target.com/old/login
```

If the input is empty, the output file will be empty. Errors (e.g., network issues) may print to stderr, like "fetching CDX failed".

## Related

- [[procedures/Enumerate-Historical-URLs-via-Wayback-Machine]]
- [[tools/waybackurls]]
