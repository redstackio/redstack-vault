---
id: 3b01c009-8fd5-4d63-be1a-5a4bc1c03c68
name: uniscan-scan-for-vulnerabilities
type: command
executor: bash
data: uniscan -u $_TARGET_URL -qweds
output: >-
  ####################################

  # Uniscan project                  #

  # http://uniscan.sourceforge.net/  #

  ####################################

  V. 6.3


  Scan date: [DATE]

  ===================================================================================================

  | Domain: $_TARGET_URL/

  | Server: [SERVER_INFO]

  | IP: [TARGET_IP]

  ===================================================================================================

  | Directory check: [STATUS]

  ===================================================================================================

  | File check: [STATUS]

  ===================================================================================================

  | Check robots.txt: [RESULTS]

  | Check sitemap.xml: [RESULTS]

  ===================================================================================================

  | Crawler Started: [PLUGINS_LOADED]

  | [+] Crawling finished, X URL's found!

  | External hosts: [LIST_OF_HOSTS]

  | Source Code Disclosure: [RESULTS]

  | Timthumb: [RESULTS]

  | File Upload Forms: [RESULTS]

  | FCKeditor File Upload: [RESULTS]

  | E-mails: [LIST_OF_EMAILS]

  | Web Backdoors: [RESULTS]

  | PHPinfo() Disclosure: [+] phpinfo() page: [URL] [CONFIG_DETAILS]
created_at: '2020-08-31T18:28:13.588477+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - LFI
  - RFI
  - RCE
  - scanning
verified: true
validated: true
---

# uniscan-scan-for-vulnerabilities

## Command

```bash
uniscan -u $_TARGET_URL -qweds
```

## Description

This command uses Uniscan to scan a web application at the specified URL for LFI, RFI, and RCE vulnerabilities. It performs crawling, plugin-based checks for disclosures, and tests inclusion vectors. Use during reconnaissance to identify weak points in PHP-based apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_TARGET_URL | Target URL to scan (e.g., http://example.com/login.php) | Yes |
| -q | Quiet mode: Reduces verbose output | No |
| -w | Enable web bug detection | No |
| -e | Perform encoding tests for evasions | No |
| -d | Directory enumeration checks | No |
| -s | Additional scanning options (inferred from usage) | No |

## Examples

### Basic Usage

```bash
uniscan -u http://192.168.1.11/vcart/login.php -qweds
```

### Advanced Usage

```bash
uniscan -u https://target.com/app.php -qweds -o results.txt
```

(Assuming -o for output file; adjust based on tool version.)

## Expected Output

The output starts with tool banner and scan details, followed by domain info, skipped checks if 404 inconsistent, crawler results with plugins loaded, number of URLs found, lists of external hosts (potential RFI), emails harvested, and disclosures like phpinfo pages with config (e.g., allow_url_include: On indicating RFI risk). Success shows findings like '[+] phpinfo() page: [URL]' or external hosts.

## Related

- [[procedures/Scan-Web-Application-for-LFI-RFI-and-RCE-Using-Uniscan]]
- [[tools/uniscan]]
