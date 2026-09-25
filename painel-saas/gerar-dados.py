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
    "hextech": {
        "kit_custo_essencia": 3,
        "bau": {"nome": "Baú Hextech", "img": "painel-saas/img/wiki/Hextech_Crafting_Chest.png"},
        "chave": {"nome": "Chave Hextech", "img": "painel-saas/img/wiki/Hextech_Crafting_Key.png"},
        "nota": "O Kit Hextech (1 baú + 1 chave) custa Essência Mítica. Use a chave para abrir o baú. Cosmético repetido vira fragmentos."
    },
    "promocao": {"fragmentos": 13, "nota": "Ao subir de cargo, P.P., Pontos Míticos e destaque voltam ao início e o membro recebe 13 Fragmentos."},
    "subir_maestria": {"moedas": 50, "essencia": 1},
    "penalidade": {"pp": -10},
    "bot": {"nome": "Bot L.S.P. UT", "img": "image/server_br.gif"},
    "erro": {"img": "image/notConnected.png"}
}

W = "painel-saas/img/wiki/"  # imagens da wiki do League of Legends (wiki.leagueoflegends.com)
C = "painel-saas/midia/cd/"     # arquivos do cliente do LoL, via CommunityDragon (raw.communitydragon.org)


def cos(id, nome, tipo, raridade, img=None, preco=None, **extra):
    c = {"id": id, "nome": nome, "tipo": tipo, "raridade": raridade, "preco": preco}
    if img:
        c["img"] = img
    c.update(extra)
    return c


def evo(*estagios):
    """Linha de evolução: cada nível da Forja troca o visual para o próximo estágio."""
    return [{"nome": n, "img": i} for n, i in estagios]


def evo_aura(nome, img):
    """Emote de campeão que ganha aura na Forja: sem aura, azul, vermelha, roxa e dourada."""
    auras = [("", None), (" com Aura Azul", "azul"), (" com Aura Vermelha", "vermelha"),
             (" com Aura Roxa", "roxa"), (" com Aura Dourada", "dourada")]
    return [dict({"nome": nome + sufixo, "img": img}, **({"aura": a} if a else {})) for sufixo, a in auras]


def evo_borda(*estagios):
    return [{"nome": n, "estilo": e} for n, e in estagios]


