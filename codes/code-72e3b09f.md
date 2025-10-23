---
id: 72e3b09f-68f6-4512-aaba-432cb1ef6976
type: code
language: Ruby
verified: false
created_at: '2019-11-22T22:40:14.399861+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 72e3b09f

**Language**: Ruby

```ruby
conn = WinRM::Connection.new( 
   endpoint: 'http://10.10.10.10:5985/wsman',
#  transport: :ssl,
  user: 'Bob',
  password: 'hunter2',
  :no_ssl_peer_verification => true
)

```


