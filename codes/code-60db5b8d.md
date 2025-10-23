---
id: 60db5b8d-5985-474d-b366-c05248c9154c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:18.766205+00:00'
updated_at: '2023-04-10T20:34:34.074102+00:00'
---

# Code Snippet 60db5b8d

**Language**: Powershell

```powershell
systemctl list-timers --all
NEXT                          LEFT     LAST                          PASSED             UNIT                         ACTIVATES
Mon 2019-04-01 02:59:14 CEST  15h left Sun 2019-03-31 10:52:49 CEST  24min ago          apt-daily.timer              apt-daily.service
Mon 2019-04-01 06:20:40 CEST  19h left Sun 2019-03-31 10:52:49 CEST  24min ago          apt-daily-upgrade.timer      apt-daily-upgrade.service
Mon 2019-04-01 07:36:10 CEST  20h left Sat 2019-03-09 14:28:25 CET   3 weeks 0 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service

3 timers listed.
```


