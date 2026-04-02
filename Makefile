.PHONY: deploy init serve gitc log up

up:
	sudo apt-get update && sudo apt-get install -y \
		libnss3 \
		libatk-bridge2.0-0 \
		libgtk-3-0 \
		libgbm-dev \
		libasound2 \
		libx11-xcb1 \
		libxcomposite1 \
		libxcursor1 \
		libxdamage1 \
		libxi6 \
		libxtst6 \
		libxrandr2 \
		libxss1

serve:
	@echo "Starting the MkDocs server..."
	@source .env && mkdocs serve

log:
	@echo "Starting the MkDocs server..."
	@source ./.env && mkdocs serve 2>&1 | tee mkdocs.log

init: gitc
	@echo "Configure container"
	@sudo apt-get update && sudo apt-get install -y \
		libnss3 \
		libatk-bridge2.0-0 \
		libgtk-3-0 \
		libgbm-dev \
		libasound2 \
		libx11-xcb1 \
		libxcomposite1 \
		libxcursor1 \
		libxdamage1 \
		libxi6 \
		libxtst6 \
		libxrandr2 \
		libxss1
	@echo "Start PIP configuration"
	@pip3 install --break-system-packages --upgrade pip
	@pip3 install --break-system-packages mkdocs mkdocs-material mkdocs-git-authors-plugin mkdocs-git-revision-date-localized-plugin mkdocs-git-committers-plugin
	@echo "Configuration is done"

gitc:
	git config pull.rebase false
	git config --global user.name "Serhioromano"
	git config --global user.email "Serhioromano@outlook.com"

deploy:
	@echo "Deploying the application..."
	@mkdocs gh-deploy
	@echo "Deployment complete."