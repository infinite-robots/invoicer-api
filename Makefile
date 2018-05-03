.PHONY: clean relclean venv

test:
	@echo "==> Starting dev server"
	FLASK_APP=invoicer/application.py \
	FLASK_DEBUG=1 \
	./venv/bin/flask run --host=0.0.0.0

venv:
	@if [ ! -d venv ]; then \
	  echo "==> Installing virtualenv"; \
	  virtualenv venv; \
	fi
	@echo "==> Installing dependencies"
	@./venv/bin/pip install -e .

clean:
	@echo "==> cleaning working files"
	@find . -name \*~ -delete
	@find . -name \*.pyc -delete
	@find . -name \#* -delete

relclean: clean
	@echo "==> Removing dev venv"
	@rm -rf venv invoicer_api.egg-info
