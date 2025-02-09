import os
import re
from nltk.corpus import stopwords

def clean_text(text):
    # Remove non-ASCII characters
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Remove extra newlines
    text = re.sub(r"\n+", "\n", text)
    return text

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def clean_text_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            txt_path = os.path.join(folder_path, filename)
            with open(txt_path, 'r') as f:
                text = f.read()
            cleaned_text = clean_text(text)
            cleaned_text = remove_stop_words(cleaned_text)
            cleaned_txt_path = txt_path.replace(".txt", "_cleaned.txt")
            with open(cleaned_txt_path, 'w') as f:
                f.write(cleaned_text)
            print(f"Cleaned text in {filename} and saved to {cleaned_txt_path}")
