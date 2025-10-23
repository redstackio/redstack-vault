---
id: f7b1ef50-6175-4456-9805-c6104b6b9138
name: openssl Generate a SHA512 Hash
type: command
executor: bash
data: ' openssl passwd -6 -salt $_SALT $_PASSWORD'
output: 'root@hackers:~# openssl passwd -6 -salt 16bytesXX16bytes Thisisyourpassword

  $6$16bytesXX16bytes$FXuYP0OI7qYB3K6u6.91Blr7rtvjLZmpcuAWuWVnTj4G2nVGny6k5yzaDbV3iQCwoSDMGgXePvFxddnxYkpa5/'
created_at: '2019-09-16T18:26:12.711397+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# openssl Generate a SHA512 Hash

```bash
 openssl passwd -6 -salt $_SALT $_PASSWORD
```

## Expected Output

```
root@hackers:~# openssl passwd -6 -salt 16bytesXX16bytes Thisisyourpassword
$6$16bytesXX16bytes$FXuYP0OI7qYB3K6u6.91Blr7rtvjLZmpcuAWuWVnTj4G2nVGny6k5yzaDbV3iQCwoSDMGgXePvFxddnxYkpa5/
```


