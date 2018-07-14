# Contest Analyzer Online

This is a web page designed for ham radio contesters. It provides a set of tables and charts to analyze a contest operation.

# Run the web

The preferred way to run the web is with [Docker](https://docs.docker.com/). To do so, please type the following commands:

```bash
cd HamToolsManager/
docker-compose up
```

And that is it! Now click [here](http://localhost:8000/) to open the web in your browser.


## No Docker available

In case Docker is not available, this web can also be run. The only requirement is to have a local [Python 2.7 installation](https://www.python.org/). Once it is available in your system, type the following commands to install the required libraries and start the web:

```bash
pip install -r requirements.txt
cd HamToolsManager/
python manage.py runserver
```
