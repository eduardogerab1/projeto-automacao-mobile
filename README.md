# Automação Mobile

Suíte de testes automatizados para o aplicativo Android **Sauce Labs Demo App**, desenvolvida em Python com Appium, Selenium e Pytest.

## Objetivo

Validar o fluxo de compra do aplicativo, desde a seleção de um produto até as etapas de carrinho, autenticação e preenchimento do endereço de entrega. A suíte também verifica mensagens de validação e o comportamento dos controles de quantidade.

## Tecnologias

- Python
- Pytest
- Appium Python Client
- Selenium WebDriver
- Android Emulator
- Appium UiAutomator2

## Estrutura do projeto

```text
.
├── conftest.py             # Fixture do driver e evidências de falha
├── pytest.ini              # Configuração de execução do Pytest
├── tests/
│   └── test_app.py         # Suíte principal com Page Object Model
├── pages/                  # Page Objects das telas do aplicativo
├── utils/                  # Utilitários, dados e logger
├── test_challenge.py       # Fluxo exploratório com validações detalhadas
└── test_open_app.py        # Fluxo manual de compra ponta a ponta
```

## Cobertura da suíte

O teste principal, em `tests/test_app.py`, cobre:

- abertura do aplicativo e validação da tela de produtos;
- seleção da **Sauce Labs Backpack (orange)**;
- redução da quantidade até zero e verificação de que o botão do carrinho fica desabilitado;
- aumento da quantidade e validação da habilitação do botão;
- adição de duas unidades ao carrinho;
- conferência do badge, nome, preço, quantidade e total dos itens;
- navegação para o checkout e validação da tela de login;
- tentativa de login sem usuário e sem senha;
- login usando as credenciais disponibilizadas na própria tela do aplicativo;
- validação dos campos obrigatórios do endereço de entrega;
- preenchimento dos dados de entrega e avanço para a etapa de pagamento.

Os scripts `test_challenge.py` e `test_open_app.py` registram fluxos complementares. O primeiro aprofunda as validações negativas de login, endereço e pagamento; o segundo executa um fluxo completo de checkout e valida a mensagem **Checkout Complete**.

## Pré-requisitos

1. Instale o Python 3.9 ou superior.
2. Instale e configure o [Node.js](https://nodejs.org/) e o Appium Server.
3. Instale o driver Android UiAutomator2:

	```bash
	appium driver install uiautomator2
	```

4. Configure um Android Emulator com o identificador `emulator-5554`.
5. Instale no emulador o aplicativo Sauce Labs Demo App com o pacote `com.saucelabs.mydemoapp.android`.
6. Instale as bibliotecas Python do projeto:

	```bash
	python -m pip install pytest Appium-Python-Client selenium
	```

## Como executar

Com o emulador iniciado e o Appium Server disponível em `http://127.0.0.1:4723`, execute na raiz do projeto:

```bash
pytest
```

Para executar somente a suíte principal:

```bash
pytest tests/test_app.py
```

O arquivo `pytest.ini` configura `tests` como diretório padrão e habilita saída detalhada e logs no terminal.

## Evidências de falha

O fixture definido em `conftest.py` inicia a gravação da tela para cada teste. Quando um teste falha, a suíte salva:

- uma captura de tela em `screenshots/`;
- um vídeo da execução em `videos/`.

Em caso de sucesso, a gravação é encerrada e descartada.

## Observações

- Os testes dependem da disponibilidade do emulador, do Appium Server e do aplicativo instalado.
- Os seletores e textos esperados são específicos da versão do Sauce Labs Demo App usada no projeto.
- O teste principal utiliza o padrão **Page Object Model**, mantendo a interação com cada tela concentrada em `pages/`.