---
id: a79fa9ac-9f97-42b2-8732-acb8610221ef
name: download emails via curl
type: command
executor: bash
data: 'curl --insecure --url "imaps://target-domain/Drafts;UID=4" --user "username:password"

  '
output: null
created_at: '2020-07-14T18:14:56.370702+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# download emails via curl

```bash
curl --insecure --url "imaps://target-domain/Drafts;UID=4" --user "username:password"

```
