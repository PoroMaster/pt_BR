"""Gera painel-saas/data.json, o banco de dados de exemplo do protótipo.

As regras do sistema (reputação, maestrias, elos, destaques, raridades,
cargos e tags) seguem o painel L.S.P. UT original e o que o dono do
projeto lembrou. Pontos, carteiras, inventários e atividades são
fictícios. Rode com: python3 painel-saas/gerar-dados.py
"""
import json
import os

B = "image/banco_de_dados/"

sistema = {
    "reputacao": {
        "nome": "Pontos de Prestígio",
        "sigla": "P.P.",
        "icone": B + "Pontos_Prestigios.png",
        "min": 20, "max": 100, "inicial": 30, "alerta_abaixo_de": 30,
        "nota": "Vale para todos, menos os Devs. Em 100 o membro pode subir de cargo; em 20 é removido da staff."
    },
    "maestrias": [
        {"nome": "Sem Maestria", "min": 20, "img": B + "Rank_0.png"},
        {"nome": "Maestria 1", "min": 30, "img": B + "Rank_1.png"},
        {"nome": "Maestria 2", "min": 40, "img": B + "Rank_2.png"},
        {"nome": "Maestria 3", "min": 50, "img": B + "Rank_3.png"},
        {"nome": "Maestria 4", "min": 60, "img": B + "Rank_4.png"},
        {"nome": "Maestria 5", "min": 70, "img": B + "Rank_5.png"},
        {"nome": "Maestria 6", "min": 80, "img": B + "Rank_6.png"},
        {"nome": "Maestria 7", "min": 90, "img": B + "Rank_7.png"}
    ],
    "miticos": {
        "nome": "Pontos Míticos",
        "icone": B + "Pontos_Miticos.png",
        "max": 100,
        "nota": "Ganhos por ajuda voluntária ou grandiosa: divulgação, vídeos, eventos."
    },
    "elos": [
        {"nome": "Sem Elo", "min": 0, "img": B + "Rank_0.png"},
        {"nome": "Ferro", "min": 10, "img": B + "Ferro.png"},
        {"nome": "Bronze", "min": 20, "img": B + "Bronze.png"},
        {"nome": "Prata", "min": 30, "img": B + "Prata.png"},
        {"nome": "Ouro", "min": 40, "img": B + "Ouro.png"},
        {"nome": "Platina", "min": 50, "img": B + "Platina.png"},
        {"nome": "Diamante", "min": 60, "img": B + "Diamante.png"},
        {"nome": "Mestre", "min": 70, "img": "assets/logos/mestre.png"},
        {"nome": "Grão-Mestre", "min": 80, "img": B + "Grao_Mestre.png"},
        {"nome": "Desafiante", "min": 90, "img": B + "Desafiante.png"},
        {"nome": "Imperador Urf", "min": 100, "img": B + "Imperador.png"}
    ],
    "destaques": [
        {"nome": "Sem destaque", "cor": "Cinza", "img": B + "Destaque_0.png"},
        {"nome": "Destaque Azul", "cor": "Azul", "img": B + "Destaque_1.png"},
        {"nome": "Destaque Vermelho", "cor": "Vermelho", "img": B + "Destaque_2.png"},
        {"nome": "Destaque Roxo", "cor": "Roxo", "img": B + "Destaque_3.png"},
        {"nome": "Destaque Laranja", "cor": "Laranja", "img": B + "Destaque_4.png"}
    ],
    "imunidade": {"img": B + "Imunidade.png", "nota": "Quem tem destaque acima do Roxo fica imune a rebaixamento e perda de P.P."},
    "alerta": {"img": B + "Alerta.png", "nota": "Aparece com uma penalidade ou P.P. abaixo de 30, até a reputação subir de novo."},
    "cargos": [
        {"nome": "Tester", "img": B + "Tester.png"},
        {"nome": "Suporte", "img": B + "Supp.png"},
        {"nome": "Mod", "img": B + "Mod.png"},
        {"nome": "Dev", "img": B + "Dev.png"}
    ],
    "tags": [
        {"nome": "Designer", "img": B + "Designer.png", "nota": "Cria artes e ícones"},
        {"nome": "Parceiro", "img": B + "Parceiro.png", "nota": "Parceiro do projeto"},
        {"nome": "Booster", "img": "image/Booster.png", "nota": "Impulsiona o servidor"},
        {"nome": "Doador", "img": "image/Doador.png", "nota": "Apoia com doações"},
        {"nome": "Corretor", "img": "image/Corretor.png", "nota": "Corrige a ortografia"},
        {"nome": "Qualificador", "img": "image/Qualificador.png", "nota": "Avalia o desempenho de cada membro"}
    ],
    "moedas": {
        "moedas": {"nome": "Moedas", "img": B + "Moedas.png", "nota": "Compram cosméticos comuns e temas na loja."},
        "essencia": {"nome": "Essência Mítica", "img": B + "Essencia_Mitica.png", "nota": "Abre LootBoxes, que podem dar cosméticos raros."},
        "fragmentos": {"nome": "Fragmentos", "img": B + "Shards.png", "nota": "Sobem o nível de cosméticos Comuns e Épicos na Forja."},
        "estelares": {"nome": "Fragmentos Estelares", "img": B + "Star_Shards.png", "nota": "Sobem o nível de cosméticos Lendários ou acima. Vêm de eventos, bugs reportados e mérito dado pelo dono."}
    },
    "raridades": [
        {"id": "comum", "nome": "Comum", "cor": "Cinza", "img": B + "Destaque_0.png", "peso": 45, "frag": "fragmentos", "custo": 3, "duplicata": 5},
        {"id": "epica", "nome": "Épica", "cor": "Azul", "img": B + "Destaque_1.png", "peso": 30, "frag": "fragmentos", "custo": 5, "duplicata": 10},
        {"id": "lendaria", "nome": "Lendária", "cor": "Vermelha", "img": B + "Destaque_2.png", "peso": 15, "frag": "estelares", "custo": 2, "duplicata": 2},
        {"id": "mitica", "nome": "Mítica", "cor": "Roxa", "img": B + "Destaque_3.png", "peso": 8, "frag": "estelares", "custo": 3, "duplicata": 4},
        {"id": "ultimate", "nome": "Ultimate", "cor": "Laranja", "img": B + "Destaque_4.png", "peso": 2, "frag": "estelares", "custo": 5, "duplicata": 8}
    ],
    "forja": {"nivel_max": 5, "nota": "Custo para subir de nível = custo da raridade x nível atual."},
    "lootbox": {"custo_essencia": 3, "nota": "Roleta aleatória. Cosmético repetido vira fragmentos."},
    "promocao": {"fragmentos": 13, "nota": "Ao subir de cargo, P.P., Pontos Míticos e destaque voltam ao início e o membro recebe 13 Fragmentos."},
    "subir_maestria": {"moedas": 50, "essencia": 1},
    "penalidade": {"pp": -10},
    "bot": {"nome": "Bot L.S.P. UT", "img": "image/server_br.gif"},
    "erro": {"img": "image/notConnected.png"}
}

