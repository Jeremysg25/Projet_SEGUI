# Esilv_Api_Project

### Project

I choose the website PapersWithCode.com, which is a website that acts as a central platform for artificial intelligence (AI) and machine learning (ML) research. Its main objective is to provide a comprehensive search repository where users can find research articles, related source codes, as well as experimental results.

### Objective

/get_data: This endpoint is mandatory because it scrapes the data to use the other endpoints.
Example usage: http://127.0.0.1:5000/get_data

/scraped_data: It shows all the data scraped from the website.
Example usage: http://127.0.0.1:5000/scraped_data

/nb_articles: This endpoint retrieves the number of articles scraped from the website.
Example usage: http://127.0.0.1:5000/

/date_articles: Retrieves the publication dates of all the articles scraped from the website.
Example usage: http://127.0.0.1:5000/date_articles

/articles: Displays a formatted list of articles with their titles and publication dates. Each article is numbered for easy reference.
Example usage: http://127.0.0.1:5000/

/articles/<number>: Fetches the full information of a specific article identified by its number. It returns the title, publication date, URL, and abstract of the article.
Example usage: http://127.0.0.1:5000/articles/1 (to fetch the first article)

/ml and /ml/<number>: Executes a machine learning script to perform sentiment analysis on the fetched articles. It can analyze either all retrieved articles or a single specified one. The sentiment analysis results include the polarity and subjectivity of the article's title.
Example usage: http://127.0.0.1:5000/ml (for all articles) and http://127.0.0.1:5000/ml/1 (for the first article)

Polarity measures the degree of positivity or negativity of the title, where 0 corresponds to neutrality. Subjectivity indicates to what extent the title is based on opinions rather than facts, with 0 corresponding to objectivity and 1 corresponding to total subjectivity.

These endpoints provide a comprehensive interface for interacting with AI news data, offering functionalities such as retrieving articles, obtaining article metadata, reading full articles, and performing sentiment analysis on article titles.