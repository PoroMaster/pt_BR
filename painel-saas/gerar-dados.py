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
        "min": 0, "max": 100, "inicial": 30, "alerta_abaixo_de": 30,
        "nota": "Vale para todos, menos os Devs. Todo mundo entra com 30 P.P. Em 100 o membro pode subir de cargo; se cair para 0, é demitido da staff."
    },
    "maestrias": [
        {"nome": "Sem Maestria", "min": 0, "img": B + "Rank_0.png"},
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
        "abrir_varios": [5, 10],
        "peso_pack": 0.25,
        "bonus": [
            {"id": "essencia", "nome": "Essência Mítica", "chance": 10, "min": 1, "max": 3},
            {"id": "kit", "nome": "Baú + Chave", "chance": 8, "min": 1, "max": 1}
        ],
        "nota": "O Kit Hextech (1 baú + 1 chave) custa Essência Mítica. Use a chave para abrir o baú, um por vez ou vários de uma vez. Cosmético repetido vira fragmentos. Itens dos packs temáticos também podem sair, com um quarto da chance normal da raridade. Cada baú ainda pode dar um bônus: Essência Mítica (10%) ou outro Baú com Chave (8%)."
    },
    "promocao": {"fragmentos": 13, "nota": "Ao subir de cargo, P.P., Pontos Míticos e destaque voltam ao início e o membro recebe 13 Fragmentos."},
    "subir_maestria": {"moedas": 50, "essencia": 1},
    "penalidade": {"pp": -10},
    "bot": {"nome": "Bot L.S.P. UT", "img": "image/server_br.gif"},
    "erro": {"img": "image/notConnected.png"}
}

W = "painel-saas/img/wiki/"  # imagens da wiki do League of Legends (wiki.leagueoflegends.com)
R = "painel-saas/midia/regiao/"  # arte oficial das regiões de Runeterra (League Displays)
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
    cos("tema-demacia", "Tema Demacia", "tema", "comum", R + "tema_demacia.jpg", 400),
    cos("tema-piltover", "Tema Piltover", "tema", "comum", R + "tema_piltover.jpg", 400),
    cos("tema-freljord", "Tema Freljord", "tema", "comum", R + "tema_freljord.jpg", 400),
    cos("tema-ionia", "Tema Ionia", "tema", "epica", "painel-saas/img/ionia.jpg", 600),
    cos("tema-noxus", "Tema Noxus", "tema", "epica", R + "tema_noxus.jpg", 600),
    cos("tema-zaun", "Tema Zaun", "tema", "epica", R + "tema_zaun.jpg", 600),
    cos("tema-sentina", "Tema Águas de Sentina", "tema", "lendaria", "image/back.png", 900),
    cos("tema-shurima", "Tema Shurima", "tema", "lendaria", R + "tema_shurima.jpg", 900),
    cos("tema-targon", "Tema Targon", "tema", "mitica", R + "tema_targon.jpg"),
    cos("tema-sombras", "Tema Ilhas das Sombras", "tema", "mitica", R + "tema_sombras.jpg"),
    cos("tema-bandopolis", "Tema Bandópolis", "tema", "comum", R + "tema_bandopolis.jpg", 400),
    cos("tema-ixtal", "Tema Ixtal", "tema", "epica", R + "tema_ixtal.jpg", 600),
    cos("tema-ionia-mistica", "Tema Ionia Mística", "tema", "lendaria", R + "tema_ionia2.jpg", 900),
    cos("tema-vazio", "Tema O Vazio", "tema", "ultimate", R + "tema_vazio.jpg"),

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
    cos("borda-ouro", "Borda de Ouro", "borda", "comum", preco=300, estilo="ouro"),
    cos("borda-gelo", "Borda Gelo de Freljord", "borda", "comum", preco=350, estilo="gelo"),
    cos("borda-zaun", "Borda Química de Zaun", "borda", "epica", estilo="zaun"),
    cos("borda-sol", "Borda Solari de Targon", "borda", "lendaria", estilo="sol"),
    cos("borda-nevoa", "Borda Névoa Negra", "borda", "mitica", estilo="nevoa"),
    cos("borda-estelar", "Borda Guardiã Estelar", "borda", "ultimate", estilo="estelar"),

    # Ícones de perfil (medalhão na foto)
    cos("icone-poro-classico", "Ícone Poro do PoroMaster", "icone", "comum", "assets/users/02.png", 200),
    cos("icone-rosa", "Ícone Brasão da Rosa", "icone", "comum", W + "Crest_Of_The_Rose_profileicon.jpg", 300),
    cos("icone-academia", "Ícone Academia de Batalha", "icone", "comum", W + "Battle_Academia_profileicon.png", 300),
    cos("icone-aspectos", "Ícone Convergência dos Aspectos", "icone", "epica", W + "Aspects_Converge_profileicon.jpg"),
    cos("icone-heartsteel", "Ícone HEARTSTEEL", "icone", "epica", W + "HEARTSTEEL_Brand_profileicon.jpg"),
    cos("icone-lucian", "Ícone Lucian Velho Oeste", "icone", "lendaria", W + "High_Noon_Lucian_Mythic_Chroma_profileicon.jpg"),
    cos("icone-mf", "Ícone Miss Fortune MVP", "icone", "lendaria", W + "MVP_T1_Miss_Fortune_Signature_profileicon.jpg"),
    cos("icone-riven", "Ícone Riven Alvorecer", "icone", "mitica", W + "Dawnbringer_Riven_Mythic_Chroma_profileicon.jpg"),
    cos("icone-zed", "Ícone Zed Matador de Galáxias", "icone", "mitica", W + "Galaxy_Slayer_Zed_Mythic_Chroma_profileicon.jpg"),
    cos("icone-maestria", "Ícone Maestria 7", "icone", "mitica", B + "Rank_7.png"),
    cos("icone-veigar", "Ícone Veigar Chefão Final", "icone", "mitica", W + "Final_Boss_Veigar_Mythic_Chroma_profileicon.jpg"),
    cos("icone-urf", "Ícone Imperador Urf", "icone", "mitica", B + "Imperador.png"),

    # Sentinelas: aparecem na vitrine do perfil
    cos("sent-durandal", "Sentinela Durandal da Academia", "sentinela", "lendaria", C + "ward_136.png"),
    cos("sent-olho-dragao", "Sentinela Olho do Dragão", "sentinela", "comum", C + "ward_76.png", 350),
    cos("sent-arcane", "Sentinela Arcane", "sentinela", "epica", C + "ward_218.png"),
    cos("sent-pulsefire", "Sentinela Pulsefire", "sentinela", "epica", C + "ward_77.png"),
    cos("sent-lua-sangrenta", "Sentinela Lua Sangrenta", "sentinela", "lendaria", C + "ward_132.png"),
    cos("sent-florescer", "Sentinela Florescer Espiritual", "sentinela", "lendaria", C + "ward_230.png"),
    cos("sent-kanmei", "Sentinela Kanmei", "sentinela", "mitica", C + "ward_200.png"),
    cos("sent-akana", "Sentinela Akana", "sentinela", "epica", C + "ward_201.png"),

    # Emotes: ao lado do nome e na biografia (:codigo:). Os raros são animados.
    cos("emote-gg", "Emote GG <3", "emote", "comum", C + "emote_3124.png", 120, codigo="gg"),
    cos("emote-flex", "Emote Pose de Força", "emote", "comum", W + "Big_Flex_Emote.png", 150, codigo="flex", evolucoes=evo_aura("Emote Pose de Força", W + "Big_Flex_Emote.png")),
    cos("emote-espiada", "Emote Só uma Espiada", "emote", "comum", W + "Just_A_Peek_Emote.png", 150, codigo="espiada"),
    cos("emote-trabalho", "Emote De Volta ao Trabalho", "emote", "lendaria", W + "Back_To_Business_Emote.png", codigo="trabalho", anim="pulsar"),
    # Mordekaiser de elo: as auras vêm da própria arte do jogo (emotes "2019 - Etapa 2")
    cos("emote-brinde", "Emote Um Brinde", "emote", "comum", W + "Cheers_Dears_Emote.png", 200, codigo="brinde"),
    cos("emote-emoteemo", "Emote Emoteemo", "emote", "epica", C + "emote_3212.png", codigo="emoteemo", anim="pular", evolucoes=evo_aura("Emote Emoteemo", C + "emote_3212.png")),
    cos("emote-petala", "Emote Leve como Pétala", "emote", "epica", W + "Light_As_A_Petal_Emote.png", codigo="petala", anim="flutuar"),
    cos("emote-comigo", "Emote Fica Comigo", "emote", "epica", W + "Be_With_Me_Emote.png", codigo="fica_comigo", anim="pulsar"),
    cos("emote-guma", "Emote Deusa Guma", "emote", "lendaria", W + "Guma-Goddess_Emote.png", codigo="guma", anim="pulsar", evolucoes=evo_aura("Emote Deusa Guma", W + "Guma-Goddess_Emote.png")),
    # Pack Guardiãs Estelares: itens exclusivos, só vêm no pack
    cos("icone-guardias", "Ícone Guardiãs Estelares", "icone", "epica", pack="guardias", custo_fixo=4, evolucoes=evo(
        ("Ícone Marca da Guardiã", C + "icon_1381.jpg"), ("Ícone Lux Guardiã Estelar", C + "icon_5863.jpg"),
        ("Ícone Jinx Guardiã Estelar", C + "icon_5864.jpg"), ("Ícone Janna Guardiã Estelar", C + "icon_5865.jpg"),
        ("Ícone Lulu Guardiã Estelar", C + "icon_5866.jpg"), ("Ícone Poppy Guardiã Estelar", C + "icon_5867.jpg"),
        ("Ícone Seraphine Guardiã Estelar", C + "icon_5868.jpg"), ("Ícone Orianna Guardiã Estelar", C + "icon_5869.jpg"),
        ("Ícone Senna Guardiã Estelar", C + "icon_5873.jpg"), ("Ícone Kai'Sa Guardiã Estelar", C + "icon_5419.jpg"),
        ("Ícone Ekko Guardião Estelar", C + "icon_5420.jpg"), ("Ícone Sona Guardiã Estelar", C + "icon_5421.jpg"),
        ("Ícone Nilah Guardiã Estelar", C + "icon_5422.jpg"), ("Ícone Emblema das Guardiãs", C + "icon_5872.jpg"))),
    cos("emote-guardias", "Emote Guardiãs Estelares", "emote", "lendaria", pack="guardias", custo_fixo=2, codigo="guardias", anim="flutuar", evolucoes=evo(
        ("Emote Kai'Sa: Iti, que fofinho!", C + "emote_3931.png"), ("Emote Ekko: Peguei você!", C + "emote_3932.png"),
        ("Emote Sona: Que gracinha!", C + "emote_3933.png"), ("Emote Nilah: Quanta alegria!", C + "emote_3934.png"),
        ("Emote Akali: Quem vem agora?", C + "emote_3939.png"), ("Emote Taliyah: Só pedrada!", C + "emote_3940.png"),
        ("Emote Rell: Mais uma coisinha...", C + "emote_3941.png"), ("Emote Quinn: Perfeição", C + "emote_3942.png"),
        ("Emote Morgana: Você não me escapa!", C + "emote_3943.png"))),
    cos("sent-guardias-linha", "Sentinela Guardiãs Estelares", "sentinela", "lendaria", pack="guardias", evolucoes=evo(
        ("Sentinela Guardiã Estelar", C + "ward_63.png"), ("Sentinela Guardiãs Estelares 2019", C + "ward_188.png"),
        ("Sentinela Guardiãs Estelares 2022", C + "ward_227.png"))),
    cos("tema-guardias", "Tema Academia das Guardiãs", "tema", "mitica", R + "tema_guardias.jpg", pack="guardias"),
    cos("emote-bolinho", "Emote Bolinho do Teemo", "emote", "mitica", C + "emote_3797.png", codigo="bolinho_teemo", anim="girar")
]


