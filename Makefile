ACTIVATE=venv/bin/activate

venv: $(ACTIVATE)
$(ACTIVATE): requirements.txt requirements_test.txt
	test -d venv || virtualenv venv
	. $(ACTIVATE); pip install -r requirements.txt -r requirements_test.txt

.PHONY : clean
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

.PHONY : static-analysis
static-analysis: venv
	. $(ACTIVATE); flake8 .

.PHONY : test
test: venv
	. $(ACTIVATE); pytest
