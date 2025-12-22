---
id: fa919351-5072-405b-89b2-eba3fec0fdc6
name: assets-from-spf-with-asn-to-jq
type: command
executor: bash
data: |
  python assets_from_spf.py $_DOMAIN --asn | jq .
output: null
created_at: '2020-07-24T17:11:28.248165+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
  - asn
verified: true
validated: true
---

# assets-from-spf-with-asn-to-jq

## Command

```bash
python assets_from_spf.py $_DOMAIN --asn | jq .
```

## Description

This command extends the basic SPF scan by including ASN (Autonomous System Number) lookups for discovered IPs and netblocks, then formats the JSON output using jq. It is useful for mapping assets to cloud providers or organizations during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain to query SPF records for (e.g., example.com) | Yes |
| --asn | Enable ASN whois lookups for IPs | Yes (flag) |

## Examples

### Basic Usage

```bash
python assets_from_spf.py owasp.com --asn | jq .
```

### Advanced Usage

Save formatted JSON:

```bash
python assets_from_spf.py owasp.com --asn | jq . > spf_assets_asn.json
```

## Expected Output

JSON-formatted list with ASN details, such as:

```json
{
  "ips": ["192.0.2.1"],
  "asns": [{
    "ip": "192.0.2.1",
    "asn": "AS12345",
    "owner": "Example ISP"
  }],
  "domains": ["partner.example.com"]
}
```

Success is indicated by structured JSON without parsing errors.

## Related

- [[procedures/Find-Domains-and-Netblocks-from-SPF-Records]]
- [[commands/assets-from-spf-basic-scan]]
