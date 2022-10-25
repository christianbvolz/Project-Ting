from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    txt = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    if len(instance) == 0:
        instance.enqueue(data)
        print(data)
    else:
        for instance_data in instance._data:
            if path_file != instance_data["nome_do_arquivo"]:
                instance.enqueue(data)
                print(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
