#!/usr/bin/env bash
all: main

main: main.py
	printf "#!/bin/bash\npython main.py \$1 \$2 \$3\n" > ./main && chmod +x ./main

clean:
	rm main
	