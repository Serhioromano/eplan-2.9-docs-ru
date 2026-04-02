import json
import os
import requests
import time
import html2text
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urlparse

# Пути
INPUT_FILE = "29/api_tree.json"
OUTPUT_DIR = Path("../docs/2.9/api")
LOG_FILE = Path("processed_linksapi.txt")

# Настройки для Markdown
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False # Теперь обрабатываем картинки
h.body_width = 0       # Не переносить строки автоматически

# Словарь для заголовков Admonition
TITLES = {
    'note': 'Замечание:',
    'tip': 'Совет:',
    'warning': 'Предупреждение:',
    'example': 'Пример:'
}

def load_processed_links():
    """Загружает список уже скачанных ссылок."""
    if LOG_FILE.exists():
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f)
    return set()

def mark_as_processed(url):
    """Добавляет ссылку в лог."""
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(url + '\n')

BASE_IMAGE_ROOT = "https://www.eplan.help/ru-ru/Infoportal/Content/Plattform/2.9/Content/"

def download_image(img_url, output_dir, page_url):
    """Скачивает картинку и возвращает относительный путь."""
    try:
        # Формируем полный URL
        if img_url.startswith('../'):
            full_url = requests.compat.urljoin(BASE_IMAGE_ROOT, img_url.replace('../', ''))
        elif not img_url.startswith('http'):
            full_url = requests.compat.urljoin(BASE_IMAGE_ROOT, img_url)
        else:
            full_url = img_url
            
        parsed = urlparse(full_url)
        filename = os.path.basename(parsed.path)
        
        # Пропускаем служебные картинки
        if filename == 'transparent.gif':
            return img_url

        if not filename:
            filename = f"img_{hash(full_url)}.png"
        
        images_dir = output_dir / "images"
        images_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = images_dir / filename
        
        # Deduplication: если файл существует, просто возвращаем путь
        if filepath.exists():
            return f"images/{filename}"

        # Скачивание
        response = requests.get(full_url, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return f"images/{filename}"
        else:
            print(f"❌ Ошибка скачивания картинки {full_url} (код {response.status_code}) на странице {page_url}")
            return img_url
            
    except Exception as e:
        print(f"⚠️ Ошибка при обработке картинки {img_url} на странице {page_url}: {e}")
        return img_url

# Файл глоссария
GLOSSARY_FILE = OUTPUT_DIR / "glossary.md"

def get_glossary_definition(url, base_url):
    """Скачивает глоссарий, извлекает определение и записывает в файл."""
    full_url = requests.compat.urljoin(base_url, url)
    
    try:
        response = requests.get(full_url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h3').get_text(strip=True) if soup.find('h3') else "Unknown"
            definition = soup.find('p', class_='glossary').get_text(strip=True) if soup.find('p', class_='glossary') else ""
            
            if definition:
                entry = f'*[{title}]: {definition}\n'
                # Простая проверка на наличие в файле перед записью
                if not GLOSSARY_FILE.exists() or entry not in open(GLOSSARY_FILE, 'r', encoding='utf-8').read():
                    with open(GLOSSARY_FILE, 'a', encoding='utf-8') as f:
                        f.write(entry)
            return title
    except Exception as e:
        print(f"⚠️ Ошибка при обработке глоссария {full_url}: {e}")
    return None

def save_as_markdown(html_content, filename, current_url):
    """Преобразует HTML в Markdown, заменяя note, tip, warning и example на Admonitions."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        output_dir = filename.parent
        # Базовый URL для относительных ссылок
        parsed = urlparse(current_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path.rsplit('/', 1)[0]}/"

        # 1.5. Обработка жирного курсива (Bold + Italic)
        # Ищем теги с классом 'important' -> превращаем в жирный курсив (Markdown: ***Text***)
        for span in soup.find_all('span', class_='important'):
            text = span.get_text()
            span.replace_with(soup.new_string(f"***{text}***"))

        # 2. Обработка картинок
        for img in soup.find_all('img'):
            if img.has_attr('src'):
                img['src'] = download_image(img['src'], output_dir, current_url)
        
        # 3. Обработка заголовков Gui_Heading (превращаем в ###)
        for p in soup.find_all('p', class_='Gui_Heading'):
            header_text = p.get_text(strip=True)
            new_header = soup.new_tag('h3')
            new_header.string = header_text
            p.replace_with(new_header)
        
        admonitions = []
        
        # 4. Обработка простых блоков (note, tip, warning)
        for class_name in ['note', 'tip', 'warning']:
            for div in soup.find_all('div', class_=class_name):
                # Удаляем только заголовок (Infoblock_Heading)
                heading = div.find('p', class_='Infoblock_Heading')
                if heading:
                    heading.decompose()

                body_md = h.handle(str(div)).strip()
                admon_title = TITLES.get(class_name, "Примечание")
                
                placeholder = f"@@@ADMON_{len(admonitions)}@@@"
                indented_body = "\n    ".join(body_md.splitlines())
                admonition = f'\n\n!!! {class_name} "{admon_title}"\n\n    {indented_body}\n\n\n'
                
                admonitions.append(admonition)
                div.replace_with(placeholder)

        # 5. Обработка сложных блоков (example)
        for div in soup.find_all('div', class_='example'):
            body = div.find('div', class_='dropDownBody')
            body_text = body.get_text(strip=True) if body else ""
            
            placeholder = f"@@@ADMON_{len(admonitions)}@@@"
            admonition = f'\n\n!!! example "{TITLES["example"]}"\n\n    {body_text}\n\n\n'
            
            admonitions.append(admonition)
            div.replace_with(placeholder)

        # Конвертируем остальной текст
        md_content = h.handle(str(soup))
        
        # Вставляем блоки обратно на места плейсхолдеров
        for i, block in enumerate(admonitions):
            md_content = md_content.replace(f"@@@ADMON_{i}@@@", block)
        
        md_filename = filename.with_suffix('.md')
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"📄 Конвертировано в MD: {md_filename.name}")
    except Exception as e:
        print(f"⚠️ Ошибка при конвертации в MD: {e}")

def download_file(url, output_folder, processed_links):
    """Скачивает файл в бинарном режиме."""
    parsed_url = urlparse(url)
    filename_from_url = os.path.basename(parsed_url.path)
    
    # Если URL заканчивается слэшем или путь пуст — ставим index.html
    if not filename_from_url:
        filename_from_url = "index.html"
        
    filename = output_folder / filename_from_url
    
    # Если файл уже существует, пропускаем скачивание
    if filename.exists():
        print(f"⏩ Пропуск (файл существует): {filename_from_url}")
        mark_as_processed(url)
        return False
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # 1. Сохраняем оригинал (HTML)
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            # 2. Конвертируем в Markdown
            save_as_markdown(response.content, filename, url)
            
            mark_as_processed(url)
            print(f"✅ Скачано: {filename_from_url}")
            return True
        else:
            print(f"❌ Ошибка {response.status_code}: {url}")
    except Exception as e:
        print(f"❌ Ошибка при скачивании {url}: {e}")
    return False

def traverse_and_download(node, output_folder, processed_links):
    """Рекурсивный обход дерева ссылок."""
    if "link" in node and node["link"].startswith("http"):
        # Исключаем узлы-пустышки
        if node["link"].endswith("___"):
            print(f"⏩ Пропуск (организационный узел): {node.get('title', 'Без названия')}")
        elif node["link"] not in processed_links:
            success = download_file(node["link"], output_folder, processed_links)
            if success:
                print("⏳ Пауза 10 секунд...")
                time.sleep(10)
                processed_links.add(node["link"])
        else:
            print(f"⏩ Пропуск (уже скачано): {node['link']}")
    
    # Обходим детей в любом случае
    if "children" in node:
        for child in node["children"]:
            traverse_and_download(child, output_folder, processed_links)

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Файл {INPUT_FILE} не найден.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    processed_links = load_processed_links()
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        traverse_and_download(item, OUTPUT_DIR, processed_links)
    
    print("🏁 Все ссылки обработаны.")

if __name__ == "__main__":
    main()