cosmeticos = [
    {"id": "tema-oficial", "nome": "Tema Oficial", "tipo": "tema", "raridade": "comum", "img": "image/background.png", "preco": 0},
    {"id": "tema-ionia", "nome": "Tema Ionia", "tipo": "tema", "raridade": "epica", "img": "image/back2.jpg", "preco": 600},
    {"id": "tema-sentina", "nome": "Tema Águas de Sentina", "tipo": "tema", "raridade": "lendaria", "img": "image/back.png", "preco": 900},
    {"id": "banner-classico", "nome": "Banner Cliente Clássico", "tipo": "banner", "raridade": "comum", "img": "assets/banner.png", "preco": 200},
    {"id": "banner-instalador", "nome": "Banner Instalador", "tipo": "banner", "raridade": "comum", "img": "assets/download_03.png", "preco": 150},
    {"id": "banner-colecao", "nome": "Banner Coleção", "tipo": "banner", "raridade": "comum", "img": "assets/sobre02.png", "preco": 150},
    {"id": "banner-feerica", "nome": "Banner Feérica", "tipo": "banner", "raridade": "epica", "img": "assets/download_01.png", "preco": None},
    {"id": "banner-fliperama", "nome": "Banner Fliperama", "tipo": "banner", "raridade": "epica", "img": "assets/download_02.png", "preco": None},
    {"id": "banner-guardia", "nome": "Banner Guardiã Estelar", "tipo": "banner", "raridade": "lendaria", "img": "assets/sobre01.png", "preco": None},
    {"id": "icone-poro", "nome": "Ícone Poro", "tipo": "icone", "raridade": "epica", "img": "assets/users/02.png", "preco": None},
    {"id": "icone-maestria", "nome": "Ícone Maestria 7", "tipo": "icone", "raridade": "mitica", "img": B + "Rank_7.png", "preco": None},
    {"id": "icone-urf", "nome": "Ícone Imperador Urf", "tipo": "icone", "raridade": "ultimate", "img": B + "Imperador.png", "preco": None}
]


