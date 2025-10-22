---
id: c9694bcf-16f7-4286-bc84-18b5841262a8
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:04.524465+00:00'
updated_at: '2023-04-10T20:25:56.021148+00:00'
---

# Code Snippet c9694bcf

**Language**: ps1

```ps1
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred -Domain "domain.local"
Add-DomainGroupMember -Identity 'LAPS READ' -Members 'user1' -Credential $cred -Domain "domain.local"
```
