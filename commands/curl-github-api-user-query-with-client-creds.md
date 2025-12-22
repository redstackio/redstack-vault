---
id: 3d510c46-ec34-4a69-9e11-f56cd571e092
name: curl-github-api-user-query-with-client-creds
type: command
executor: bash
data: >-
  curl
  'https://api.github.com/users/$_TARGET_USERNAME?client_id=$_CLIENT_ID&client_secret=$_CLIENT_SECRET'
output: null
created_at: '2023-04-06T03:55:52.237687+00:00'
updated_at: '2023-04-06T03:55:52.249415+00:00'
platforms:
  - Linux
  - macOS
tags:
  - api-query
  - credential-use
  - github
verified: true
validated: true
---

# curl-github-api-user-query-with-client-creds

## Command

```bash
curl 'https://api.github.com/users/$_TARGET_USERNAME?client_id=$_CLIENT_ID&client_secret=$_CLIENT_SECRET'
```

## Description

This command queries the GitHub API for user information using OAuth client credentials (ID and secret) for authentication. It is used to validate stolen credentials and retrieve account details like profile, email, and organizations, enabling further reconnaissance or access in a credential abuse scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_USERNAME | The GitHub username to query (e.g., 'octocat') | Yes |
| $_CLIENT_ID | The leaked OAuth client ID (e.g., 'abc123def456') | Yes |
| $_CLIENT_SECRET | The leaked OAuth client secret (e.g., 'ghp_789xyz') | Yes |
| -s (optional) | Silent mode to suppress progress meter | No |
| -H 'Accept: application/vnd.github.v3+json' (optional) | Specify API version header | No |

## Examples

### Basic Usage

```bash
curl 'https://api.github.com/users/octocat?client_id=abc123def456&client_secret=ghp_789xyz'
```

### Advanced Usage (with JSON output formatting)

```bash
curl -s 'https://api.github.com/users/octocat?client_id=abc123def456&client_secret=ghp_789xyz' | jq '.'
```

## Expected Output

Successful response is JSON with user data:

```json
{
  "login": "octocat",
  "id": 1,
  "node_id": "MDQ6VXNlcjE=",
  "avatar_url": "https://avatars.githubusercontent.com/u/1?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/octocat",
  "html_url": "https://github.com/octocat",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "following_url": "https://api.github.com/users/octocat/following{/other_user}",
  "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
  "organizations_url": "https://api.github.com/users/octocat/orgs",
  "repos_url": "https://api.github.com/users/octocat/repos",
  "events_url": "https://api.github.com/users/octocat/events{/privacy}",
  "received_events_url": "https://api.github.com/users/octocat/received_events",
  "type": "User",
  "site_admin": false,
  "name": "monalisa octocat",
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": null,
  "twitter_username": null,
  "public_repos": 8,
  "public_gists": 7,
  "followers": 5811,
  "following": 9,
  "created_at": "2008-10-09T17:46:40Z",
  "updated_at": "2023-04-06T03:55:52Z"
}
```

Error example (invalid creds): {"message":"Bad credentials","documentation_url":"https://docs.github.com/rest"}

## Related

- [[procedures/Access-GitHub-API-with-Leaked-Client-Credentials]]
