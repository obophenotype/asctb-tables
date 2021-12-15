NAME = asctb
RUN = poetry run
project:
	$(RUN) gen-project -d $(NAME) $(NAME).yaml

md:
	$(RUN) gen-markdown -d docs $(NAME).yaml

data/vasculature.tsv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/13g01JtzQJYNrKZx7eF6njWtkMl5O6JNSwwWvzpGyZqE/export?format=tsv&gid=0' > $@

docserve:
	$(RUN) mkdocs serve

deploy-docs:
	$(RUN) mkdocs gh-deploy
