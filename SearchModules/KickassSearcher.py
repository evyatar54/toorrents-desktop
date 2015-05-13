
from KickassAPI import *

from StubSearcher import Searcher

torrentList = []
  
  
class QueryResults:
  
  def __init__(self, query="", results=[]):
    self.query = query
    self.results = results
    
    
class KickassSearcher(Searcher):
    def __init__(self):
	Searcher.__init__(self)
	
    def search(self, queries):
	results = []
	for q in queries:
	    print "searching:\n", q
	    result = None
	    try:
		result = Search(q)
		resList = result.list()
	    except ValueError:
		print "no matches found for:\n", q
		resList = []
	    QR = QueryResults(q, resList)
	    results.append(QR)

	return results