cosmeticos = [
    # Temas: fundo do painel e do perfil. Comprados com Moedas.
    cos("tema-oficial", "Tema Oficial", "tema", "comum", "image/background.png", 0),
    cos("tema-demacia", "Tema Demacia", "tema", "comum", C + "tema_demacia.jpg", 400),
    cos("tema-piltover", "Tema Piltover", "tema", "comum", C + "tema_piltover.jpg", 400),
    cos("tema-freljord", "Tema Freljord", "tema", "comum", C + "tema_freljord.jpg", 400),
    cos("tema-ionia", "Tema Ionia", "tema", "epica", "painel-saas/img/ionia.jpg", 600),
    cos("tema-noxus", "Tema Noxus", "tema", "epica", C + "tema_noxus.jpg", 600),
    cos("tema-zaun", "Tema Zaun", "tema", "epica", C + "tema_zaun.jpg", 600),
    cos("tema-sentina", "Tema Águas de Sentina", "tema", "lendaria", "image/back.png", 900),
    cos("tema-shurima", "Tema Shurima", "tema", "lendaria", C + "tema_shurima.jpg", 900),
    cos("tema-targon", "Tema Targon", "tema", "mitica", C + "tema_targon.jpg"),
    cos("tema-sombras", "Tema Ilhas das Sombras", "tema", "mitica", C + "tema_sombras.jpg"),

    # Bordas animadas em volta da foto (CSS). A Borda Arcana evolui na Forja.
    cos("borda-arcana", "Borda Arcana", "borda", "epica", evolucoes=evo_borda(
        ("Borda Arcana: Aço", "aco"), ("Borda Arcana: Pulso", "pulso"), ("Borda Arcana: Hextech", "hextech"),
        ("Borda Arcana: Vazio", "vazio"), ("Borda Arcana: Prisma", "prisma"))),
    cos("borda-aco", "Borda de Aço", "borda", "comum", preco=200, estilo="aco"),
    cos("borda-poro", "Borda Poro", "borda", "comum", preco=250, estilo="poro"),
    cos("borda-hextech", "Borda Hextech", "borda", "epica", estilo="hextech"),
    cos("borda-pulso", "Borda Pulso Arcano", "borda", "epica", estilo="pulso"),
    cos("borda-chama", "Borda Chama de Noxus", "borda", "lendaria", estilo="chama"),
    cos("borda-sakura", "Borda Florescer Espiritual", "borda", "lendaria", estilo="sakura"),
    cos("borda-vazio", "Borda do Vazio", "borda", "mitica", estilo="vazio"),
    cos("borda-prisma", "Borda Prisma Estelar", "borda", "ultimate", estilo="prisma"),

    # Ícones de perfil (medalhão na foto)
    cos("icone-poro", "Ícone Poro", "icone", "comum", preco=250, evolucoes=evo(
        ("Ícone Poro Iniciante", C + "icon_3521.jpg"), ("Ícone Poro Cavalheiro", C + "icon_744.jpg"),
        ("Ícone Poro Máquina de Combate", C + "icon_743.jpg"), ("Ícone Poro Fliperama", C + "icon_2094.jpg"),
        ("Ícone Poro Gamer", C + "icon_4226.jpg"))),
    cos("icone-realeza", "Ícone Realeza Poro", "icone", "lendaria", evolucoes=evo(
        ("Ícone Poro Sakura", C + "icon_1626.jpg"), ("Ícone Poro Pirata", C + "icon_3493.jpg"),
        ("Ícone Poro Barão", C + "icon_3233.jpg"), ("Ícone Rei Poro", C + "icon_1441.jpg"),
        ("Ícone Rainha Poro", C + "icon_3901.jpg"))),
    cos("icone-poro-classico", "Ícone Poro do PoroMaster", "icone", "comum", "assets/users/02.png", 200),
    cos("icone-poro-rena", "Ícone Poro Rena", "icone", "comum", C + "icon_3232.jpg", 250),
    cos("icone-piltover", "Ícone de Piltover", "icone", "comum", C + "icon_1448.jpg", 300),
    cos("icone-zaun", "Ícone de Zaun", "icone", "comum", C + "icon_1449.jpg", 300),
    cos("icone-rosa", "Ícone Brasão da Rosa", "icone", "comum", W + "Crest_Of_The_Rose_profileicon.jpg", 300),
    cos("icone-academia", "Ícone Academia de Batalha", "icone", "comum", W + "Battle_Academia_profileicon.png", 300),
    cos("icone-porofissional", "Ícone Porofissional", "icone", "epica", C + "icon_4149.jpg"),
    cos("icone-dj-poro", "Ícone DJ Poro", "icone", "epica", C + "icon_5710.jpg"),
    cos("icone-poro-estelar", "Ícone Poro Guardião Estelar", "icone", "epica", C + "icon_1446.jpg"),
    cos("icone-vazio", "Ícone do Vazio", "icone", "epica", C + "icon_3369.jpg"),
    cos("icone-aspectos", "Ícone Convergência dos Aspectos", "icone", "epica", W + "Aspects_Converge_profileicon.jpg"),
    cos("icone-heartsteel", "Ícone HEARTSTEEL", "icone", "epica", W + "HEARTSTEEL_Brand_profileicon.jpg"),
    cos("icone-poronauta", "Ícone Poronauta", "icone", "lendaria", C + "icon_4081.jpg"),
    cos("icone-poro-chamas", "Ícone Poro em Chamas", "icone", "lendaria", C + "icon_3872.jpg"),
    cos("icone-lucian", "Ícone Lucian Velho Oeste", "icone", "lendaria", W + "High_Noon_Lucian_Mythic_Chroma_profileicon.jpg"),
    cos("icone-mf", "Ícone Miss Fortune MVP", "icone", "lendaria", W + "MVP_T1_Miss_Fortune_Signature_profileicon.jpg"),
    cos("icone-poro-negro", "Ícone Poro Estrela Negra", "icone", "mitica", C + "icon_1447.jpg"),
    cos("icone-teclado", "Ícone Poro Rei do Teclado", "icone", "mitica", C + "icon_5755.jpg"),
    cos("icone-riven", "Ícone Riven Alvorecer", "icone", "mitica", W + "Dawnbringer_Riven_Mythic_Chroma_profileicon.jpg"),
    cos("icone-zed", "Ícone Zed Matador de Galáxias", "icone", "mitica", W + "Galaxy_Slayer_Zed_Mythic_Chroma_profileicon.jpg"),
    cos("icone-maestria", "Ícone Maestria 7", "icone", "mitica", B + "Rank_7.png"),
    cos("icone-veigar", "Ícone Veigar Chefão Final", "icone", "ultimate", W + "Final_Boss_Veigar_Mythic_Chroma_profileicon.jpg"),
    cos("icone-urf", "Ícone Imperador Urf", "icone", "ultimate", B + "Imperador.png"),

    # Sentinelas: aparecem na vitrine do perfil
    cos("sent-poro", "Sentinela Poro", "sentinela", "comum", preco=300, evolucoes=evo(
        ("Sentinela Poro", C + "ward_33.png"), ("Sentinela Poro Cavalheiro", C + "ward_35.png"),
        ("Sentinela Poro Máquina de Combate", C + "ward_36.png"), ("Sentinela Poro Fliperama", C + "ward_85.png"),
        ("Sentinela Poro Fã de Games", C + "ward_252.png"))),
    cos("sent-el-poro", "Sentinela El Poro", "sentinela", "comum", C + "ward_58.png", 350),
    cos("sent-astronauta", "Sentinela Poro Astronauta", "sentinela", "epica", C + "ward_34.png"),
    cos("sent-vamporo", "Sentinela Vamporo", "sentinela", "epica", C + "ward_70.png"),
    cos("sent-submundo", "Sentinela Poro do Submundo", "sentinela", "epica", C + "ward_38.png"),
    cos("sent-estelar", "Sentinela Guardiã Estelar", "sentinela", "lendaria", C + "ward_63.png"),
    cos("sent-dragao", "Sentinela Poro Matador de Dragões", "sentinela", "lendaria", C + "ward_37.png"),
    cos("sent-rainha", "Sentinela Rainha Poro", "sentinela", "mitica", C + "ward_123.png"),
    cos("sent-durandal", "Sentinela Durandal da Academia", "sentinela", "ultimate", C + "ward_136.png"),

    # Emotes: ao lado do nome e na biografia (:codigo:). Os raros são animados.
    cos("emote-poro", "Emote Poro", "emote", "comum", preco=100, codigo="poro", anim="flutuar", evolucoes=evo(
        ("Emote Poro da Paz", C + "emote_1498.png"), ("Emote Poro Bochechudo", C + "emote_1499.png"),
        ("Emote Poro Dorminhoco", C + "emote_3173.png"), ("Emote Andando de Poro", C + "emote_3210.png"),
        ("Emote Poropido", C + "emote_3126.png"))),
    cos("emote-gg", "Emote GG <3", "emote", "comum", C + "emote_3124.png", 120, codigo="gg"),
    cos("emote-flex", "Emote Pose de Força", "emote", "comum", W + "Big_Flex_Emote.png", 150, codigo="flex", evolucoes=evo_aura("Emote Pose de Força", W + "Big_Flex_Emote.png")),
    cos("emote-espiada", "Emote Só uma Espiada", "emote", "comum", W + "Just_A_Peek_Emote.png", 150, codigo="espiada"),
    cos("emote-trabalho", "Emote De Volta ao Trabalho", "emote", "lendaria", W + "Back_To_Business_Emote.png", codigo="trabalho", anim="pulsar"),
    # Mordekaiser de elo: as auras vêm da própria arte do jogo (emotes "2019 - Etapa 2")
    cos("emote-morde", "Emote Mordekaiser", "emote", "comum", preco=200, codigo="morde", evolucoes=evo(
        ("Emote Mordekaiser de Ferro", C + "emote_3248.png"), ("Emote Mordekaiser de Diamante", C + "emote_3253.png"),
        ("Emote Mordekaiser Grão-Mestre", C + "emote_3255.png"), ("Emote Mordekaiser Mestre", C + "emote_3254.png"),
        ("Emote Mordekaiser Desafiante", C + "emote_3256.png"))),
    cos("emote-brinde", "Emote Um Brinde", "emote", "comum", W + "Cheers_Dears_Emote.png", 200, codigo="brinde"),
    cos("emote-carinho", "Emote Carinho no Poro", "emote", "comum", C + "emote_5009.png", 150, codigo="carinho"),
    cos("emote-infusao", "Emote Infusão de Poro", "emote", "epica", C + "emote_4551.png", codigo="infusao", anim="flutuar"),
    cos("emote-revigorado", "Emote Poro Revigorado", "emote", "epica", C + "emote_4956.png", codigo="revigorado", anim="pular"),
    cos("emote-emoteemo", "Emote Emoteemo", "emote", "epica", C + "emote_3212.png", codigo="emoteemo", anim="pular", evolucoes=evo_aura("Emote Emoteemo", C + "emote_3212.png")),
    cos("emote-petala", "Emote Leve como Pétala", "emote", "epica", W + "Light_As_A_Petal_Emote.png", codigo="petala", anim="flutuar"),
    cos("emote-comigo", "Emote Fica Comigo", "emote", "epica", W + "Be_With_Me_Emote.png", codigo="fica_comigo", anim="pulsar"),
    cos("emote-espectral", "Emote Poro Espectral", "emote", "lendaria", C + "emote_5124.png", codigo="espectral", anim="balancar"),
    cos("emote-vamporo", "Emote Vamporo", "emote", "lendaria", C + "emote_3106.png", codigo="vamporo", anim="balancar"),
    cos("emote-guma", "Emote Deusa Guma", "emote", "lendaria", W + "Guma-Goddess_Emote.png", codigo="guma", anim="pulsar", evolucoes=evo_aura("Emote Deusa Guma", W + "Guma-Goddess_Emote.png")),
    cos("emote-bolinho", "Emote Bolinho do Teemo", "emote", "mitica", C + "emote_3797.png", codigo="bolinho_teemo", anim="girar")
]


def inv(*pares):
    return [{"item": i, "nivel": n} for i, n in pares]


def membro(id, nome, acesso, cargo, pp, pm, destaque, carteira, contrib, desde,
           foto=None, tags=(), conta=None, penalidade=False, inventario=None, equipado=None,
           materiais=(0, 0), bio=""):
    m = {"id": id, "nome": nome, "acesso": acesso, "cargo": cargo, "tags": list(tags),
         "pp": pp, "pm": pm, "destaque": destaque, "penalidade": penalidade,
         "carteira": dict(zip(["moedas", "essencia", "fragmentos", "estelares"], carteira)),
         "inventario": inventario or inv(("tema-oficial", 1)),
         "equipado": equipado or {"tema": "tema-oficial"},
         "materiais": {"baus": materiais[0], "chaves": materiais[1]},
         "bio": bio, "contrib": contrib, "desde": desde}
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
               inventario=inv(("tema-oficial", 1), ("tema-sentina", 3), ("tema-ionia", 1), ("icone-poro", 4), ("icone-urf", 1), ("icone-riven", 1), ("emote-flex", 2), ("emote-guma", 4),
                               ("emote-poro", 2), ("emote-gg", 1), ("borda-chama", 1), ("borda-arcana", 3), ("sent-rainha", 1), ("sent-poro", 3)),
               equipado={"tema": "tema-sentina", "icone": "icone-urf", "emote": "emote-guma", "borda": "borda-arcana", "sentinela": "sent-poro"},
               materiais=(2, 2), bio="Dev do PoroMaster desde 2022 :poro: Atualizo o ModSkin toda noite de patch. Bug? Manda no Discord :gg:"),
        membro("m2", "Bruch", "Admin", "Dev", None, 55, 2, [610, 3, 12, 2],
               [10, 8, 12, 14, 11, 15, 13, 12], "2022-01-20", tags=["Qualificador"],
               inventario=inv(("tema-oficial", 1), ("icone-poro", 1)),
               equipado={"tema": "tema-oficial", "icone": "icone-poro"}),
        membro("m3", "Jake", "Admin", "Mod", 84, 41, 3, [480, 2, 9, 3],
               [6, 9, 7, 11, 8, 6, 10, 12], "2022-02-03", foto="image/Profile/04.png", tags=["Corretor"], conta="u2",
               inventario=inv(("tema-oficial", 1), ("tema-ionia", 2), ("icone-rosa", 2), ("emote-trabalho", 1), ("emote-morde", 3), ("borda-hextech", 1), ("sent-vamporo", 1)),
               equipado={"tema": "tema-ionia", "icone": "icone-rosa", "emote": "emote-trabalho", "borda": "borda-hextech", "sentinela": "sent-vamporo"},
               materiais=(1, 0), bio="Moderador. Corrijo texto torto :trabalho:"),
        membro("m4", "Finger", "Membro", "Suporte", 67, 23, 1, [320, 1, 6, 0],
               [4, 6, 5, 7, 8, 6, 7, 9], "2022-02-11"),
        membro("m5", "Kawai Foxxy", "Membro", "Suporte", 58, 30, 1, [290, 2, 4, 1],
               [3, 5, 5, 6, 4, 7, 6, 7], "2022-03-01", tags=["Designer"],
               inventario=inv(("tema-oficial", 1)), equipado={"tema": "tema-oficial"}),
        membro("m6", "Khyago", "Membro", "Tester", 100, 64, 3, [410, 4, 11, 3],
               [9, 7, 11, 8, 12, 10, 13, 14], "2022-02-24", foto="image/Profile/03.png", conta="u3",
               inventario=inv(("tema-oficial", 1), ("icone-maestria", 1), ("emote-espiada", 1), ("borda-pulso", 1), ("sent-astronauta", 2)),
               equipado={"tema": "tema-oficial", "icone": "icone-maestria", "emote": "emote-espiada", "borda": "borda-pulso", "sentinela": "sent-astronauta"},
               materiais=(1, 1), bio="Tester caçador de bugs :espiada: 100 P.P. e contando."),
        membro("m7", "TaikunX3", "Membro", "Tester", 27, 12, 0, [90, 0, 2, 0],
               [3, 4, 2, 5, 1, 2, 0, 3], "2022-05-09", foto="image/Profile/02.png", penalidade=True),
        membro("m8", "imnotChinna", "Membro", "Tester", 76, 90, 2, [880, 5, 8, 4],
               [2, 12, 3, 4, 15, 3, 5, 13], "2022-04-18", foto="image/Profile/05.png", tags=["Parceiro"],
               inventario=inv(("tema-oficial", 1)), equipado={"tema": "tema-oficial"}),
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
