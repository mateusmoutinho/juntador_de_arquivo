



#----------------------------------------Funcoes-------------------------------------------------------

remover_comentarios = lambda x: True if x[0] != "#" else False

remover_quebra_de_linha = lambda x: x.replace("\n","")

remover_espacos = lambda x : x.strip()

remover_itens_vazios = lambda x: True if x != "" else False

verificar_se_existe_extensao = lambda x: True if x.find(".lawtex") != -1 else False

add_extensao_se_nao_existir = lambda x:  x + ".lawtex" if verificar_se_existe_extensao(x) == False else x 

verificar_se_e_para_adicionar_extensao = lambda x:  True if "add extensao" in x  else False

remover_add_extensao_da_lista = lambda x: True if x != "add extensao" else False
#----------------------------------------------------------------------------------------------------

arquivo_config = open("exec/config","r")

config = arquivo_config.readlines()

config = list(filter(remover_comentarios,config))

config = list(map(remover_quebra_de_linha,config))

config = list(map(remover_espacos,config))


config = list(filter(remover_itens_vazios,config))



if verificar_se_e_para_adicionar_extensao(config):
   config = list(filter(remover_add_extensao_da_lista,config))
   config = list(map(add_extensao_se_nao_existir,config))




print(config)