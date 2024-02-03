.PHONY: run fclean re

run:
	python3 main.py

fclean:
	rm -f *.pyc

re: fclean run
