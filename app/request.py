
from .models import Quote
import request


def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    response = request.get("http://quotes.stormconsultancy.co.uk/random.json").json()

    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote