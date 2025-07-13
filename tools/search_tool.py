from googlesearch import search
def search_google(query:str, num_results:int=5) -> list:
    """
    Perform a Google search and return a list of URLs.
    
    Args:
        query (str): The search query.
        num_results (int): Number of search results to return.
        
    Returns:
        list: A list of URLs from the search results.
    """
    return list(search(query, num_results=num_results))

