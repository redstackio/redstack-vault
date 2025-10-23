---
id: 3d6de3eb-4de8-496d-a50c-7300ecc81e3f
name: Create Personal Access Token for GitLab API
type: command
executor: bash
data: 'curl -k --request POST --header "PRIVATE-TOKEN: apiToken" --data "name=user-persistence-token"
  --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data
  "scopes[]=write_repository" "https://gitlabHost/api/v4/users/UserIDNumber/personal_access_tokens"'
output: null
created_at: '2023-04-06T03:56:25.247231+00:00'
updated_at: '2023-04-10T20:34:09.415829+00:00'
---

# Create Personal Access Token for GitLab API

```bash
curl -k --request POST --header "PRIVATE-TOKEN: apiToken" --data "name=user-persistence-token" --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data "scopes[]=write_repository" "https://gitlabHost/api/v4/users/UserIDNumber/personal_access_tokens"
```


