import os
import shutil
from typing import Dict, List

def criar_pastas(diretorio: str) -> Dict[str, List[str]]:
    """Cria pastas para organizar arquivos e retorna um dicionário com extensões."""
    pastas: Dict[str, List[str]] = {
        'planilhas': ['.xls', '.xlsx', '.csv'],
        'documentos': ['.doc', '.docx', '.txt', '.pdf'],
        'imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'arquivos_compactados': ['.zip', '.rar', '.7z']
    }
    
    for pasta in pastas.keys():
        caminho_pasta = os.path.join(diretorio, pasta)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
    
    return pastas

def organizar_arquivos(diretorio: str) -> None:
    """Organiza arquivos por extensão em subpastas."""
    try:
        pastas: Dict[str, List[str]] = criar_pastas(diretorio)
        arquivos: List[str] = os.listdir(diretorio)
        
        for arquivo in arquivos:
            caminho_arquivo: str = os.path.join(diretorio, arquivo)
            
            if os.path.isfile(caminho_arquivo):
                nome, extensao = os.path.splitext(arquivo)
                extensao = extensao.lower()
                
                movido: bool = False
                for pasta, extensoes in pastas.items():
                    if extensao in extensoes:
                        destino: str = os.path.join(diretorio, pasta, arquivo)
                        if not os.path.exists(destino):
                            shutil.move(caminho_arquivo, destino)
                        else:
                            print(f"Arquivo {arquivo} já existe na pasta de destino")
                        movido = True
                        break
                
                if not movido:
                    print(f"Extensão {extensao} não categorizada para o arquivo {arquivo}")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    organizar_arquivos('.')