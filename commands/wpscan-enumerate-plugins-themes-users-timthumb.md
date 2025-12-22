---
type: command
executor: bash
data: 'wpscan --url http://$_TARGET_URL --enumerate p,t,u,tt'
output: |-
  root@kali:~# wpscan --url http://10.10.10.10 --enumerate p,t,u,tt
  [+] URL: http://10.10.10.10/
  [+] Started: Mon Oct  2 12:34:56 2023
  [+] Detection: WordPress 5.8.1
  [+] Interesting Finding(s):
  [+] Config Backup Files:
   | Location: http://10.10.10.10/wp-config.bak
   | Confidence: 100
  [+] Users:
   | admin (ID: 1)
   | Username: admin
   | Name: Admin User
   | Description: Just another WordPress site
  [+] Plugins:
   | Name: vulnerable-plugin
   | Version: 1.0
   | Status: Vulnerable (latest known: 2.0)
  [+] Themes:
   | Name: twentytwentyone
   | Version: 1.4
   | Status: Active
  [+] TimThumb files:
   | Location: http://10.10.10.10/wp-content/plugins/timthumb.php
   | Confidence: 80
  [+] Finished: Mon Oct  2 12:35:10 2023
  [+] Scan took 14 seconds
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
tags:
  - wordpress
  - enum
  - vulnerability-scanning
verified: true
validated: true
---

# wpscan-enumerate-plugins-themes-users-timthumb

## Command

```bash
wpscan --url http://$_TARGET_URL --enumerate p,t,u,tt
```

## Description

This command performs comprehensive enumeration of a WordPress site's users (u), plugins (p), themes (t), and TimThumb files (tt). It identifies installed components, their versions, and potential vulnerabilities by querying WordPress endpoints and comparing against known databases. Use this during reconnaissance to map the site's attack surface.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | The full URL of the target WordPress site (e.g., http://example.com) | Yes |
| `--enumerate p,t,u,tt` | Enumeration options: p=plugins, t=themes, u=users, tt=TimThumb files | Yes |
| `$_TARGET_URL` | Placeholder for the target site's URL or IP (substitute with actual value) | Yes |
| `--api-token` (optional) | WPScan API token for enhanced vulnerability details | No |
| `-v` (optional) | Verbose output for more details | No |

## Examples

### Basic Usage

Enumerate core components on a target site:

```bash
wpscan --url http://10.10.10.10 --enumerate p,t,u,tt
```

### Advanced Usage

Include API token and verbosity for full vuln reporting:

```bash
wpscan --url https://target.com --enumerate p,t,u,tt --api-token YOUR_TOKEN -v
```

## Expected Output

The command outputs detection of WordPress version, interesting findings (e.g., backup files), lists of users with IDs and details, plugins/themes with versions and vulnerability status, and TimThumb locations. Success is indicated by populated sections like [+] Users: or [+] Plugins: with specific data. Errors may show if the site is not WordPress or access is blocked.

## Related

- [[procedures/enumerate-web-application-components]]
- [[tools/Nmap]]
