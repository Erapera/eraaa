import gradio as gr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Я люблю этот фильм",
    "Это лучший день в моей жизни",
    "Мне грустно и плохо",
    "Ужасный сервис, я недоволен",
    "Фильм был скучный и длинный",
    "Мне понравилось обслуживание"
]
labels = [1, 1, 0, 0, 0, 1]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_sentiment(text):
    X_test = vectorizer.transform([text])
    pred = model.predict(X_test)[0]
    return "Позитивный 😊" if pred == 1 else "Негативный 😞"

demo = gr.Interface(
    fn=predict_sentiment,
    inputs="text",
    outputs="text",
    title="Классификатор отзывов",
    description="Простая ML-модель на Gradio."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=10000)
