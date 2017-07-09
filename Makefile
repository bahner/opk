#!/usr/bin/env make -f

clean:
	find opk -type d -name __pycache__ -exec rm -rf {} \;
	find opk -type f -name "*pyc" -delete
