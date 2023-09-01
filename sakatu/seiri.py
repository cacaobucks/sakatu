import pandas as pd
import re

# Load the CSV file into a DataFrame
file_path = 'sauna_reviews.csv'
df = pd.read_csv(file_path)

# Remove leading and trailing whitespaces and newlines
df['review'] = df['review'].str.strip()

# Remove empty or null reviews
df = df[df['review'].notna() & (df['review'] != '')]

# Remove newlines within the text
df['review'] = df['review'].str.replace('\n', ' ', regex=True)

# Remove extra spaces within the text
df['review'] = df['review'].str.replace(' +', ' ', regex=True)

# Remove emojis from the reviews
def remove_emojis(text):
    return re.sub(r'[^\w\s,]', '', text)
df['review'] = df['review'].apply(remove_emojis)

# Save the cleaned DataFrame to a new CSV file with UTF-8 encoding
cleaned_file_path_utf8 = 'sauna_reviews_cleaned.csv'
df.to_csv(cleaned_file_path_utf8, index=False, encoding='utf-8')