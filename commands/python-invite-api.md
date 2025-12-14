---
id: cmd-python-invite-api-001
data: >-
  python invite.py --project-id $PROJECT_ID --user $USERNAME --token
  $GITLAB_TOKEN --role developer
tags:
  - python
  - api
  - gitlab
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.900Z'
verified: false
validated: true
submitted: true
---
# python-invite-api

## Command

```bash
python invite.py --project-id $PROJECT_ID --user $USERNAME --token $GITLAB_TOKEN --role developer
```

## Description

Runs a Python script to invite users to a GitLab project via the API, automating victim targeting for XSS exposure. The script uses requests to POST to /api/v4/projects/:id/members.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--project-id` | ID of the target project | Yes |
| `--user` | Username or ID of invitee | Yes |
| `--token` | Personal access token with invite permissions | Yes |
| `--role` | Role like 'developer' | Yes |

## Examples

### Basic Usage

```bash
python invite.py --project-id 123 --user victim01 --token glpat-xxx --role developer
```

### Advanced Usage

```bash
python invite.py --project-id 123 --user victim01 --token glpat-xxx --role developer  # Batch via loop
```

## Expected Output

HTTP 201 Created with member details; error on failure.

## Related

- [[tools/Python]]
- [[procedures/Invite-Victim-and-Trigger-XSS-Execution]]
