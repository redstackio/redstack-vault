---
id: 5008b449-9ce9-44c0-ba79-6e3644d19a44
name: mkpasswd Generate a SHA512 Hash
type: command
executor: bash
data: ' mkpasswd -m sha-512 -S $_SALT $_PASSWORD'
output: 'root@hackers:~# mkpasswd -m sha-512 -S 16bytesXX16bytes Thisisyourpassword

  $6$16bytesXX16bytes$FXuYP0OI7qYB3K6u6.91Blr7rtvjLZmpcuAWuWVnTj4G2nVGny6k5yzaDbV3iQCwoSDMGgXePvFxddnxYkpa5/'
created_at: '2019-09-16T18:26:12.712091+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mkpasswd Generate a SHA512 Hash

```bash
 mkpasswd -m sha-512 -S $_SALT $_PASSWORD
```

## Expected Output

```
root@hackers:~# mkpasswd -m sha-512 -S 16bytesXX16bytes Thisisyourpassword
$6$16bytesXX16bytes$FXuYP0OI7qYB3K6u6.91Blr7rtvjLZmpcuAWuWVnTj4G2nVGny6k5yzaDbV3iQCwoSDMGgXePvFxddnxYkpa5/
```


