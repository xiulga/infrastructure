up:
	docker-compose up --build

down:
	docker-compose down

pull:
	git submodule update --init --recursive

update:
	git submodule foreach git pull origin main
