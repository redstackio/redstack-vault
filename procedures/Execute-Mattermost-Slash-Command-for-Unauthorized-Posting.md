---
id: proc-uuid-001
tags:
  - mattermost
  - access-control-bypass
  - api-vulnerability
  - slash-command
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/mattermost-execute-slash-command]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:17.893Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: proc-uuid-001
name: Execute-Mattermost-Slash-Command-for-Unauthorized-Posting
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]]
techniques: [[Valid Accounts]], [[Exploit Public-Facing Application]]
sub_techniques: []
tags: mattermost, access-control-bypass, api-vulnerability, slash-command
commands: [[commands/mattermost-execute-slash-command]]
platforms: Web
tools: []
---

# Execute-Mattermost-Slash-Command-for-Unauthorized-Posting

## Summary

This procedure exploits an improper access control vulnerability in Mattermost by executing slash commands via the API, allowing users without post_message permissions to post messages in restricted channels. It demonstrates how the /api/v4/commands/execute endpoint fails to enforce the same checks as direct posting, enabling unauthorized communication or spam.

## Description

In Mattermost, team members with roles lacking channel post permissions should be restricted from sending messages. However, by sending a POST request to the /api/v4/commands/execute endpoint with a slash command like /echo, attackers can bypass these restrictions. The root cause is that the command execution endpoint does not validate post_message permissions, treating command outputs as valid posts. This can lead to information disclosure if sensitive data is echoed or disruption through spam. The procedure requires an authenticated session and knowledge of team and channel IDs, typically obtained from the web interface or prior reconnaissance.

## Requirements

1. Authenticated session cookie from a Mattermost team member account
2. Valid CSRF token extracted from the session (via browser dev tools or prior API call)
3. Target team_id and channel_id (e.g., from channel URLs like /team_id/channels/channel_name)
4. Access to an HTTP client like curl for API interaction
5. Mattermost instance version vulnerable to this issue (pre-fix for CVE or similar)

## Defense

Defensive measures and detection strategies:

- Enforce consistent permission checks across all API endpoints, including command execution
- Monitor API logs for unusual slash command executions from low-privilege users
- Implement rate limiting on /api/v4/commands/execute to prevent spam
- Use role-based access controls (RBAC) audits to identify permission gaps

## Objectives

1. Post a message to a restricted channel without direct post permissions
2. Validate the bypass by observing the message in the channel
3. Demonstrate potential for broader abuse like data exfiltration via custom commands

## Instructions

### Step 1: Authenticate and Gather IDs

**Context**: Log in to Mattermost as a team member without post permissions in the target channel. Extract session cookies, CSRF token, team_id, and channel_id from the browser or API.

No specific command; use browser dev tools to inspect network requests.

> Expected: Obtain values like team_id: '8jdphis493d4pbq3u1bagz643r', channel_id: 'khhnkrf5wf8yibwx8bd14s6fbw', and X-CSRF-Token.

### Step 2: Execute Slash Command

**Context**: Send the POST request to execute the /echo command, which posts the provided text to the channel.

**Command** ([[commands/mattermost-execute-slash-command]]):
```bash
curl -X POST https://your-mattermost-instance.com/api/v4/commands/execute \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: YOUR_CSRF_TOKEN" \
  -b "MMAUTHTOKEN=YOUR_SESSION_COOKIE" \
  -d '{"command":"/echo test_message","channel_id":"TARGET_CHANNEL_ID","team_id":"TARGET_TEAM_ID"}'
```

> This command sends a JSON payload to the endpoint. On success, it returns a 200 OK with execution details, and the 'test_message' appears in the channel. Failure would return a 403 or 400 if permissions were enforced.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/mattermost-execute-slash-command]]

## Tools Used

- None

## Tags

- mattermost
- access-control-bypass
- api-vulnerability
- slash-command
