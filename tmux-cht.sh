#!/usr/bin/env bash

selected=`cat ~/.tmux-cht-languages ~/.tmux-cht-command | fzf`
if [[ -z $selected ]]; then
    exit 0
fi

read -p "$selected- Query: " query
if grep -qs "$selected" ~/.tmux-cht-languages; then
  tmux split-window -p 30 -h bash -c "curl cht.sh/$selected/$(echo "$query" | tr " " "+") | less"
else 
  tmux split-window -p 30 -h bash -c "curl cht.sh/$selected~$query | less"
fi
