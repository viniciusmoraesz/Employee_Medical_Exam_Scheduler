
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

