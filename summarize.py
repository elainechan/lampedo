from nltk.corpus import reuters
from nltk.corpus import stopwords
import nltk

def content_fraction(text):
	stopwords = nltk.corpus.stopwords.words("english")
	content = [w for w in text if w.lower() not in stopwords]
	return len(content) / len(text)

content_fraction(nltk.corpus.reuters.words())


def collection_stats():

	# List of documents
	documents = reuters.fileids()
	print(str(len(documents)) + " " + "documents")

	train_docs = list(filter(lambda doc: doc.startswith("train"), documents))
	print(str(len(train_docs)) + " " + "total training documents")

	test_docs = list(filter(lambda doc: doc.startswith("test"), documents))
	print(str(len(test_docs)) + " " + "total test documents")

	# List of categories
	categories = reuters.categories()
	print(str(len(categories)) + " " + "categories")

	# Documents in a category
	category_docs = reuters.fileids("acq")

	# Words for a document
	document_id = category_docs[0]
	document_words = reuters.words(category_docs[0])
	print(document_words)

	# Raw document
	print(reuters.raw(document_id))