def inv(*pares):
    return [{"item": i, "nivel": n} for i, n in pares]


def membro(id, nome, acesso, cargo, pp, pm, destaque, carteira, contrib, desde,
           foto=None, tags=(), conta=None, penalidade=False, inventario=None, equipado=None):
    m = {"id": id, "nome": nome, "acesso": acesso, "cargo": cargo, "tags": list(tags),
         "pp": pp, "pm": pm, "destaque": destaque, "penalidade": penalidade,
         "carteira": dict(zip(["moedas", "essencia", "fragmentos", "estelares"], carteira)),
         "inventario": inventario or inv(("tema-oficial", 1)),
         "equipado": equipado or {"tema": "tema-oficial"},
         "contrib": contrib, "desde": desde}
    if foto:
        m["foto"] = foto
    if conta:
        m["conta"] = conta
    return m


poromaster = {
    "id": "poromaster", "nome": "PoroMaster", "descricao": "Staff do ModSkin brasileiro",
    "plano": "pro", "cor": "#c8a24a", "logo": "assets/users/02.png",
    "regras": [
        {"id": "r1", "acao": "Verificação de campeão aprovada", "setor": "Testadores", "recompensa": {"pp": 2, "moedas": 20}},
        {"id": "r2", "acao": "Bug reportado e confirmado", "setor": "Testadores", "recompensa": {"pp": 3, "estelares": 1}},
        {"id": "r3", "acao": "Tarefa do dia concluída", "setor": "Testadores", "recompensa": {"pp": 1, "moedas": 10}},
        {"id": "r4", "acao": "Divulgação em rede social", "setor": "Academia", "recompensa": {"pm": 2, "moedas": 15}},
        {"id": "r5", "acao": "Vídeo mostrando o ModSkin", "setor": "Academia", "recompensa": {"pm": 5, "essencia": 1}},
        {"id": "r6", "acao": "Ajuda a usuário no suporte", "setor": "Federativa", "recompensa": {"pp": 1, "moedas": 10}},
        {"id": "r7", "acao": "Participação em evento", "setor": "Federativa", "recompensa": {"pm": 3, "estelares": 1}},
        {"id": "r8", "acao": "Mérito dado pelo dono", "setor": "Dono", "recompensa": {"estelares": 2, "essencia": 1}, "so_admin": True}
    ],
    "membros": [
        membro("m1", "Luckey", "Dono", "Dev", None, 72, 4, [1240, 7, 26, 9],
               [14, 18, 12, 22, 19, 24, 21, 27], "2022-01-15", foto="image/Profile/01.png", tags=["Booster"], conta="u1",
               inventario=inv(("tema-oficial", 1), ("tema-sentina", 3), ("tema-ionia", 1), ("banner-guardia", 2), ("banner-classico", 4), ("icone-poro", 4), ("icone-urf", 1)),
               equipado={"tema": "tema-sentina", "banner": "banner-guardia", "icone": "icone-urf"}),
        membro("m2", "Bruch", "Admin", "Dev", None, 55, 2, [610, 3, 12, 2],
               [10, 8, 12, 14, 11, 15, 13, 12], "2022-01-20", tags=["Qualificador"],
               inventario=inv(("tema-oficial", 1), ("banner-instalador", 2), ("icone-poro", 1)),
               equipado={"tema": "tema-oficial", "banner": "banner-instalador", "icone": "icone-poro"}),
        membro("m3", "Jake", "Admin", "Mod", 84, 41, 3, [480, 2, 9, 3],
               [6, 9, 7, 11, 8, 6, 10, 12], "2022-02-03", foto="image/Profile/04.png", tags=["Corretor"], conta="u2",
               inventario=inv(("tema-oficial", 1), ("tema-ionia", 2), ("banner-fliperama", 1)),
               equipado={"tema": "tema-ionia", "banner": "banner-fliperama"}),
        membro("m4", "Finger", "Membro", "Suporte", 67, 23, 1, [320, 1, 6, 0],
               [4, 6, 5, 7, 8, 6, 7, 9], "2022-02-11"),
        membro("m5", "Kawai Foxxy", "Membro", "Suporte", 58, 30, 1, [290, 2, 4, 1],
               [3, 5, 5, 6, 4, 7, 6, 7], "2022-03-01", tags=["Designer"],
               inventario=inv(("tema-oficial", 1), ("banner-colecao", 1)), equipado={"tema": "tema-oficial", "banner": "banner-colecao"}),
        membro("m6", "Khyago", "Membro", "Tester", 100, 64, 3, [410, 4, 11, 3],
               [9, 7, 11, 8, 12, 10, 13, 14], "2022-02-24", foto="image/Profile/03.png", conta="u3",
               inventario=inv(("tema-oficial", 1), ("banner-feerica", 2), ("icone-maestria", 1)),
               equipado={"tema": "tema-oficial", "banner": "banner-feerica", "icone": "icone-maestria"}),
        membro("m7", "TaikunX3", "Membro", "Tester", 27, 12, 0, [90, 0, 2, 0],
               [3, 4, 2, 5, 1, 2, 0, 3], "2022-05-09", foto="image/Profile/02.png", penalidade=True),
        membro("m8", "imnotChinna", "Membro", "Tester", 76, 90, 2, [880, 5, 8, 4],
               [2, 12, 3, 4, 15, 3, 5, 13], "2022-04-18", foto="image/Profile/05.png", tags=["Parceiro"],
               inventario=inv(("tema-oficial", 1), ("banner-classico", 1)), equipado={"tema": "tema-oficial", "banner": "banner-classico"}),
        membro("m9", "Hatcubinho", "Membro", "Comunidade", None, 15, 0, [150, 1, 0, 0],
               [0, 1, 2, 1, 2, 1, 2, 2], "2022-08-02", foto="assets/users/08.png", tags=["Doador"])
    ],
    "envios": [
        {"id": "e1", "membro": "m7", "regra": "r1", "detalhe": "Ahri, Espírito Florescente: cromas e VFX conferidos", "quando": "2026-09-24T14:10:00", "status": "pendente"},
        {"id": "e2", "membro": "m6", "regra": "r2", "detalhe": "Skin de Aphelios some ao trocar de croma no lobby", "quando": "2026-09-24T11:42:00", "status": "pendente"},
        {"id": "e3", "membro": "m8", "regra": "r5", "detalhe": "Vídeo \"Top 10 skins do patch\" com link para download", "quando": "2026-09-23T21:05:00", "status": "pendente"},
        {"id": "e4", "membro": "m5", "regra": "r6", "detalhe": "Resolveu erro de instalação de 3 usuários no Discord", "quando": "2026-09-23T18:30:00", "status": "pendente"},
        {"id": "e6", "membro": "m3", "regra": "r7", "detalhe": "Organizou a Semana de caça aos bugs", "quando": "2026-09-23T12:00:00", "status": "pendente"},
        {"id": "e5", "membro": "m4", "regra": "r4", "detalhe": "Post no grupo de LoL do Facebook", "quando": "2026-09-22T16:00:00", "status": "aprovado"}
    ],
    "atividade": [
        {"quando": "2026-09-24T09:15:00", "texto": "Khyago chegou a 100 P.P. e pode subir para Suporte"},
        {"quando": "2026-09-23T22:40:00", "texto": "TaikunX3 recebeu uma penalidade (-10 P.P.)"},
        {"quando": "2026-09-23T20:10:00", "texto": "Luckey aprimorou Tema Águas de Sentina para o nível 3"},
        {"quando": "2026-09-22T16:05:00", "texto": "Finger ganhou 2 Pontos Míticos por divulgação"}
    ],
    "novidades": [
        {"quando": "2026-09-24T12:00:00", "titulo": "ModSkin 13.6.1 liberado para testers", "texto": "Download antecipado disponível no painel. Confiram as skins novas do patch."},
        {"quando": "2026-09-22T09:00:00", "titulo": "Evento: Semana de caça aos bugs", "texto": "Todo bug confirmado nesta semana vale 1 Fragmento Estelar."},
        {"quando": "2026-09-19T18:00:00", "titulo": "Novo tema na loja: Águas de Sentina", "texto": "Personalize o fundo do painel. Custa 900 Moedas."}
    ]
}

