---
id: 9bc5e770-9f20-4ba3-8906-26a688e95ee6
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:25.247153+00:00'
updated_at: '2023-04-10T20:34:09.418264+00:00'
---

# Code Snippet 9bc5e770

**Language**: ps1

```ps1
curl -k --request POST --header "PRIVATE-TOKEN: apiToken" --data "name=user-persistence-token" --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data "scopes[]=write_repository" "https://gitlabHost/api/v4/users/UserIDNumber/personal_access_tokens"
```


