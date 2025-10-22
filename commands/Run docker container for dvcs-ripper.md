---
id: 533036c5-d819-41ae-bd50-8cba6e409e01
name: Run docker container for dvcs-ripper
type: command
executor: bash
data: docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl
  -v -u
output: null
created_at: '2023-04-06T03:56:00.387422+00:00'
updated_at: '2023-04-10T20:33:57.951547+00:00'
---

# Run docker container for dvcs-ripper

```bash
docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl -v -u
```
