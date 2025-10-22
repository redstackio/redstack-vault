---
id: 5be43ceb-c5b6-43ad-b4ce-b410e3321441
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:25.723316+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 5be43ceb

**Language**: Bash

```bash

# .bash_profile PATH=$PATH:/home/james/ export PATH alias ls='ls -G'
alias grep='grep --color=auto'
alias la='ls -AlahG'
alias el='sudo $(history -p \!\!)'
alias ll='ls -alF'
alias l='ls -CF'
alias lg='ls -AlahG |grep $1'
alias netstati='lsof -P -i -n' export PS1="\n\n\[\$(if [[ \$? == 0 ]]; then echo \"\[$GREEN\]✓\"; else echo \"\[$RED\]✕\"; fi)[\033[33m\]\D{%Y%m%d_%H%M%S}\[\033[m\] \[\033[36m\]\u@\h__`ipconfig getifaddr en0`__`ipconfig getifaddr en8`\[\033[m\]] \[\033[1;31m\]\n[\w]\[\033[m\] \n \$

```
