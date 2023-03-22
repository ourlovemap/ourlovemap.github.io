ENV_NAME = map
PYTHON = python3
PIP = pip3
BRANCH = develop
PROJECT_PATH = "/Users/matheus_assis/Desktop/projects/Love-Map/love_map"

map:
	mamba create -n $(ENV_NAME) python=3.8

install:
	git checkout -b $(BRANCH)
	$(PIP) install -r requirements.txt
	git add requirements.txt
	git commit -m "Start | Add requirements"
	git push -u origin $(BRANCH)

setup-requirements:
	pip-compile --output-file=requirements/requirements.txt requirements/requirements.in --resolver=backtracking

run:
	streamlit run social_pulse/main/app.py