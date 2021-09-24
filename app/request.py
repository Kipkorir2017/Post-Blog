from flask import request

from .models import Quote


def get_quote():
    """
    Function to take http request and return an instance of a Quote
    """
    response = request.get("http://quotes.stormconsultancy.co.uk/random.json").json()

    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote


