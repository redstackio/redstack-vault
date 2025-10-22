---
id: 17e45e26-5ba6-4649-9bb7-8391c5e44da0
name: Restore Old Configuration
type: command
executor: bash
data: certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889
  -template 'ESC4' -configuration ESC4.json
output: null
created_at: '2023-04-06T03:56:05.850160+00:00'
updated_at: '2023-04-10T20:25:59.025048+00:00'
---

# Restore Old Configuration

```bash
certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889 -template 'ESC4' -configuration ESC4.json
```