packs = [
    {"id": "guardias", "nome": "Pack Guardiãs Estelares", "capa": R + "tema_guardias.jpg",
     "descricao": "Coleção temática com linhas de evolução que passam por todas as Guardiãs Estelares.",
     "moeda": "essencia", "preco": 8,
     "itens": ["icone-guardias", "emote-guardias", "sent-guardias-linha", "tema-guardias", "borda-estelar"]},
    {"id": "poro", "nome": "Pack Poro", "capa": C + "icon_4226.jpg",
     "descricao": "Tudo de Poro com desconto: as três linhas de evolução do Poro, a borda e o ícone do PoroMaster.",
     "moeda": "moedas", "preco": 700,
     "itens": ["icone-poro", "sent-poro", "emote-poro", "borda-poro", "icone-poro-classico"]}
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
    "cor": "#c8a24a", "logo": "assets/users/02.png",
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
    # Reset: os cinco perfis originais do painel L.S.P. UT (fantome-fantom.js, jan/2023), como eram:
    # 30 pontos (Rank 1), sem elo, sem destaque, carteira zerada. Devs são isentos de P.P.
    "membros": [
        membro("m1", "Luckey", "Dono", "Dev", None, 0, 0, [0, 0, 0, 0], [0] * 8, "2023-01-09",
               foto="image/Profile/01.png", conta="u1"),
        membro("m2", "Jake", "Admin", "Mod", 30, 0, 0, [0, 0, 0, 0], [0] * 8, "2023-01-09",
               foto="image/Profile/04.png", conta="u2"),
        membro("m3", "imnotChinna", "Membro", "Mod", 30, 0, 0, [0, 0, 0, 0], [0] * 8, "2023-01-09",
               foto="image/Profile/05.png"),
        membro("m4", "Khyago", "Membro", "Tester", 30, 0, 0, [0, 0, 0, 0], [0] * 8, "2023-01-09",
               foto="image/Profile/03.png", conta="u3"),
        membro("m5", "TaikunX3", "Membro", "Tester", 30, 0, 0, [0, 0, 0, 0], [0] * 8, "2023-01-09",
               foto="image/Profile/02.png", tags=["Parceiro"], bio="Parceria: TAIKUNDROME")
    ],
    "envios": [],
    "atividade": [],
    # Downloads do ModSkin, como no painel original (painel.html): versão estável e as betas experimentais
    # que os testers baixam antes de todo mundo. "status": teste (em teste agora), aprovada ou reprovada.
    "modskin": {
        "estavel": {"versao": "6.4.0", "patch": "12.10", "quando": "2022-05-25T20:00:00",
                    "links": [{"nome": "ModSkin PoroMaster", "url": "https://github.com/PoroMaster/Latests/releases/download/pt_BR/PoroMaster.zip"},
                              {"nome": "ModSkin Lite", "url": "https://github.com/poromaster/Latests/releases/download/pt_BR/PoroMaster_Lite.zip", "indisponivel": True}]},
        "beta_url": "https://github.com/modskinbr/Testers/releases/download/Betas/BETA.zip",
        "betas": [{"id": f"#{n:04d}", "status": "teste" if n == 103 else ("reprovada" if n in (95, 97) else "aprovada")} for n in range(103, 93, -1)]
    },
    "novidades": [
        {"quando": "2026-09-24T12:00:00", "titulo": "ModSkin 13.6.1 liberado para testers", "texto": "Download antecipado disponível no painel. Confiram as skins novas do patch."},
        {"quando": "2026-09-22T09:00:00", "titulo": "Evento: Semana de caça aos bugs", "texto": "Todo bug confirmado nesta semana vale 1 Fragmento Estelar."},
        {"quando": "2026-09-19T18:00:00", "titulo": "Novo tema na loja: Águas de Sentina", "texto": "Personalize o fundo do painel. Custa 900 Moedas."}
    ]
}

