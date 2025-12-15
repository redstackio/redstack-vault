---
data: >-
  shodan search 'ssl.cert.subject.cn:*.mil country:"US" http.status:200
  product:"Docker Registry HTTP API"' --fields ip_str,port,hostnames
tags:
  - recon
  - shodan
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.924Z'
id: e0604c11-18f0-4335-b83c-557e191e57a4
verified: false
validated: true
submitted: true
---
# shodan-search-docker

## Command

```bash
shodan search 'ssl.cert.subject.cn:*.mil country:"US" http.status:200 product:"Docker Registry HTTP API"' --fields ip_str,port,hostnames
```

## Description

Searches Shodan for exposed Docker Registry APIs on US .mil domains, returning IP, port, and hostname details for vulnerable instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| search query | Dork string targeting Docker on .mil | Yes |
| --fields | Specifies output fields (ip_str,port,hostnames) | No |

## Examples

### Basic Usage

```bash
shodan search 'product:"Docker Registry HTTP API"' --fields ip_str
```

### Advanced Usage

```bash
shodan search 'ssl.cert.subject.cn:*.mil country:"US"' --limit 10 --fields ip_str,port
```

## Expected Output

JSON or tabular list of matching devices, e.g., IP: 192.0.2.1, Port: 443, Hostnames: example.mil.

## Related

- [[Related Procedure: Discover-Exposed-Docker-Registry-with-Shodan]]
