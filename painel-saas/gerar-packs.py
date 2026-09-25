"""Gera painel-saas/packs.json: packs temáticos montados a partir dos dados do cliente do LoL.

Para cada temática de skins (Fliperama, Congregação das Bruxas...) o script procura nos dados
do jogo (CommunityDragon, em pt_BR) os ícones, emotes e sentinelas daquela temática e monta
linhas de evolução que passam pelos campeões. As imagens vão para painel-saas/midia/packs/.
A arte de cena usada como tema de alguns packs fica em painel-saas/midia/regiao/ (já reduzida).

Rode com: python3 painel-saas/gerar-packs.py  (precisa de acesso a raw.communitydragon.org)
Depois rode gerar-dados.py, que junta os packs ao data.json.
"""
import json
import os
import re
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
G = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global"
MIDIA = os.path.join(AQUI, "midia", "packs")
REL = "painel-saas/midia/packs/"

# id, nome em português, regex (nomes em inglês), cena para o tema (arquivo em midia/regiao ou None)
TEMATICAS = [
    ("fliperama", "Fliperama", r"\barcade\b", "tema_pack_fliperama.jpg"),
    ("congregacao", "Congregação das Bruxas", r"\bcoven\b", "tema_pack_congregacao.jpg"),
    ("florescer", "Florescer Espiritual", r"spirit ?blossom", None),
    ("academia", "Academia de Batalha", r"battle ?academ", None),
    ("lua-sangrenta", "Lua Sangrenta", r"blood ?moon", None),
    ("projeto", "PROJETO", r"\bproject\b", "tema_pack_projeto.jpg"),
    ("velho-oeste", "Velho Oeste", r"high ?noon", None),
    ("kda", "K/DA", r"\bk/?da\b", "tema_pack_kda.jpg"),
]
FORA = re.compile(r"chroma|border|frame|pass\b|event|token|merch|bundle|prestige points|mission|emblem", re.I)
MAX_ICONES, MAX_EMOTES = 10, 8


def baixar_json(caminho):
    out = subprocess.run(["curl", "-s", "-f", "-m", "120", G + caminho], capture_output=True, check=True)
    return json.loads(out.stdout)


def url_asset(caminho):
    return G + "/default/" + caminho.replace("/lol-game-data/assets/", "").lower()


def baixar(url, nome):
    os.makedirs(MIDIA, exist_ok=True)
    destino = os.path.join(MIDIA, nome)
    if not os.path.exists(destino):
        subprocess.run(["curl", "-s", "-f", "-m", "120", "-o", destino, url], check=True)
    return REL + nome


def main():
    icones_pt = {x["id"]: x for x in baixar_json("/pt_br/v1/summoner-icons.json")}
    icones_en = baixar_json("/default/v1/summoner-icons.json")
    emotes_pt = {x["id"]: x for x in baixar_json("/pt_br/v1/summoner-emotes.json")}
    emotes_en = baixar_json("/default/v1/summoner-emotes.json")
    sent_pt = {x["id"]: x for x in baixar_json("/pt_br/v1/ward-skins.json")}
    sent_en = baixar_json("/default/v1/ward-skins.json")

    packs, cosmeticos = [], []
    for pid, nome, rx, cena in TEMATICAS:
        r = re.compile(rx, re.I)
        ics, vistos = [], set()
        for x in sorted(icones_en, key=lambda x: x["id"]):
            t = x.get("title", "")
            if r.search(t) and not FORA.search(t) and x["id"] in icones_pt and t not in vistos:
                vistos.add(t)
                ics.append(x["id"])
        ems = [x["id"] for x in sorted(emotes_en, key=lambda x: x["id"])
               if r.search(x.get("name", "") + " " + x.get("inventoryIcon", "")) and x["id"] in emotes_pt
               and not re.search(r"_FPO_", x.get("inventoryIcon", ""))][:MAX_EMOTES]
        sts = [x["id"] for x in sorted(sent_en, key=lambda x: x["id"]) if r.search(x.get("name", "")) and x["id"] in sent_pt]
        ics = ics[:MAX_ICONES]

        itens = []
        if len(ics) >= 2:
            cid = f"icone-pack-{pid}"
            cosmeticos.append({"id": cid, "nome": f"Ícone {nome}", "tipo": "icone", "raridade": "epica", "preco": None,
                               "pack": pid, "custo_fixo": 4,
                               "evolucoes": [{"nome": icones_pt[i]["title"], "img": baixar(f"{G}/default/v1/profile-icons/{i}.jpg", f"icon_{i}.jpg")} for i in ics]})
            itens.append(cid)
        if len(ems) >= 2:
            cid = f"emote-pack-{pid}"
            cosmeticos.append({"id": cid, "nome": f"Emote {nome}", "tipo": "emote", "raridade": "lendaria", "preco": None,
                               "pack": pid, "custo_fixo": 2, "codigo": pid.replace("-", "_"), "anim": "flutuar",
                               "evolucoes": [{"nome": "Emote " + emotes_pt[i]["name"].strip(), "img": baixar(url_asset(emotes_pt[i]["inventoryIcon"]), f"emote_{i}.png")} for i in ems]})
            itens.append(cid)
        if sts:
            cid = f"sent-pack-{pid}"
            base = {"id": cid, "nome": f"Sentinela {nome}", "tipo": "sentinela", "raridade": "lendaria", "preco": None, "pack": pid}
            imgs = [{"nome": sent_pt[i]["name"], "img": baixar(url_asset(sent_pt[i]["wardImagePath"]), f"ward_{i}.png")} for i in sts]
            if len(imgs) >= 2:
                base.update(custo_fixo=2, evolucoes=imgs)
            else:
                base.update(nome=imgs[0]["nome"], img=imgs[0]["img"])
            cosmeticos.append(base)
            itens.append(cid)
        if cena and os.path.exists(os.path.join(AQUI, "midia", "regiao", cena)):
            cid = f"tema-pack-{pid}"
            cosmeticos.append({"id": cid, "nome": f"Tema {nome}", "tipo": "tema", "raridade": "mitica", "preco": None,
                               "pack": pid, "img": "painel-saas/midia/regiao/" + cena})
            itens.append(cid)
        capa = ("painel-saas/midia/regiao/" + cena) if cena else next(c for c in cosmeticos if c["id"] == itens[0])["evolucoes"][-1]["img"]
        packs.append({"id": pid, "nome": f"Pack {nome}", "capa": capa, "moeda": "essencia", "preco": 8,
                      "descricao": f"Coleção {nome}: linhas de evolução que passam pelos campeões da temática.",
                      "itens": itens})
        print(f"{nome}: {len(ics)} ícones, {len(ems)} emotes, {len(sts)} sentinelas, tema: {'sim' if cena else 'não'}")

    with open(os.path.join(AQUI, "packs.json"), "w", encoding="utf-8") as f:
        json.dump({"packs": packs, "cosmeticos": cosmeticos}, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