# Toda pessoa da staff tem uma conta de login. As três primeiras são fixas (u1, u2, u3);
# os demais membros ganham uma conta própria com e-mail no domínio da comunidade.
contas = [
    {"id": "u1", "nome": "Luckey", "email": "luckey@poromaster.dev", "foto": "image/Profile/01.png"},
    {"id": "u2", "nome": "Jake", "email": "jake@poromaster.dev", "foto": "image/Profile/04.png"},
    {"id": "u3", "nome": "Khyago", "email": "khyago@poromaster.dev", "foto": "image/Profile/03.png"},
]
for com, dominio in ((poromaster, "poromaster.dev"),):
    for m in com["membros"]:
        if m.get("conta"):
            continue
        cid = "u-" + m["id"]
        slug = "".join(ch for ch in m["nome"].lower() if ch.isalnum())
        contas.append({"id": cid, "nome": m["nome"], "email": f"{slug}@{dominio}", "foto": m.get("foto")})
        m["conta"] = cid

dados = {
    "_nota": "Banco de dados de exemplo. As regras seguem o painel L.S.P. UT original; pontos, carteiras e atividades são fictícios. Caminhos de imagem são relativos à raiz do repositório. Gerado por gerar-dados.py.",
    "contas": contas,
    "sistema": sistema,
    "cosmeticos": cosmeticos,
    "packs": packs,
    "comunidades": [poromaster]
}

# coleções geradas por gerar-colecoes.py (Poro, regiões, CBLoL, Ultimates e ranqueada)
colecoes = os.path.join(os.path.dirname(os.path.abspath(__file__)), "colecoes.json")
if os.path.exists(colecoes):
    with open(colecoes, encoding="utf-8") as f:
        novos = json.load(f)["cosmeticos"]
    ids_novos = {c["id"] for c in novos}
    dados["cosmeticos"] = [c for c in dados["cosmeticos"] if c["id"] not in ids_novos] + novos

# packs temáticos gerados por gerar-packs.py a partir dos dados do cliente do LoL
extra = os.path.join(os.path.dirname(os.path.abspath(__file__)), "packs.json")
if os.path.exists(extra):
    with open(extra, encoding="utf-8") as f:
        gerado = json.load(f)
    dados["packs"] += gerado["packs"]
    dados["cosmeticos"] += gerado["cosmeticos"]

saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
with open(saida, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("ok:", saida)
