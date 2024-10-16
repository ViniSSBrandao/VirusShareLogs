#!/bin/bash

# Registrar o tempo de início em milissegundos
inicio=$(date +%s%3N)

# Diretório onde os arquivos estão localizados
diretorio_origem="./Untreated_logs/"

# Diretório onde os arquivos serão organizados
diretorio_destino="./sample_classification"

# Arquivo de log para registrar a pasta de destino de cada arquivo
arquivo_log="registro_destino.csv"

# Verifica se o diretório destino existe, se não, cria
mkdir -p "$diretorio_destino"
echo "Diretório destino '$diretorio_destino' verificado ou criado."

# Inicializa o arquivo de log
echo "Arquivo,MIME_type,Pasta de Destino" > "$arquivo_log"
echo "Arquivo de log '$arquivo_log' criado."

# Contagem de arquivos processados
contador=0

# Total de arquivos a processar
total_arquivos=$(find "$diretorio_origem" -type f | wc -l)
echo "Total de arquivos a processar: $total_arquivos"

# Loop para processar cada arquivo no diretório de origem
find "$diretorio_origem" -type f | while read arquivo; do
    # Incrementa contador
    ((contador++))

    # Exibe progresso
    echo "Processando arquivo $contador de $total_arquivos: $arquivo"

    # Obtém a assinatura do arquivo (MIME_type)
    assinatura=$(file --mime-type -b "$arquivo")
    echo "Assinatura detectada: $assinatura"

    # Cria um nome de diretório baseado na assinatura do arquivo
    subdir=$(echo $assinatura | tr '/' '_')

    # Cria o diretório se ele não existir
    if [ ! -d "$diretorio_destino/$subdir" ]; then
        mkdir -p "$diretorio_destino/$subdir"
        echo "Diretório criado: $diretorio_destino/$subdir"
    fi

    # Move o arquivo para o diretório correspondente
    mv "$arquivo" "$diretorio_destino/$subdir/"
    echo "Arquivo movido para $diretorio_destino/$subdir/"

    # Registra a pasta de destino no arquivo de log
    echo "$(basename "$arquivo"),$assinatura,$diretorio_destino/$subdir" >> "$arquivo_log"
done

echo "Organização de arquivos por assinatura concluída."

# Registrar o tempo de término em milissegundos
fim=$(date +%s%3N)

# Calcular e exibir a duração do script em milissegundos
duracao=$((fim - inicio))
echo "Tempo de execução do script: $duracao milissegundos."
