---
id: 55e115e3-5241-41fc-a608-7f193189896a
name: Ruby Install WinRM Dependencies
type: command
executor: bash
data: gem install winrm-fs
output: "root@kali:~# gem install winrm-fs          \nFetching: erubi-1.9.0.gem (100%)\
  \    \nSuccessfully installed erubi-1.9.0        \nFetching: little-plugger-1.1.4.gem\
  \ (100%)\nSuccessfully installed little-plugger-1.1.4   \nFetching: logging-2.2.2.gem\
  \ (100%)   \nSuccessfully installed logging-2.2.2       \nFetching: rubyzip-2.0.0.gem\
  \ (100%)      \nSuccessfully installed rubyzip-2.0.0          \nFetching: builder-3.2.3.gem\
  \ (100%)       \n...\n...\nDone installing documentation for erubi, little-plugger,\
  \ logging, rubyzip, builder, gssapi, gyoku, nori, rubyntlm, winrm, winrm-fs after\
  \ 2 seconds"
created_at: '2019-11-22T22:40:14.392316+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Ruby Install WinRM Dependencies

```bash
gem install winrm-fs
```

## Expected Output

```
root@kali:~# gem install winrm-fs          
Fetching: erubi-1.9.0.gem (100%)    
Successfully installed erubi-1.9.0        
Fetching: little-plugger-1.1.4.gem (100%)
Successfully installed little-plugger-1.1.4   
Fetching: logging-2.2.2.gem (100%)   
Successfully installed logging-2.2.2       
Fetching: rubyzip-2.0.0.gem (100%)      
Successfully installed rubyzip-2.0.0          
Fetching: builder-3.2.3.gem (100%)       
...
...
Done installing documentation for erubi, little-plugger, logging, rubyzip, builder, gssapi, gyoku, nori, rubyntlm, winrm, winrm-fs after 2 seconds
```


