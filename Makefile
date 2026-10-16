all:
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt

run:
	sudo .venv/bin/python3 main.py

clean:
	rm -rf .venv
	sudo rm -rf Addresses
