---
id: cmd-uuid-1
data: |-
  import requests
  import json

  url="https://api.hackerone.com/v1/programs/44544"

  headers ={'Authorization':'Basic ████',}

  response = requests.request("GET", url, headers=headers)

  convert_to_json = json.loads(response.text)

  data = convert_to_json['data']['relationships']['members']
  for member in data['data']:
      member = member['attributes']['groups']
      print(member)
tags:
  - api
  - verification
  - dos
type: command
output: >-
  Repeated JSON objects for groups, e.g., hundreds of lines showing
  {'id':95004,'key':null,'name':'AAABC2','team_members_count':0,'permissions':[],'immutable':false,'team_member_ids':[]}
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.654Z'
verified: false
validated: true
submitted: true
---
# verify-hackerone-group-loop

## Command

```python
import requests
import json

url="https://api.hackerone.com/v1/programs/44544"

headers ={'Authorization':'Basic ████',}

response = requests.request("GET", url, headers=headers)

convert_to_json = json.loads(response.text)

data = convert_to_json['data']['relationships']['members']
for member in data['data']:
    member = member['attributes']['groups']
    print(member)
```

## Description

This Python script fetches details from the HackerOne API for a specific program and prints the groups associated with members, demonstrating the infinite loop by showing repeated group entries in the response due to the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | API endpoint for the program (e.g., https://api.hackerone.com/v1/programs/44544) | Yes |
| headers.Authorization | Base64 encoded Basic auth credentials (████ represents redacted token) | Yes |

## Examples

### Basic Usage

```python
import requests
import json

url="https://api.hackerone.com/v1/programs/44544"

headers ={'Authorization':'Basic ████',}

response = requests.request("GET", url, headers=headers)

convert_to_json = json.loads(response.text)

data = convert_to_json['data']['relationships']['members']
for member in data['data']:
    member = member['attributes']['groups']
    print(member)
```

### Advanced Usage

Modify the URL for different programs and add error handling:

```python
import requests
import json

url="https://api.hackerone.com/v1/programs/[PROGRAM_ID]"
headers ={'Authorization':'Basic [ENCODED_CREDS]'}
try:
    response = requests.request("GET", url, headers=headers)
    response.raise_for_status()
    convert_to_json = json.loads(response.text)
    data = convert_to_json['data']['relationships']['members']
    for member in data['data']:
        groups = member['attributes']['groups']
        print(f"Groups for member {member['id']}: {groups}")
except Exception as e:
    print(f"Error: {e}")
```

## Expected Output

The script outputs repeated JSON objects for the affected group, such as hundreds of lines of {'id':95004,'key':null,'name':'AAABC2','team_members_count':0,'permissions':[],'immutable':false,'team_member_ids':[]}, indicating the loop's persistence in API responses and database storage.

## Related

- [[procedures/Trigger-Infinite-Loop-by-Renaming-HackerOne-Group]]
