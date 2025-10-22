---
id: f561722b-2ae9-4962-811c-ed8bf3e71f2b
name: Dig zone transfer
type: command
executor: ''
data: dig axfr $DOMAIN@$NAMESERVER
output: dig axfr domain.local @nameservers.local
created_at: '2023-01-11T20:23:08.313927+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dig zone transfer

```bash
dig axfr $DOMAIN@$NAMESERVER
```

## Expected Output

```
dig axfr domain.local @nameservers.local
```
