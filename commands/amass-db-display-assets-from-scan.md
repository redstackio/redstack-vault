---
type: command
executor: bash
data: amass db -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -enum $_SCAN_NUMBER -show
output: "root@kali ~# amass db -dir owasp.org/ -d owasp.org -enum 2 -show\nlists.owasp.org\nocms.owasp.org\nowasp.org\nwiki.owasp.org\ndev.owasp.org\ngapps.owasp.org\nvideos.owasp.org\naustin.owasp.org\nwww2.owasp.org\ncontact.owasp.org\nname-virt-host.owasp.org\nwww.owasp.org\ncheatsheetseries.owasp.org\ngroups.owasp.org\ncalendar.owasp.org\nsl.owasp.org\nmail.owasp.org\nkerala.owasp.org\n\nOWASP Amass v3.7.2                                https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n18 names discovered - cert: 10, api: 8\n--------------------------------------------------------------------------------\nASN: 13335 - CLOUDFLARENET, US\n\t2606:4700:10::/44 \t54   Subdomain Name(s)\n\t172.67.0.0/20     \t18   Subdomain Name(s)\n\t104.22.16.0/20    \t36   Subdomain Name(s)\n"
tags:
  - reconnaissance
  - dns
  - amass
platforms:
  - Linux
verified: true
validated: true
---

# amass-db-display-assets-from-scan

## Command

```bash
amass db -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -enum $_SCAN_NUMBER -show
```

## Description

This command displays the assets (subdomains, IPs, ASNs) discovered in a specific Amass enumeration scan from the database. It requires the scan's enumeration number from a prior list command and filters by target domain for precise retrieval.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OUTPUT_DIRECTORY | Path to the directory containing Amass .db files | Yes |
| $_TARGET_DOMAIN | The domain to filter assets for (e.g., owasp.org) | Yes |
| $_SCAN_NUMBER | The enumeration ID of the scan (e.g., 2 from -list output) | Yes |
| -show | Flag to display the assets from the specified enum | Yes (built-in) |

## Examples

### Basic Usage

```bash
amass db -dir /home/user/output/ -d owasp.org -enum 2 -show
```

### Advanced Usage

For scripting, combine with grep to filter subdomains:

```bash
amass db -dir ./output/ -d example.com -enum 1 -show | grep -E '^[^\s]+\.'
```

## Expected Output

A list of discovered names followed by a summary of sources and network details. For example:

```
root@kali ~# amass db -dir owasp.org/ -d owasp.org -enum 2 -show
lists.owasp.org
ocms.owasp.org
owasp.org
wiki.owasp.org
dev.owasp.org
gapps.owasp.org
videos.owasp.org
austin.owasp.org
www2.owasp.org
contact.owasp.org
name-virt-host.owasp.org
www.owasp.org
cheatsheetseries.owasp.org
groups.owasp.org
calendar.owasp.org
sl.owasp.org
mail.owasp.org
kerala.owasp.org

OWASP Amass v3.7.2                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
18 names discovered - cert: 10, api: 8
--------------------------------------------------------------------------------
ASN: 13335 - CLOUDFLARENET, US
	2606:4700:10::/44 	54   Subdomain Name(s)
	172.67.0.0/20     	18   Subdomain Name(s)
	104.22.16.0/20    	36   Subdomain Name(s)

```

Success is shown by listed assets and summary stats; errors occur if the enum ID or domain is invalid.

## Related

- [[procedures/Query-Amass-Database-for-Previous-Scans-and-Assets]]
- [[commands/amass-db-list-previous-scans]]
