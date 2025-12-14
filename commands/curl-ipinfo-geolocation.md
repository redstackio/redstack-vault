---
id: cmd-curl-ipinfo
data: curl ipinfo.io/IP-address-of-victim
tags:
  - recon
  - geolocation
type: command
output: 'JSON with geolocation data such as city, region, country, and coordinates'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.812Z'
verified: false
validated: true
submitted: true
---
# curl-ipinfo-geolocation

## Command

```bash
curl ipinfo.io/IP-address-of-victim
```

## Description

This command queries the ipinfo.io API to retrieve geolocation and network details for a given IP address, useful in post-exploitation reconnaissance after capturing IPs via SSRF or similar attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IP-address-of-victim | The target IP address to query (e.g., 192.0.2.1) | Yes |

## Examples

### Basic Usage

```bash
curl ipinfo.io/8.8.8.8
```

### Advanced Usage

```bash
curl -s ipinfo.io/8.8.8.8 | jq '.city'
```

(Requires jq for parsing; outputs just the city.)

## Expected Output

JSON response including ip, hostname, city, region, country, loc (latitude,longitude), org, and postal code. Example:

```json
{
  "ip": "8.8.8.8",
  "city": "Mountain View",
  "region": "California",
  "country": "US",
  "loc": "37.4056,-122.0775",
  "org": "AS15169 Google LLC"
}
```

## Related

- [[Related Procedure: Analyze Captured Data and Trace Victim Geolocation]]
