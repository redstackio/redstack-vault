---
id: 0c85dcf4-87a3-4783-ba0b-38ffb6756ac1
name: curl-azure-imds-public-ip-address
type: command
executor: bash
data: >-
  curl
  "http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text"
  -H "Metadata: true"
output: null
created_at: '2023-04-06T03:56:38.548449+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
  - Linux
tags:
  - ssrf
  - metadata
  - network
verified: true
validated: true
---

# curl-azure-imds-public-ip-address

## Command

```bash
curl -H $_METADATA_HEADER "http://$_IMDS_HOST/metadata/instance/network/interface/$_INTERFACE_INDEX/ipv4/ipAddress/$_IP_INDEX/publicIpAddress?api-version=$_API_VERSION&format=$_FORMAT"
```

## Description

Retrieves the public IP address of the Azure VM's primary network interface from IMDS. Useful in SSRF scenarios to identify the VM's external exposure for further attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_METADATA_HEADER | IMDS authentication header | Yes |
| $_IMDS_HOST | Metadata service host | Yes |
| $_INTERFACE_INDEX | Network interface index (e.g., 0) | Yes |
| $_IP_INDEX | IP address index (e.g., 0) | Yes |
| $_API_VERSION | API version (e.g., 2017-04-02) | Yes |
| $_FORMAT | Output format (e.g., 'text' for plain IP) | No |

## Examples

### Basic Usage

```bash
curl -H 'Metadata: true' "http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text"
```

### JSON Format

```bash
curl -H 'Metadata: true' "http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02"
```

## Expected Output

Plain text IP or JSON:
```
20.123.45.67
```
Or
```
{"publicIpAddress": {"ipAddress": {"ipv4": {"address": "20.123.45.67"}}}
```

## Related

- [[procedures/Exploit-Azure-SSRF-to-Access-VM-Metadata-Service]]
- [[commands/curl-azure-imds-instance-metadata]]
