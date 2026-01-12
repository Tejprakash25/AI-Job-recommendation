try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError as e:
    raise ImportError(
        "scikit-learn is required to run matcher.calculate_match.\n"
        "Install it with: pip install scikit-learn"
    ) from e


def calculate_match(resume_text, job_text):
    # Return 0.0 if either text is empty to avoid errors from the vectorizer
    if not (resume_text and job_text):
        return 0.0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(vectors)[0][1]
    return round(float(score), 3)
