"""Gera painel-saas/colecoes.json: coleções grandes montadas a partir dos dados do cliente do LoL.

- Linhas Poro: um único Ícone Poro com todos os ícones de Poro, uma Sentinela Poro com todas as
  sentinelas de Poro e um Emote Poro com todos os emotes de Poro.
- Outros tipos de ícone: Regiões de Runeterra e times do CBLoL.
- Sentinelas e emotes avulsos para completar a vitrine do Mercado.
- Recompensas de ranqueada: emotes e ícones de cada temporada, de Ferro a Desafiante. Não são
  vendidos: cada estágio é liberado pelo elo mítico do membro (campo "elo" de cada estágio).

Rode com: python3 painel-saas/gerar-colecoes.py  (precisa de acesso a raw.communitydragon.org)
Depois rode gerar-dados.py, que junta as coleções ao data.json.
"""
import json
import os
import re
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
G = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global"
MIDIA = os.path.join(AQUI, "midia", "colecoes")
REL = "painel-saas/midia/colecoes/"
TIERS = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Esmeralda", "Diamante", "Mestre", "Grão-Mestre", "Desafiante"]
TIER_RX = "(" + "|".join(TIERS) + ")"


def baixar_json(caminho):
    out = subprocess.run(["curl", "-s", "-f", "-m", "120", G + caminho], capture_output=True, check=True)
    return json.loads(out.stdout)


def asset(caminho):
    return G + "/default/" + caminho.replace("/lol-game-data/assets/", "").lower()


def baixar(url, nome):
    os.makedirs(MIDIA, exist_ok=True)
    destino = os.path.join(MIDIA, nome)
    if not os.path.exists(destino):
        subprocess.run(["curl", "-s", "-f", "-m", "120", "-o", destino, url], check=True)
    return REL + nome


