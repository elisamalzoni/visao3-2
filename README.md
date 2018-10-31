# Projeto Visão Computacional 3-2 2018.2
### Elisa Malzoni

## Rodando o programa:

`pyhton busca_imagens termo --build-index --partial`

Onde `termo` é o palavra a ser buscada, a flag `--partial`, indica que o termo usado é somente uma parte da categoria, como por exemplo *'goldfish'* ao invés de *'goldfish, Carassius auratus'* e a flag `--build-index` cria um dicionário em um arquivo pickle que contém o nome da categoria como chave e as imagens da categoria como valores. Caso `--partial` esteja em uso outro arquivo é criado com os mesmos princípios, só neste caso haverá maior quantidade de chaves.

## Técnicas utilizadas
Para esse projeto foi utilizado uma rede neural pré-treinada (Imagenet), onde o modelo já está pronto.

Primeiro cada imagem do banco foi carregada e classificada de acordo com as 1000 categorias (`id_to_name.py`) e também foi calculada a confiança dessa classificação.

Após esses passos um dicionário foi criado com as categorias como chaves e as imagens pertecentes a categoria com suas confianças como valores.

Ao fazer a busca por um termo (chave do dicionário) as imagens da categoria são ordenadas por confiança decrescente. Assim é mostrada as 5 imagens com maior confiança.

## Organização do código
O código está dividido em 3 arquivos: dicionário com ids das caegorias para nomes da categoria, funções utilizadas no projeto, e o arquivo principal que faz uso do de funções.

As etapas descritas acima foram traduzidas em funções que são classificação (`mnetv2_input_from_image(img)`), criação do índice a partir do banco de onde serão buscadas as imagens (`create_in(path_folders)`), que cria os dicionário dos nomes com as imagens e salva em um arquivo, depois caso `--partial` esteja ativado o arquivo criado acima é utilizado para a criação de um segundo dicionário onde os nomes da categorias são divididos por `', '` (vígula espaço), assim com esses dicionários prontos é possível mostrar as 5 melhores imagens para aquele termo (`show_5(dici, termo)`).

As flags são avaliadas no arquivo `busca_imagens.py`, que chama as funções acima dependendo das flags e termo passado pelo terminal.

## Avaliação Crítica
Os termos buscados mostram imagens coerentes.
`python3 busca_imagens.py --partial backpack`
![backpack](./Figure_01.png)

A implementação da flag `--partial` não é completa, já que não é aceito qualquer rótulo que contenha a palavra e sim pela vígula espaço.

A implementação da flag `--build-index` também não é completa, uma vez que sempre todos os indíces são criados, e não somente os novos. 
