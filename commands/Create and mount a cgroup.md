---
id: e4701e2f-f540-4eec-8e90-990857055327
name: Create and mount a cgroup
type: command
executor: bash
data: "mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x\n\
  \ \necho 1 > /tmp/cgrp/x/notify_on_release"
output: null
created_at: '2023-04-06T03:56:17.110150+00:00'
updated_at: '2023-04-10T20:33:50.379078+00:00'
---

# Create and mount a cgroup

```bash
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
 
echo 1 > /tmp/cgrp/x/notify_on_release
```


