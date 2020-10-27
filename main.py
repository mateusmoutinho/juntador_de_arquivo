
#----------------------------------------Funcoes lambda-------------------------------------------------------


remover_quebra_de_linha = lambda x: x.replace("\n","")

remover_espacos = lambda x : x.strip()

verificar_se_existe_extensao = lambda x: True if x.find(".lawtex") != -1 else False

add_extensao_se_nao_existir = lambda x:  x + ".lawtex" if verificar_se_existe_extensao(x) == False else x 

verificar_se_e_para_adicionar_extensao = lambda x:  True if "add extensao" in x  else False

remover_add_extensao_da_lista = lambda x: True if x != "add extensao" else False
#----------------------------------------------------------------------------------------------------

def remover_comentarios(lista):
    remove = lambda x:  True if x[0] != "#" else False
    return list(filter(remove,lista))




arquivo_config = open("exec/config","r")

config = arquivo_config.readlines()

r = remover_comentarios(config)
print(r)