tradutores = {
    "id": "tradutores", "nome": "Tradutores ModSkin", "descricao": "Equipe que traduz o site e o cliente",
    "plano": "gratis", "cor": "#2bb5a6",
    "regras": [
        {"id": "t1", "acao": "Página traduzida", "setor": "Tradução", "recompensa": {"pp": 3, "moedas": 30}},
        {"id": "t2", "acao": "Revisão de tradução", "setor": "Revisão", "recompensa": {"pp": 1, "moedas": 15}}
    ],
    "membros": [
        membro("n1", "Luckey", "Dono", "Dev", None, 20, 1, [300, 1, 3, 0],
               [2, 3, 1, 4, 2, 5, 3, 4], "2022-11-15", foto="image/Profile/01.png", conta="u1"),
        membro("n2", "Diogo Teixeira", "Membro", "Tester", 62, 18, 1, [240, 1, 2, 0],
               [2, 2, 3, 2, 4, 3, 3, 4], "2022-11-15", foto="assets/users/03.png", tags=["Corretor"]),
        membro("n3", "Selin", "Membro", "Tester", 35, 5, 0, [60, 0, 0, 0],
               [0, 1, 1, 2, 1, 2, 2, 3], "2022-12-01")
    ],
    "envios": [
        {"id": "f1", "membro": "n2", "regra": "t1", "detalhe": "FAQ traduzido para es_AR", "quando": "2026-09-24T10:00:00", "status": "pendente"}
    ],
    "atividade": [{"quando": "2026-09-24T10:00:00", "texto": "Diogo Teixeira enviou o FAQ em espanhol"}],
    "novidades": [{"quando": "2026-09-20T12:00:00", "titulo": "Faltam 4 páginas em turco", "texto": "Quem puder ajudar, pegue uma página no canal de tradução."}]
}

dados = {
    "_nota": "Banco de dados de exemplo. As regras seguem o painel L.S.P. UT original; pontos, carteiras e atividades são fictícios. Caminhos de imagem são relativos à raiz do repositório. Gerado por gerar-dados.py.",
    "contas": [
        {"id": "u1", "nome": "Luckey", "email": "luckey@poromaster.dev", "foto": "image/Profile/01.png"},
        {"id": "u2", "nome": "Jake", "email": "jake@poromaster.dev", "foto": "image/Profile/04.png"},
        {"id": "u3", "nome": "Khyago", "email": "khyago@poromaster.dev", "foto": "image/Profile/03.png"}
    ],
    "sistema": sistema,
    "cosmeticos": cosmeticos,
    "comunidades": [poromaster, tradutores]
}

saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
with open(saida, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("ok:", saida)
