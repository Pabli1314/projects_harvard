import re

def convertHTML(markdown_text):
    # Convertir encabezados
    markdown_text = re.sub(r'###### (.+)', r'<h6>\1</h6>', markdown_text)
    markdown_text = re.sub(r'##### (.+)', r'<h5>\1</h5>', markdown_text)
    markdown_text = re.sub(r'#### (.+)', r'<h4>\1</h4>', markdown_text)
    markdown_text = re.sub(r'### (.+)', r'<h3>\1</h3>', markdown_text)
    markdown_text = re.sub(r'## (.+)', r'<h2>\1</h2>', markdown_text)
    markdown_text = re.sub(r'# (.+)', r'<h1>\1</h1>', markdown_text)

    # Convertir texto en negrita y cursiva
    markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', markdown_text)
    markdown_text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', markdown_text)

    # Convertir enlaces
    markdown_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown_text)

    # Convertir listas desordenadas
    markdown_text = re.sub(r'^\* (.+)', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'(<li>.+</li>)', r'<ul>\1</ul>', markdown_text)

    # Convertir párrafos
    markdown_text = re.sub(r'\n\n+', r'</p><p>', markdown_text)
    markdown_text = re.sub(r'^(?!<h|<ul|<li|<p|<strong|<em)(.+)$', r'<p>\1</p>', markdown_text, flags=re.MULTILINE)

    return markdown_text


