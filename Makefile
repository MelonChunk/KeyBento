api-up:
	uvicorn src.main:app --reload --port 8001

frontend-up:
	npm start --prefix client

run-all:
	make api-up & make frontend-up
