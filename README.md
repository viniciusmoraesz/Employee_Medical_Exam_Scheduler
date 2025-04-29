
# 📚 Sistema de Agendamento de Exames para Funcionários

## 📋 Visão Geral do Projeto

**O sistema permite**:

✅ Agendar exames em clínicas cadastradas.

✅ Garantir que o funcionário e a clínica existam.

✅ Validar se o tipo de exame é oferecido pela clínica.

✅ Garantir que o agendamento ocorra dentro do horário de funcionamento.

✅ Evitar conflitos de horário com outros exames.


## 🛠 Como Funciona - Classes

🏥 **Clinic** :

Contém informações sobre:

- Horários de funcionamento da clínica

- Tipos de exame disponíveis

- Exames já agendados

👨‍💼 **Employee** :

- Armazena dados dos funcionários, como:

- Nome

- E-mail

- Data de nascimento (DOB)

- Esses funcionários são os que podem agendar exames no sistema.

📅 **ExamSchedulerClass** :

***É o coração do sistema do meu código***

Responsável por:

- Localizar a clínica e o funcionário corretos

- Verificar se o tipo de exame é válido

- Confirmar se o horário do exame está disponível

- Agendar o exame caso todas as condições sejam atendidas

*Obs : Toda a lógica principal de agendamento e validações foi construída dentro dessa classe.*

## 🔎 Explicação Detalhada do Método execute()

🔎 **Buscar a Clínica** :
Verifica se a clínica existe no sistema usando o clinic_id.

🔎 **Buscar o Funcionário** :
Verifica se o funcionário existe usando o employee_id.

📑 **Verificar o Tipo de Exame** :
Confirma se o exame solicitado está disponível na clínica.

⏰ **Checar Horário de Funcionamento** :
Garante que o exame seja agendado dentro do horário de abertura e fechamento da clínica.

📆 **Verificar Conflito de Horário** :
Confirma que não há outro exame agendado no mesmo horário.

✅ **Agendar o Exame** :
Se tudo estiver correto, agenda o exame para o funcionário.


## 💻 Como Rodar o Projeto

Para rodar o projeto, siga os seguintes passos:

1. **Clone o repositório** para sua máquina local:
    ```bash
    git clone <url-do-repositório>
    ```

2. **Instale as dependências necessárias** (se houver):
    Caso haja dependências específicas, você pode usar o `pip` para instalar o que for necessário.
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o código**:
    O código principal está no arquivo `__main__.py`. Para rodá-lo, basta executar o seguinte comando:

    ```bash
    python __main__.py
    ```

    Isso criará as listas de clínicas e funcionários, e agendará um exame conforme as validações da lógica implementada.

    **Nota**: Lembre-se de que o próprio código já cria as clínicas, os funcionários e os exames. Ou seja, não é necessário inserir dados manualmente para testar o sistema.

    **OBS:** Você pode criar **quantas clínicas e funcionários quiser**! Basta criar novos objetos e adicionar às listas de clínicas (`list_of_clinics`) e funcionários (`list_of_employee`) dentro do código, como no exemplo abaixo:

    ```python
    clinic3 = Clinic(
        clinic_id=uuid4(),
        opening_hour=time(9, 0),
        closing_hour=time(17, 0),
        exam_types=[ExamTypeEnum.GENERAL_CHECKUP]
    )
    list_of_clinics.append(clinic3)
    
    employee2 = Employee(
        employee_id=uuid4(),
        name="João Silva",
        date_of_birth=date(1990, 7, 12),
        position="Manager",
        email="joao.silva@email.com",
        phone_number="+55 (11) 912345678",
        business="TechCorp",
        status=True
    )
    list_of_employee.append(employee2)
    ```

    Basta adicionar novos objetos à lista e os exames serão agendados com base nas novas clínicas e funcionários cadastrados.

---

## 📜 Exemplo de Execução

Ao rodar o código, você verá algo assim no terminal:

```bash
True Exam was scheduled with success!
==================================================
Clinic ID: 4918d8cf-abbe-4f77-bc1f-5cc6d739ff15   
Operating Hours: 08:00 - 18:00
--------------------------------------------------
Scheduled Exams:
  1. Exam Type: GENERAL_CHECKUP
     Start: 17:00
     End: 18:00
     Scheduled by: Maria Valentina
     Employee DOB: 05/11/2004
     Employee Email: mariavalentina995@email.com  

==================================================
==================================================
Clinic ID: 572532f7-c608-4eaf-8482-fdc6f4196516   
Operating Hours: 06:00 - 17:00
--------------------------------------------------
  No exams scheduled.
==================================================