def main():
    icones = {x["id"]: x for x in baixar_json("/pt_br/v1/summoner-icons.json")}
    emotes = {x["id"]: x for x in baixar_json("/pt_br/v1/summoner-emotes.json")}
    sentinelas = {x["id"]: x for x in baixar_json("/pt_br/v1/ward-skins.json")}

    def img_icone(i):
        return baixar(f"{G}/default/v1/profile-icons/{i}.jpg", f"icon_{i}.jpg")

    def img_emote(i):
        return baixar(asset(emotes[i]["inventoryIcon"]), f"emote_{i}.png")

    def img_sent(i):
        return baixar(asset(sentinelas[i]["wardImagePath"]), f"ward_{i}.png")

    cos = []

    # --- Poro: uma linha única por tipo, com todos os Poros ---
    fora = re.compile(r"Croma|Bolão|do Verão (?!CBLoL)|Merch|Sejuani|Acolhedor - (?!Meio)|Jogadores")
    poros, vistos = [], set()
    for i in sorted(icones):
        t = icones[i]["title"]
        if re.search(r"\bporos?\b|poronauta|porofissional", t, re.I) and not fora.search(t) and t not in vistos:
            vistos.add(t)
            poros.append(i)
    poros.remove(3521); poros.remove(4226)
    poros = [3521] + poros + [4226]            # começa no Poro Iniciante e termina no Poro Gamer
    cos.append({"id": "icone-poro", "nome": "Ícone Poro", "tipo": "icone", "raridade": "comum", "preco": 250, "custo_fixo": 2,
                "evolucoes": [{"nome": icones[i]["title"], "img": img_icone(i)} for i in poros]})
    ws = [i for i in sorted(sentinelas) if re.search(r"poro", sentinelas[i]["name"], re.I)]
    ws.remove(33); ws.remove(252)
    ws = [33] + ws + [252]                     # Sentinela Poro ... Poro Fã de Games
    cos.append({"id": "sent-poro", "nome": "Sentinela Poro", "tipo": "sentinela", "raridade": "comum", "preco": 300, "custo_fixo": 3,
                "evolucoes": [{"nome": sentinelas[i]["name"], "img": img_sent(i)} for i in ws]})
    es, vistos = [], set()
    for i in sorted(emotes):
        n = emotes[i]["name"].strip()
        if re.search(r"poro", n, re.I) and n.lower() not in vistos:
            vistos.add(n.lower())
            es.append(i)
    es.remove(1498)
    es = [1498] + es                           # começa no Poro da Paz
    cos.append({"id": "emote-poro", "nome": "Emote Poro", "tipo": "emote", "raridade": "comum", "preco": 100, "custo_fixo": 3,
                "codigo": "poro", "anim": "flutuar",
                "evolucoes": [{"nome": "Emote " + emotes[i]["name"].strip(), "img": img_emote(i)} for i in es]})

    # --- Outros tipos de ícone ---
    regioes = [1594, 3368, 3556, 1448, 1449, 3382, 3555, 3551, 3554, 3369]
    cos.append({"id": "icone-regioes", "nome": "Ícone Regiões de Runeterra", "tipo": "icone", "raridade": "epica", "preco": None, "custo_fixo": 3,
                "evolucoes": [{"nome": icones[i]["title"], "img": img_icone(i)} for i in regioes]})
    cblol = [674, 675, 676, 677, 678, 679, 680, 681, 4064, 5398]
    cos.append({"id": "icone-cblol", "nome": "Ícone CBLoL", "tipo": "icone", "raridade": "lendaria", "preco": None, "custo_fixo": 2,
                "evolucoes": [{"nome": icones[i]["title"], "img": img_icone(i)} for i in cblol]})

    # --- Sentinelas e emotes avulsos (completam a vitrine) ---
    for i, rar, preco in [(1, "comum", 250), (8, "comum", 300), (43, "epica", None), (98, "epica", None), (128, "lendaria", None), (171, "mitica", None)]:
        if i in sentinelas:
            cos.append({"id": f"sent-{i}", "nome": sentinelas[i]["name"], "tipo": "sentinela", "raridade": rar, "preco": preco, "img": img_sent(i)})
    extras = [x for x in sorted(emotes) if re.search(r"Amumu|Blitzcrank|Yuumi|Gragas|Bardo", emotes[x]["name"] + emotes[x]["inventoryIcon"])
              and "_FPO_" not in emotes[x]["inventoryIcon"]][:4]
    for i, (rar, preco) in zip(extras, [("comum", 150), ("comum", 200), ("epica", None), ("lendaria", None)]):
        cos.append({"id": f"emote-{i}", "nome": "Emote " + emotes[i]["name"].strip(), "tipo": "emote", "raridade": rar, "preco": preco,
                    "codigo": re.sub(r"[^a-z0-9]+", "_", emotes[i]["name"].strip().lower()).strip("_")[:20] or f"e{i}", "img": img_emote(i)})

    # --- Ultimates: linhas das skins Ultimate do LoL ---
    for cid, nome, ids in [("icone-udyr", "Ícone Udyr Guardião Espiritual", [549, 551, 550, 552, 5491, 5492, 5493, 5494, 5495]),
                           ("icone-dj-sona", "Ícone DJ Sona", [4286, 778, 779, 780]),
                           ("icone-samira", "Ícone Samira Soul Fighter", [5905, 5914, 5929])]:
        cos.append({"id": cid, "nome": nome, "tipo": "icone", "raridade": "ultimate", "preco": None, "custo_fixo": 3,
                    "evolucoes": [{"nome": icones[i]["title"], "img": img_icone(i)} for i in ids]})
    cos.append({"id": "sent-elementalista", "nome": "Sentinela Elementalista", "tipo": "sentinela", "raridade": "ultimate", "preco": None, "img": img_sent(69)})

    # --- Recompensas de ranqueada ---
    def temporadas(fonte, chave, filtro):
        grupos = {}
        for i in sorted(fonte):
            n = fonte[i].get(chave, "")
            m = re.search(TIER_RX, n)
            if m and filtro(n):
                grupos.setdefault(re.sub(TIER_RX, "#", n).strip(), {})[m.group(1)] = i
        return {k: v for k, v in grupos.items() if len(v) >= 9}

    ems = temporadas(emotes, "name", lambda n: re.search(r"^(\d{4}|Temporada \d{4})", n) and "Croma" not in n)
    ics = temporadas(icones, "title", lambda n: re.search(r"(Solo/Duo|Ano da Temporada|Ranqueada-5)", n) and "Croma" not in n)
    for grupo, por_tier in sorted(ems.items()):
        nome = grupo.replace(" – #", "").replace(" - #", "").replace("#", "").strip(" –-")
        cid = "rank-emote-" + re.sub(r"[^0-9a-z]+", "-", nome.lower()).strip("-")
        cos.append({"id": cid, "nome": f"Emote Ranqueada {nome}", "tipo": "emote", "raridade": "lendaria", "preco": None, "ranqueada": True,
                    "codigo": "rank" + re.sub(r"\D", "", nome), "evolucoes": [{"nome": f"Emote Ranqueada {nome}: {t}", "elo": t, "img": img_emote(por_tier[t])} for t in TIERS if t in por_tier]})
    for grupo, por_tier in sorted(ics.items()):
        nome = re.sub(r"\s*[–-]?\s*Ícone\s*#\s*(Solo/Duo)?", "", grupo).replace("#", "").strip(" –-")
        cid = "rank-icone-" + re.sub(r"[^0-9a-z]+", "-", nome.lower()).strip("-")
        cos.append({"id": cid, "nome": f"Ícone Ranqueada {nome}", "tipo": "icone", "raridade": "lendaria", "preco": None, "ranqueada": True,
                    "evolucoes": [{"nome": f"Ícone Ranqueada {nome}: {t}", "elo": t, "img": img_icone(por_tier[t])} for t in TIERS if t in por_tier]})

    with open(os.path.join(AQUI, "colecoes.json"), "w", encoding="utf-8") as f:
        json.dump({"cosmeticos": cos}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    for c in cos:
        print(f"{c['id']:40} {c['nome'][:50]:50} {len(c.get('evolucoes', [])) or 1} estágios")


if __name__ == "__main__":
    main()
