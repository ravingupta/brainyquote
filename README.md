# brainyquote scrapper
Python Script to fetch all quotes from brainyquote.com. 
It is a scrapper which results in quotes.csv file containing quote details and authors.txt authors links.

### How to use 
- Clone the repository and move inside the directory using CLI
- Install dependencies if required
- Run `python quotes.py`

### To work on virtual environment
- `pip install virtualenv` install virtualenv
- Run `virtualenv venv` to create 'venv' directory for virtual environment setup
- Run `source venv/bin/activate` to activate virtual environment

### Install Dependencies
- Install Requests Library run `pip install requests`
- Install lxml Library run `pip install lxml`

### Suggestion
It will take time to scrap all the links and fetch data so try to run it on any cloud server using `nohup` or anything to keep it running without waiting.