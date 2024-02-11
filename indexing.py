def createInvertedIndex(documents):
    wordFind = {}

    for docNo, allWords in documents.items():
        for valueWord in set(allWords):
            wordCount = allWords.count(valueWord)
            wordFind.setdefault(valueWord, {}).setdefault(docNo, 0)
            wordFind[valueWord][docNo] += wordCount

    finalDictionary = {indivWord: occurrences for indivWord, occurrences in wordFind.items()}
    return finalDictionary
