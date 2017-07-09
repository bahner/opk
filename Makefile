#!/usr/bin/env make -f

clean:
	find opk -type d -name __pycache__ -print0 | xargs -r0 rm -rf 
	find opk -type f -name "*pyc" -delete
