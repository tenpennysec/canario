# canario

# Script de Download de Áudio com yt-dlp

Este é um script Python simples para fazer o download de áudios de vídeos da internet usando o `yt-dlp`. Ele permite baixar o áudio de um link, convertê-lo para o formato MP3 e, se desejado, manter o vídeo original.

## Funcionalidades

- Baixa o áudio do link fornecido.
- Converte o áudio para o formato MP3 com qualidade de 192kbps.
- Possibilidade de manter o vídeo após o download com a flag `-k` (opcional).

## Pré-requisitos

Antes de rodar o script, certifique-se de que você tenha as dependências necessárias instaladas:

1. **Python** (versão 3.6 ou superior)
2. **yt-dlp** (um fork mais atualizado do `youtube-dl`)
3. **FFmpeg** (para conversão de áudio)

Você pode instalar essas dependências com os seguintes comandos:

### Instalando yt-dlp

```bash
pip install yt-dlp
```

### Instalando o FFmpeg

#### No Ubuntu/Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

#### No macOS (via Homebrew)

```bash
brew install ffmpeg
```

Ou, se preferir, você pode [baixar o FFmpeg manualmente](https://ffmpeg.org/download.html) para o seu sistema operacional.

## Como usar

1. Clone ou faça o download deste repositório para o seu sistema:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Execute o script com o comando:

    ```bash
    python canario.py <link-do-video>
    ```

    Onde `<link-do-video>` é o link do vídeo do qual você deseja baixar o áudio.

### Exemplo de uso

#### Baixar apenas o áudio

```bash
python canario.py https://www.youtube.com/watch?v=ID_DO_VIDEO
```

#### Baixar o áudio e manter o vídeo

Para baixar o áudio e manter o vídeo, você pode usar a flag `-k`:

```bash
python canario.py https://www.youtube.com/watch?v=ID_DO_VIDEO -k
```

Se você não passar a flag `-k`, o vídeo será automaticamente removido após o download do áudio.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
