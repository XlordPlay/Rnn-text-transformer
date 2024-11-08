import pandas as pd
import re

def load_data(csv_file):
    # Загрузка данных из CSV
    df = pd.read_csv(csv_file)
    return df

def preprocess_text(text):
    # Удаление лишних символов и приведение к нижнему регистру
    text = re.sub(r'\n{2,}', '\n', text)  # Удаление лишних пустых строк
    text = text.strip()  # Удаление пробелов в начале и конце
    text = text.lower()  # Приведение к нижнему регистру
    text = re.sub(r'[^a-zа-яё0-9\s,.!?;:\'-]', '', text)  # Удаление специальных символов
    return text

def extract_play_text(df):
    # Объединение строк пьесы на основе столбца "PlayerLine"
    all_plays = {}
    
    for index, row in df.iterrows():
        play_name = row['Play']
        player_line = row['PlayerLine']
        
        if play_name not in all_plays:
            all_plays[play_name] = []
        
        all_plays[play_name].append(preprocess_text(player_line))
    
    # Объединение строк в текст пьесы
    for play_name in all_plays:
        all_plays[play_name] = '\n'.join(all_plays[play_name])
    
    return all_plays

def save_processed_data(processed_dir, all_plays):
    for play_name, text in all_plays.items():
        file_name = play_name.replace(" ", "_") + '.txt'  # Заменяем пробелы на _
        with open(f"{processed_dir}/{file_name}", 'w', encoding='utf-8') as file:
            file.write(text)

if __name__ == "__main__":
    csv_file = 'data/raw/Shakespeare_data.csv'
    processed_dir = 'data/processed'
    
    # Загрузка данных
    df = load_data(csv_file)
    
    # Извлечение текста пьес
    all_plays = extract_play_text(df)
    
    # Сохранение обработанных данных
    save_processed_data(processed_dir, all_plays)