# Ideia do Projeto

A ideia inicial do projeto é aprender e colocar em prática conceitos relacionados ao MediaPipe, visando aprimorar minhas habilidades em lógica de programação, visão computacional e interação humano-computador.

---

# Controle por Gestos

A proposta do programa é relativamente simples. Inicialmente, foi utilizada a biblioteca OpenCV para realizar a leitura da câmera do computador em tempo real.

Em seguida, foi utilizada a biblioteca MediaPipe, importada como `mediapipe as mp`, responsável pela detecção das mãos e dos pontos utilizados para identificar os gestos realizados pelo usuário.

Posteriormente, foi utilizada a biblioteca `subprocess`, permitindo a comunicação com o sistema operacional Windows para abrir e fechar programas automaticamente.

Por fim, a biblioteca `time` foi utilizada para controlar o intervalo entre os comandos, evitando múltiplas execuções consecutivas em um curto período de tempo.

---

# Funcionamento do Programa

A lógica do programa consiste na identificação de gestos realizados com a mão. A partir disso, o sistema executa comandos específicos no computador.

Os comandos implementados atualmente são:

* ☝️ Indicador levantado:

  → abre o Bloco de Notas (Notepad)

* ✌️ Indicador + médio levantados:

  → fecha o programa aberto

---

# Execução do programa

Abra o terminal do VS Code e execute:

```bash
pip install opencv-python mediapipe
```

Depois rode o programa com:

```bash
python projeto.py
```

O programa abrirá a webcam e permitirá controlar o Bloco de Notas utilizando gestos das mãos.

---

# Linguagem Utilizada

* Python

---

# Metodologia

Toda a ideia do projeto foi idealizada e desenvolvida por mim. Durante a implementação do código, utilizei o ChatGPT como ferramenta de apoio para aprendizado, compreensão dos conceitos e auxílio no desenvolvimento do programa.

---

# Conclusão

O programa executa corretamente as funcionalidades implementadas até o momento, sem apresentar erros durante os testes realizados.

Apesar disso, o projeto ainda não está totalmente concluído, pois existem diversas melhorias e implementações planejadas futuramente, buscando tornar a interação mais completa, eficiente e intuitiva.
