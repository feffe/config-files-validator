ACTIVATE=venv/bin/activate

venv: $(ACTIVATE)
$(ACTIVATE): requirements.txt requirements_dev.txt
	test -d venv || virtualenv venv
	. $(ACTIVATE); pip install -r requirements_dev.txt

.PHONY : clean
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf build
	rm -rf dist
	rm -rf config_files_validator.egg-info

.PHONY : lint
lint: venv
	. $(ACTIVATE); flake8

.PHONY : test
test: venv
	. $(ACTIVATE); pytest
