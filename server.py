import json
from flask import Flask, Response, jsonify, abort
from code_scraping import scrape_articles
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome on my project! First, add /get_data to the URL to scrape the website.'

@app.route('/get_data')
def get_data():
    scrape_articles()
    text = '''Then, here are your options:
              /nb_articles : Show the number of articles scrapped
              /scraped_data : Show the data scrapped 
              /date_articles : Show the dates of all the articles
              /articles : Show the list of articles on the website
              /articles/<number> : Choose one article and show the info
              /ml : Sentiment and subjectivity analysis
              /ml/<number> : Choose one article and show the info'''
                            
    return Response(text, mimetype='text/plain')

@app.route('/nb_articles')  
def get_nb_articles():
    with open('articles.json') as json_file:
        data = json.load(json_file)
        return {'Number of articles': len(data)}

@app.route('/scraped_data')
def get_scraped_data():
    with open('articles.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)

@app.route('/date_articles')  
def get_date_articles():
    with open('articles.json') as json_file:
        data = json.load(json_file)
        dates = [article['date'] for article in data]
        return {'Number of articles': len(data), 'Dates': dates}

@app.route('/articles')
def articles():
    with open('articles.json', 'r') as json_file:
        data = json.load(json_file)
        articles_text = ""
        for idx, article in enumerate(data):
            articles_text += f"Article {idx + 1}: Title: {article['title']}, Date: {article['date']}\n"
        return Response(articles_text, mimetype='text/plain')

@app.route('/articles/<int:number>')
def article(number):
    try:
        with open('articles.json', 'r') as json_file:
            data = json.load(json_file)        
        if number < 1 or number > len(data):
            abort(404)        
        article = data[number - 1]
        title = article.get('title', 'No title available')
        date = article.get('date', 'No date available')
        url = article.get('url', 'No URL available')
        abstract = article.get('abstract', 'No abstract available')
        response_text = (
            f"Article {number}:\n"
            f"Title: {title}\n"
            f"Date: {date}\n"
            f"URL: {url}\n"
            f"Abstract: {abstract}\n"
        )

        return Response(response_text, mimetype='text/plain')
    except json.JSONDecodeError:
        return Response("Error decoding JSON", status=500)
    except FileNotFoundError:
        return Response("File not found", status=500)
    except Exception as e:
        return Response(str(e), status=500)


@app.route('/ml', defaults={'number': None})
@app.route('/ml/<int:number>')
def ml(number):
    try:
        with open('articles.json', 'r') as json_file:
            data = json.load(json_file)

        if number is None:
            results = []
            for idx, article in enumerate(data):
                analysis = TextBlob(article['title'])
                sentiment = analysis.sentiment
                results.append(f"Article {idx + 1}: Sentiment = {sentiment.polarity:.2f}, Subjectivity = {sentiment.subjectivity:.2f}")
            return Response("\n".join(results), mimetype='text/plain')
        else:
            if number < 1 or number > len(data):
                abort(404)
            article = data[number - 1]
            analysis = TextBlob(article['title'])
            sentiment = analysis.sentiment
            response_text = (
                f"Article {number}:\n"
                f"Title: {article['title']}\n"
                f"Sentiment: {sentiment.polarity:.2f}\n"
                f"Subjectivity: {sentiment.subjectivity:.2f}\n"
            )
            return Response(response_text, mimetype='text/plain')

    except json.JSONDecodeError:
        return Response("Error decoding JSON", status=500)
    except FileNotFoundError:
        return Response("File not found", status=500)
    except Exception as e:
        return Response(str(e), status=500)


if __name__ == '__main__':
    app.run()