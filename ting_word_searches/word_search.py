def exists_word(word, instance):
    lines = []
    for data in instance._data:
        for line, txt in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in txt.lower():
                lines.append({"linha": line + 1})
    if len(lines) == 0:
        return lines
    return [{
        "palavra": word,
        "arquivo": data["nome_do_arquivo"],
        "ocorrencias": lines,
    }]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
