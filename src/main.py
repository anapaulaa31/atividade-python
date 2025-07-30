from app.text_inspector import TextInspector

def main() -> None:
    """
    Executa a inspeção do texto utilizando a classe TextInspector.
    """
    caminho = "texto.txt"  # Caminho do arquivo de texto
    inspector = TextInspector(caminho)

    print("=== Palavras que começam com 'a' ===")
    print(inspector.palavras_comecam_com('a'))

    print("\n=== Palavras que contêm 'e' ===")
    print(inspector.palavras_contem('e'))

    print("\n=== Texto com vírgulas substituídas por pontos ===")
    print(inspector.substituir_virgulas())

    print("\n=== Datas encontradas no texto ===")
    print(inspector.extrair_datas())

    print("\n=== Texto com informações sensíveis ocultadas ===")
    print(inspector.ocultar_info_sensivel())

    print("\n=== Total de palavras no texto ===")
    print(len(inspector))


if __name__ == "__main__":
    main()
