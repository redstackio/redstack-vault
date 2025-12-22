---
type: code
language: bash
verified: true
created_at: '2020-02-21T05:40:35.379348+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - setup
  - snmp
  - configuration
validated: true
---

# Install-SNMP-MIBs-Downloader-and-Configure

## Code

```bash
apt update && apt install snmp-mibs-downloader -y \
&& sed -i '/mibs/s/^/#/g' /etc/snmp/snmp.conf
```

## Description

This bash script updates the package list, installs the snmp-mibs-downloader package to fetch standard Management Information Base (MIB) files, and modifies the SNMP configuration file to enable loading of all MIBs. It improves the readability of SNMP tool outputs by translating numeric Object Identifiers (OIDs) into descriptive names, making enumeration results more interpretable without manual lookup.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a self-contained setup script with no user-defined variables. | N/A |

## Usage

Run this script on a Debian-based Linux system (e.g., Kali, Ubuntu) prior to SNMP enumeration procedures like snmpwalk or snmp-check. It is particularly useful in red team environments where detailed SNMP output analysis is needed. Execute as root or with sudo. After running, tools like snmpwalk will display names like 'sysDescr' instead of raw OIDs like '1.3.6.1.2.1.1.1.0'.

## Detection

- Package manager logs showing 'snmp-mibs-downloader' installation.
- Modifications to /etc/snmp/snmp.conf (grep for commented 'mibs :' line).
- Benign activity, but unusual in production environments; monitor apt logs for unauthorized setups.

## Related

- [[procedures/Enumerate-Authenticated-SNMP-Server]]
