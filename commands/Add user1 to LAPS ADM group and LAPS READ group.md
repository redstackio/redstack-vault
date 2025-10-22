---
id: 6edfe0b7-0342-4311-ad6a-e5696d063d26
name: Add user1 to LAPS ADM group and LAPS READ group
type: command
executor: bash
data: 'Add-DomainGroupMember -Identity ''LAPS ADM'' -Members ''user1'' -Credential
  $cred -Domain "domain.local"

  Add-DomainGroupMember -Identity ''LAPS READ'' -Members ''user1'' -Credential $cred
  -Domain "domain.local"'
output: null
created_at: '2023-04-06T03:56:04.524544+00:00'
updated_at: '2023-04-10T20:25:56.022230+00:00'
---

# Add user1 to LAPS ADM group and LAPS READ group

```bash
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred -Domain "domain.local"
Add-DomainGroupMember -Identity 'LAPS READ' -Members 'user1' -Credential $cred -Domain "domain.local"
```
