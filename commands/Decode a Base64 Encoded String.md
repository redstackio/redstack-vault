---
id: 0184868e-c2dc-4568-8901-cba61d7864c1
name: Decode a Base64 Encoded String
type: command
executor: ''
data: base64 -d <<< $_STRING
output: 'root@kali:~# base64 -d <<< c3VwZXJ0b3BzZWNyZXQhISEhCg==

  supertopsecret!!!!'
created_at: '2020-03-26T03:48:55.520527+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Decode a Base64 Encoded String

```bash
base64 -d <<< $_STRING
```

## Expected Output

```
root@kali:~# base64 -d <<< c3VwZXJ0b3BzZWNyZXQhISEhCg==
supertopsecret!!!!
```
