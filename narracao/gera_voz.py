import asyncio, json, os, edge_tts

VOZ = "pt-BR-AntonioNeural"
pasta = os.path.dirname(os.path.abspath(__file__))
saida = os.path.join(pasta, "voz")
os.makedirs(saida, exist_ok=True)
roteiro = json.load(open(os.path.join(pasta, "roteiro.json"), encoding="utf-8"))


async def main():
    for trecho in roteiro:
        arq = os.path.join(saida, trecho["id"] + ".mp3")
        fala = edge_tts.Communicate(trecho["texto"], VOZ, rate="-8%", pitch="-3Hz")
        await fala.save(arq)
        print("ok", arq)


asyncio.run(main())
