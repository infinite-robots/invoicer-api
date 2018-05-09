.PHONY: clean relclean venv test table populate docker

docker:
	@echo "==> Running docker-compose build"
	docker-compose build
	@echo "==> Running docker-compose up"
	docker-compose up

clean:
	@echo "==> cleaning working files"
	@find . -name \*~ -delete
	@find . -name \*.pyc -delete
	@find . -name \#* -delete
