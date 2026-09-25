"""Empacota as imagens pequenas do painel em painel-saas/atlas/*.json para publicar.

O link publicado aceita no máximo 255 arquivos, e o painel usa mais de 300 imagens. Este script
junta ícones, emotes, sentinelas e emblemas (tudo abaixo de LIMITE) em poucos arquivos JSON com
data: URIs. O index.html carrega esses pacotes ao abrir; sem eles, usa os arquivos soltos.
Temas (imagens grandes), vídeos e sons continuam como arquivos normais.

Rode com: python3 painel-saas/empacotar.py   (a pasta atlas/ fica fora do Git)
Imprime a lista de arquivos que precisam ser publicados junto com o index.html.
"""
import base64
import json
import mimetypes
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SAIDA = os.path.join(AQUI, "atlas")
LIMITE = 400 * 1024          # imagens menores que isto vão para o atlas
PARTE = 9 * 1024 * 1024      # tamanho máximo de cada arquivo de atlas


def imagens_usadas(dados):
    achadas = {"image/tester.ico"}

    def andar(o):
        if isinstance(o, dict):
            for v in o.values():
                andar(v)
        elif isinstance(o, list):
            for v in o:
                andar(v)
        elif isinstance(o, str) and o.rsplit(".", 1)[-1] in ("png", "jpg", "gif", "ico"):
            achadas.add(o)
    andar(dados)
    return achadas


def main():
    with open(os.path.join(AQUI, "data.json"), encoding="utf-8") as f:
        dados = json.load(f)
    temas = {c["img"] for c in dados["cosmeticos"] if c["tipo"] == "tema"} | {p["capa"] for p in dados["packs"]}
    usadas = sorted(imagens_usadas(dados))
    no_atlas = [p for p in usadas if p not in temas and os.path.getsize(os.path.join(RAIZ, p)) < LIMITE]
    soltos = [p for p in usadas if p not in no_atlas]

    os.makedirs(SAIDA, exist_ok=True)
    for f in os.listdir(SAIDA):
        os.remove(os.path.join(SAIDA, f))
    partes, atual, tam = [], {}, 0
    for p in no_atlas:
        tipo = mimetypes.guess_type(p)[0] or "image/png"
        with open(os.path.join(RAIZ, p), "rb") as f:
            uri = f"data:{tipo};base64," + base64.b64encode(f.read()).decode()
        if tam + len(uri) > PARTE and atual:
            partes.append(atual)
            atual, tam = {}, 0
        atual[p] = uri
        tam += len(uri)
    if atual:
        partes.append(atual)
    nomes = []
    for i, parte in enumerate(partes, 1):
        nome = f"atlas-{i}.json"
        with open(os.path.join(SAIDA, nome), "w") as f:
            json.dump(parte, f, separators=(",", ":"))
        nomes.append(nome)
    with open(os.path.join(SAIDA, "index.json"), "w") as f:
        json.dump(nomes, f)

    midia = []
    for pasta in ("painel-saas/midia/video", "painel-saas/midia/som"):
        midia += [pasta + "/" + f for f in sorted(os.listdir(os.path.join(RAIZ, pasta)))]
    publicar = ["painel-saas/data.json", "painel-saas/atlas/index.json"] + ["painel-saas/atlas/" + n for n in nomes] + soltos + midia
    print(f"{len(no_atlas)} imagens em {len(nomes)} atlas; {len(publicar)} arquivos para publicar")
    with open(os.path.join(SAIDA, "publicar.json"), "w") as f:
        json.dump(publicar, f, indent=0)


if __name__ == "__main__":
    main()
