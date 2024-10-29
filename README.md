# Projeto de Análise e Previsão de Movimentações no Mercado Financeiro

Este projeto tem como objetivo identificar possíveis movimentações futuras no mercado financeiro (como ações, Ibovespa, mini índice, criptomoedas e Forex), utilizando algoritmos de aprendizado de máquina. Através da análise dos preços de abertura, máxima, mínima e fechamento ao longo do tempo, bem como das variações e desvios padrão, o modelo desenvolvido avalia a probabilidade de o mercado se mover em uma direção específica e alcançar certos níveis de preço.

## Estrutura do Projeto

### 1. Coleta e Análise de Dados
Foram utilizados dados históricos dos preços de mercado para investigar tendências, volatilidade e oscilações diárias. Os principais parâmetros analisados incluem:

- **Preços de Abertura, Máxima, Mínima e Fechamento**: Observação das flutuações diárias para entender a direção do mercado.
- **Pontos e Totais de Pontos**: Monitoramento de ganhos e perdas diárias e acumuladas, fornecendo uma visão clara do desempenho geral.
- **Desvios Padrão**: Cálculo da volatilidade dos preços de fechamento para diferentes períodos, permitindo a análise de estabilidade e risco.
- **Razões Máxima/Mínima e Fechamento**: Indicadores da proximidade dos preços de fechamento em relação às máximas e mínimas diárias, o que auxilia na interpretação de padrões.

### 2. Modelagem e Treinamento
O modelo é treinado com os dados históricos para aprender padrões e oferecer previsões baseadas em probabilidades de movimentos futuros. O treinamento é ajustado para cada ativo ou mercado financeiro em questão.

### 3. Visualizações Gráficas
Foram gerados gráficos que representam as variáveis principais ao longo do tempo, destacando as tendências e oscilações. Essas visualizações oferecem uma interpretação rápida e intuitiva dos dados para facilitar a análise e a tomada de decisões.

## Outputs

### Market Prices Over Time
- **Descrição**: Este gráfico exibe as variações diárias dos preços de `OPEN` (abertura), `HIGH` (máximo), `LOW` (mínimo) e `CLOSE` (fechamento) ao longo do tempo.
- **Análise**: A análise desses preços permite observar a volatilidade e as flutuações diárias do mercado, facilitando a identificação de tendências de alta e baixa, assim como períodos de estabilidade.
- **Insights**: Alterações significativas nos valores `HIGH` e `LOW` indicam momentos de maior incerteza ou de eventos econômicos impactantes.

### Pontos e Totais de Pontos Over Time
- **Descrição**: Monitora os ganhos e perdas diários através da variável `Pontos`, bem como o acumulado com `Tot_Pontos`.
- **Análise**: Esses indicadores ajudam a observar o comportamento diário e a performance geral ao longo do tempo.

### Standard Deviations of Close Prices
- **Descrição**: Apresenta os desvios padrão para os preços de fechamento em períodos de 5, 10 e 20 dias, refletindo a volatilidade.
- **Análise**: Auxilia na análise de riscos e estabilidade dos preços em diferentes intervalos.

### High/Low to Close Ratios and Counts
- **Descrição**: Exibe as razões entre máximas/mínimas e fechamento, além da frequência de variações.
- **Análise**: Útil para entender a proximidade entre as variações de preços ao longo do tempo, ajudando a identificar padrões de curto prazo.

Este projeto é ideal para quem busca integrar a análise quantitativa e previsões algorítmicas para decisões mais informadas no mercado financeiro.

---

Para acessar os gráficos e mais detalhes, [clique aqui e abra o projeto no meu portfólio](https://sites.google.com/view/portifolio-giovanacarmazio/projetos/projeto-de-an%C3%A1lise-e-previs%C3%A3o-de-movimenta%C3%A7%C3%B5es-no-mercado-financeiro?authuser=0).
