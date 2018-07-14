# Contest Analyzer Online

This is a web page designed for ham radio contesters. It provides a set of tables and charts to analyze a contest operation.

# Run the web

This tool is prepared to be run with [Docker](https://docs.docker.com/) with the following command:

```bash
cd HamToolsManager/
docker-compose up
```

Click [here](http://localhost:8000/) to open the tool in your browser.


## No Docker available

The web can also be run even if no docker is available. The only requirement is to have a local Python 2.7 installation. Then, type the following commands:

```bash
pip install -r requirements.txt
cd HamToolsManager/
python manage.py runserver
```
