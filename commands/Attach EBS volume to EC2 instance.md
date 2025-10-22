---
id: f30d0188-ff3f-4743-9599-c64a262b358b
name: Attach EBS volume to EC2 instance
type: command
executor: bash
data: aws ec2 attach-volume --volume-id VolumeID --instance-id InstanceID --device
  /dev/sdfd -> Can be other value
output: null
created_at: '2023-04-06T03:56:13.827098+00:00'
updated_at: '2023-04-10T20:20:08.029223+00:00'
---

# Attach EBS volume to EC2 instance

```bash
aws ec2 attach-volume --volume-id VolumeID --instance-id InstanceID --device /dev/sdfd -> Can be other value
```
