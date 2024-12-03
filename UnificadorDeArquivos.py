import os
import sys
import time

def deletar_e_esperar(arquivo):
    # Verifica se o arquivo existe
    if os.path.exists(arquivo):
        try:
            os.remove(arquivo)
            print(f"\n🗑️  Arquivo {arquivo} deletado com sucesso.")
            print("⏳ Aguardando 5 segundos...")
            time.sleep(5)  # Espera 5 segundos
            print("▶️  Continuando com a criação do novo arquivo...\n")
        except Exception as e:
            print(f"❌ Erro ao deletar o arquivo: {e}")
            sys.exit(1)
    else:
        print(f"\n📝 Arquivo {arquivo} não existe. Continuando com a criação...")
        time.sleep(5)  # Espera 5 segundos mesmo se o arquivo não existir

def juntar_arquivos(diretorio, arquivo_saida):
    # Lista de arquivos e pastas a serem ignorados
    ignorar_arquivos = [
                        'UnificadorDeArquivos.py', 
                        'conteudo_unificado.txt',
                        'gysin_ia_20241027.log'
                        ]
    ignorar_pastas = [
                        'xxxxxxxxxxxxxxxxxxxxxxxx',
                        'build',
                        'lixo',
                        'venv',
                        '.venv', 
                        '__pycache__', 
                        '.git', 
                        'resources', 
                        'models', 
                        'gysin_ia.egg-info', 
                        'gysin_env', 
                        '.pytest_cache'
                    ]
    
     # Contador para arquivos processados
    arquivos_processados = 0

    try:
        # Primeiro deleta o arquivo existente e espera 5 segundos
        deletar_e_esperar(arquivo_saida)

        print("📂 Iniciando processo de unificação dos arquivos...\n")

        with open(arquivo_saida, 'w', encoding='utf-8') as saida:
            for raiz, pastas, arquivos in os.walk(diretorio):
                # Ignora as pastas especificadas
                pastas[:] = [p for p in pastas if p not in ignorar_pastas]
                
                for arquivo in arquivos:
                    # Ignora os arquivos especificados
                    if arquivo in ignorar_arquivos:
                        continue
                    
                    caminho_completo = os.path.join(raiz, arquivo)
                    
                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as f:
                            conteudo = f.read()
                            saida.write(f"// Conteúdo do arquivo: {caminho_completo}\n\n")
                            saida.write(conteudo)
                            saida.write("\n\n")
                            
                            # Mostra o progresso no terminal
                            arquivos_processados += 1
                            print(f"✅ Arquivo {arquivos_processados}: {caminho_completo}")
                            
                    except Exception as e:
                        print(f"❌ Erro ao ler o arquivo {caminho_completo}: {e}")

        print(f"\n✨ Processo concluído com sucesso!")
        print(f"📊 Total de arquivos processados: {arquivos_processados}")
        print(f"📄 O conteúdo foi unificado no arquivo: '{arquivo_saida}'")
    
    except Exception as e:
        print(f"❌ Ocorreu um erro durante o processo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    #diretorio = r'C:\Servidor\OneDrive\Projetos\mestre-dos-codigos'
    #arquivo_saida = r'C:\Servidor\OneDrive\Projetos\mestre-dos-codigos\UnificadorDeArquivos.txt'
    #diretorio = r'C:\Servidor\OneDrive\Ultilidades.py\gerenciador_de_senhasv2'
    #arquivo_saida = r'C:\Servidor\OneDrive\Ultilidades.py\gerenciador_de_senhasv2\UnificadorDeArquivos.txt'
    diretorio = r'C:\Servidor\OneDrive\Projetos\GysinIA'
    arquivo_saida = r'C:\Servidor\OneDrive\Projetos\GysinIA\UnificadorDeArquivos.txt'    
  
    
    juntar_arquivos(diretorio, arquivo_saida)