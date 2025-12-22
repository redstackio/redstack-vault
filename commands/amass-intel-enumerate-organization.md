---
type: command
executor: bash
data: amass intel -org $_COMPANY_NAME
tags:
  - reconnaissance
  - asn
  - osint
platforms:
  - Linux
verified: true
validated: true
---

# amass-intel-enumerate-organization

## Command

```bash
amass intel -org $_COMPANY_NAME
```

## Description

This command uses Amass's intel module to enumerate Autonomous System Numbers (ASNs) associated with a specified organization by querying passive data sources like WHOIS databases. It is used during reconnaissance to identify network infrastructure linked to a company.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -org | Specifies the organization name to search for ASNs | Yes |
| $_COMPANY_NAME | The exact or partial company name (e.g., "Google") | Yes |

## Examples

### Basic Usage

```bash
amass intel -org Google
```

### Advanced Usage

```bash
amass intel -org "Google LLC" > output.txt
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali ~# amass intel -org google
6432, GOOGLE-FIBER - Google Fiber Inc.
15169, GOOGLE - Google LLC
16550, GOOGLE-PRIVATE-CLOUD - Google LLC
16591, GOOGLE-FIBER - Google Fiber Inc.
19448, GOOGLE-FIBER - Google Fiber Inc.
19527, GOOGLE-2 - Google LLC
22577, ADMOB-US - Google LLC
22859, GOOGLE - Google LLC
24424, CNNIC-GOOGLECN-AP Beijing Gu Xiang Information Technology Co.
26684, AS-MEEBO - Google LLC
26910, LINKUS - Google Access LLC
36039, GOOGLE - Google LLC
36040, YOUTUBE - Google LLC
36384, GOOGLE-IT - Google LLC
36385, GOOGLE-IT - Google LLC
36492, GOOGLEWIFI - Google
36987, google-as
40873, AS-METAWEB-2 - Google LLC
41264, GOOGLE-IT-RO-ISP
45566, GOOGLE-CORP-APAC-AS-AP AS number for Google Corporate Network in APAC
394507, GOOGLE - Google LLC
394639, GOOGLE - Google LLC
394699, GOOGLE-ACCESS-NYC - Google Access LLC
395973, GOOGLE-2 - Google LLC
396982, GOOGLE-PRIVATE-CLOUD - Google LLC
```

## Related

- [[procedures/Find-Company-ASN-Using-Amass]]
- [[tools/amass]]
