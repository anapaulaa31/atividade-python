import re
from typing import List

class TextInspector:
    """
    Classe responsável por ler, inspecionar e manipular o conteúdo de um arquivo de texto
    utilizando expressões regulares. Oferece funções como extração de palavras, substituição
    de vírgulas, reconhecimento de datas e ocultação de informações sensíveis como e-mails,
    CPFs e telefones.
    """

    def __init__(self, filepath: str):
        """
        Inicializa a classe com o caminho do arquivo e carrega o conteúdo do texto.

        :param filepath: Caminho para o arquivo .txt que será inspecionado.
        """
        self.filepath = filepath
        self.text = self._read_file()

    def _read_file(self) -> str:
        """
        Lê o conteúdo do arquivo de texto e retorna como uma string.

        :return: Conteúdo completo do arquivo.
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            return file.read()

    def palavras_comecam_com(self, letra: str) -> List[str]:
        """
        Retorna todas as palavras do texto que começam com uma letra específica.

        :param letra: Letra inicial a ser procurada.
        :return: Lista de palavras encontradas.
        """
        return re.findall(rf'\b{letra}\w*', self.text, re.IGNORECASE)

    def palavras_contem(self, letra: str) -> List[str]:
        """
        Retorna todas as palavras que contêm uma determinada letra.

        :param letra: Letra a ser procurada em qualquer posição da palavra.
        :return: Lista de palavras que contêm a letra.
        """
        return re.findall(rf'\b\w*{letra}\w*\b', self.text, re.IGNORECASE)

    def substituir_virgulas(self) -> str:
        """
        Substitui todas as vírgulas no texto por pontos.

        :return: Texto modificado com pontos no lugar das vírgulas.
        """
        return self.text.replace(',', '.')

    def extrair_datas(self) -> List[str]:
        """
        Extrai datas que estejam nos formatos dd/mm/aaaa ou dd-mm-aaaa.

        :return: Lista de strings contendo as datas encontradas.
        """
        return re.findall(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b', self.text)

    def ocultar_info_sensivel(self) -> str:
        """
        Substitui dados sensíveis (e-mails, CPFs e telefones) por marcadores seguros.

        :return: Texto com as informações sensíveis ocultadas.
        """
        texto = self.text
        texto = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', '[EMAIL_OCULTO]', texto)
        texto = re.sub(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b', '[CPF_OCULTO]', texto)
        texto = re.sub(r'\b\d{2}\s?\d{4,5}-\d{4}\b', '[TELEFONE_OCULTO]', texto)
        return texto

    def __len__(self) -> int:
        """
        Retorna o número total de palavras encontradas no texto.

        :return: Quantidade de palavras.
        """
        return len(re.findall(r'\b\w+\b', self.text))
