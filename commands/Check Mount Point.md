---
id: 270a4901-6a9f-4477-9534-18b2a484ef00
name: Check Mount Point
type: command
executor: bash
data: '$ mount | head -n 1

  overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/YLH6C6EQMMG7DA2AL5DUANDHYJ:/var/lib/docker/overlay2/l/HP7XLDFT4ERSCYVHJ2WMZBG2YT,upperdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff,workdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/work)'
output: null
created_at: '2023-04-06T03:56:17.157140+00:00'
updated_at: '2023-04-10T20:33:47.322105+00:00'
---

# Check Mount Point

```bash
$ mount | head -n 1
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/YLH6C6EQMMG7DA2AL5DUANDHYJ:/var/lib/docker/overlay2/l/HP7XLDFT4ERSCYVHJ2WMZBG2YT,upperdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff,workdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/work)
```
