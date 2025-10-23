---
id: 05c6095d-b80b-410a-967b-c4f127e6088f
name: Run dvcs-ripper container with rip-bzr.pl script
type: command
executor: bash
data: docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl
  -v -u
output: null
created_at: '2023-04-06T03:56:00.324877+00:00'
updated_at: '2023-04-10T20:33:54.895926+00:00'
---

# Run dvcs-ripper container with rip-bzr.pl script

```bash
docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl -v -u
```


