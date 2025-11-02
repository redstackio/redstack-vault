---
id: 08a6132e-8a6a-4541-87fe-987825226d21
name: systemctl Link a Service Unit File
type: command
executor: bash
data: sudo systemctl link $FULL_PATH_TO_FILE
output: "bob@ubuntu18:/tmp$ sudo systemctl enable --now /tmp/root.service \n\nCreated\
  \ symlink /etc/systemd/system/multi-user.target.wants/root.service → /tmp/root.service.\n\
  Created symlink /etc/systemd/system/root.service → /tmp/root.service."
created_at: '2019-10-16T23:21:22.677582+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[sudo]]'
- '[[systemctl]]'
---

# systemctl Link a Service Unit File

```bash
sudo systemctl link $FULL_PATH_TO_FILE
```

## Expected Output

```
bob@ubuntu18:/tmp$ sudo systemctl enable --now /tmp/root.service 

Created symlink /etc/systemd/system/multi-user.target.wants/root.service → /tmp/root.service.
Created symlink /etc/systemd/system/root.service → /tmp/root.service.
```


