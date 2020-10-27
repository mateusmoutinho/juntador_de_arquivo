def retira_elementos_inuteis(lista):
    remover_comentarios = lambda x: True if x[0] != "#" else False
