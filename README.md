# Image_generation

Olá!

Neste repositório se encontra um código capaz de ler textos e escrevê-los em imagens.
O texto escrito será quebrado em linhas, e essas linhas serão desenhadas numa série de imagens, caso necessário.

## Qual é o formato dessas imagens?
Essas imagens serão criadas num formato de postagem para Redes Sociais, bem no estilo de frases de auto-ajuda. É inspirado nos posts desses perfis:  [Perfil 1](https://www.instagram.com/segredosdauniversidade2.0/) (talvez não seja um exemplo muito bom, mas o que vale é a intenção 😄)

Também será desenhado um número em cada postagem, com o intuíto de identificá-la, sendo que esse número será gerado automaticamente, partindo do zero.

Quando se é gerada mais de uma imagem a partir da frase escrita, o número gerado será acompanhado de uma letra, indo de A a Z.

O algoritmo foi pensado para que cada arquivo de texto gerassem uma postagem, que pode ter uma ou mais imagens.

## Uso do código

 1. Clone este repositório para seu ambiente;
 2. Rode o arquivo `imgGenerate.py` uma primeira vez, para que os diretórios necessários sejam criados automaticamente;
 3. Feito isso, insira um  **arquivo na extensão .txt** no diretório `inputs/`;
 4. Após isso, basta rodar o arquivo `imgGenerate.py` novamente, que os resultados ficarão disponíveis no diretório `outputs/`!

## Especificações
 - Para rodar o código, é necessário ter instalado préviamente a biblioteca [Pillow](https://pillow.readthedocs.io/en/latest/installation.html);
 - A imagem tem um tamanho fixo de **500X500**;
 - A fonte usada nas imagens podem ser alteradas, colocando a fonte desejada no diretório `fonts/`. Após isso, você altera a variável `FONT_DIR` no arquivo `drawers/imageTextDrawer.py`, colocando o nome do arquivo da fonte que você inseriu anteriormente após o `./fonts/` que já está na variável;
 - **Obs:** O algorítmo foi projetado pensando no uso da fonte que já existe hoje, então outras fontes podem não funcionar como esperado;
 - A cor de fundo das imagens pode ser alterado, alterando o conteúdo da variável `IMAGE_BACKGROUND_COLOR` que se enconta no arquivo `drawers/imageTextDrawer.py`;
 - A cor das fonte usada nas imagens também pode ser alterada, colocando o valor em hexadecimal da cor desejada na variável `COLOR_FONT`, que se encontra no arquivo `drawers/imageTextDrawer.py`; 
##