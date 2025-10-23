---
id: 802302f3-40e4-4dbb-bfd4-51dd608dceb3
name: Map remote target folder as local drive (LOL)
type: command
executor: ''
data: 'net use t: \\$DOMAIN\C$\Users\Public /user:$DOMAIN\$USERNAME $PASSWORD'
output: The command completed successfully
created_at: '2023-01-12T22:19:00.382798+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Map remote target folder as local drive (LOL)

```bash
net use t: \\$DOMAIN\C$\Users\Public /user:$DOMAIN\$USERNAME $PASSWORD
```

## Expected Output

```
The command completed successfully
```


