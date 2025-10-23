---
id: a60b95fd-8edd-4c6d-b233-ada9de0a04dc
name: Export Certificates from Local Machine Store
type: command
executor: bash
data: 'privilege::debug

  crypto::capi

  crypto::cng

  crypto::certificates /systemstore:local_machine /store:my /export'
output: null
created_at: '2023-04-06T03:56:28.398187+00:00'
updated_at: '2023-04-10T20:37:30.878980+00:00'
---

# Export Certificates from Local Machine Store

```bash
privilege::debug
crypto::capi
crypto::cng
crypto::certificates /systemstore:local_machine /store:my /export
```


