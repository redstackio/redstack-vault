---
id: 5dba9b0a-d8bd-4333-8ba0-78b22253c626
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:15.055485+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 5dba9b0a

**Language**: Bash

```bash

<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
        *[System[EventID='4768']]
        and
        *[EventData[Data[@Name='TargetUserName'] != 'ANONYMOUS LOGON']]
        and
        *[EventData[Data[@Name='ServiceName'] = 'krbtgt']]
        and
        *[EventData[Data[@Name='TicketEncryptionType'] = '0x17']]
        </Select>
  </Query>
</QueryList>

```
