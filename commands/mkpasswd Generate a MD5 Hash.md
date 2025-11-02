---
id: 3dad85a5-aa24-4a02-820f-17a933bf0479
name: mkpasswd Generate a MD5 Hash
type: command
executor: bash
data: mkpasswd -5 -S $_SALT $_PASSWORD
output: 'root@hackers:~# mkpasswd -5 -S 8BytesXX Thisisyourpassword

  $1$8BytesXX$dXGg2H2MnwNoiq6UuVkws/'
created_at: '2019-09-16T18:26:12.712700+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[mkpasswd]]'
---

# mkpasswd Generate a MD5 Hash

```bash
mkpasswd -5 -S $_SALT $_PASSWORD
```

## Expected Output

```
root@hackers:~# mkpasswd -5 -S 8BytesXX Thisisyourpassword
$1$8BytesXX$dXGg2H2MnwNoiq6UuVkws/
```


