import os
import preprocessing
import indexing
import retrievalandranking
import nltk
# import preprocess from preprocessing

documents = {}

def extractSubDocuments(docContent):
    documents = {}

    subDocs = docContent.split('<DOC>')[1:]

    for subDoc in subDocs:
        # Extract document name from <DOCNO> tag
        docNoStart = subDoc.find('<DOCNO>') + len('<DOCNO>')
        docNoEnd = subDoc.find('</DOCNO>', docNoStart)
        docName = subDoc[docNoStart:docNoEnd].strip()

        # Extract text from <TEXT> tag
        textStart = subDoc.find('<TEXT>') + len('<TEXT>')
        textEnd = subDoc.find('</TEXT>', textStart)
        textContent = subDoc[textStart:textEnd].strip()

        # Store in the nested dictionary
        documents[docName] = textContent

    return documents

for file in os.listdir('testing'):
    filepath = 'testing/' + file
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            documents.update(extractSubDocuments(file.read()))

# Testing if the document reader seperates each subDoc correctly
# print(documents["AP880212-0001"][:10])
# print(documents["AP881120-0001"][:10])

preprocessing.preprocess(documents)

print(documents["AP880212-0001"])
# invertedIndex = indexing(tokens)

# retrievalandranking(invertedIndex)
