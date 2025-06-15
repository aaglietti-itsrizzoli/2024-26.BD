# 2024-26.BD

## Get text from wikipedia pages

https://wikitext.eluni.co/

py-spy record -o profile.svg -- python map-reduce.py

ps -L -p $(pgrep -f map-reduce.py)

strace -f -e trace=clone -o strace.out.txt python map-reduce.py

strace -ff -o strace.out.txt python map-reduce.py
