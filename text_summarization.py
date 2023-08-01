import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def summarize_text(text, num_sentences):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into words
    words = [word_tokenize(sentence.lower()) for sentence in sentences]
    
    # Remove stop words from the words list
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    for sentence in words:
        filtered_sentence = []
        for word in sentence:
            if word not in stop_words:
                filtered_sentence.append(word)
        filtered_words.append(filtered_sentence)
    
    # Stem words using Porter Stemmer
    stemmer = PorterStemmer()
    stemmed_words = []
    for sentence in filtered_words:
        stemmed_sentence = []
        for word in sentence:
            stemmed_sentence.append(stemmer.stem(word))
        stemmed_words.append(stemmed_sentence)
    
    # Calculate sentence scores based on word frequency
    word_frequencies = {}
    for sentence in stemmed_words:
        for word in sentence:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    sentence_scores = {}
    for i in range(len(stemmed_words)):
        score = 0
        for word in stemmed_words[i]:
            score += word_frequencies[word]
        sentence_scores[i] = score
    
    # Get top n sentences with highest scores
    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    top_sentences = []
    for i in range(min(num_sentences, len(sorted_scores))):
        top_sentences.append(sentences[sorted_scores[i][0]])
    
    # Return summary as a string
    summary = ' '.join(top_sentences)
    
    return summary