.PHONY: start start_build stop unit_tests
UNIT_TESTS=pytest tests

start:
	@docker-compose up -d #@ if u dont wanna see the command in the terminal
start_build:
	@docker-compose up --build -d
stop:
	@docker-compose down
unit_tests:
	@docker-compose exec -T app-test $(UNIT_TESTS)
unit_tests_local:
	@$(UNIT_TESTS)
check_typing:
	@docker-compose exec -T app-test mypy .
