from datetime import datetime, time, timedelta, date
from uuid import uuid4
from typing import List

from Modelos.exam_type_enum import ExamTypeEnum
from Modelos.clinic import Clinic
from Modelos.exam_scheduler import ExamSchedulerClass
from Modelos.employee import Employee

def main():
    
    clinic1 = Clinic(
        clinic_id=uuid4(),
        opening_hour=time(8, 0),
        closing_hour=time(18, 0),
        exam_types=[ExamTypeEnum.GENERAL_CHECKUP, ExamTypeEnum.DENTAL_EXAM]
    )

    clinic2 = Clinic(
        clinic_id=uuid4(),
        opening_hour=time(6,0),
        closing_hour=time(17,0),
        exam_types=[ExamTypeEnum.VISION_TEST]
    )
    
    list_of_clinics = []
    list_of_clinics.append(clinic1)
    list_of_clinics.append(clinic2)


    employee1 = Employee(
       employee_id=uuid4(),
       name="Maria Valentina",
       date_of_birth=date(2004, 11, 5),
       position="Developer",
       email="mariavalentina995@email.com",
       phone_number="+55 (19) 998151345",
       business="Falcon INC",
       status=True
    )





    list_of_employee = []
    list_of_employee.append(employee1)


    scheduler = ExamSchedulerClass(list_of_clinics, list_of_employee)

    #EXAM 1 IN CLINIC 1, IT SHOULD RETURN TRUE BECAUSE IT FOLLOWS ALL THE RULES
    exam_start = datetime(2025, 4, 27, 9, 0)
    result, message = scheduler.execute(employee_id=employee1.employee_id, clinic_id=clinic1.clinic_id, exam_type=ExamTypeEnum.GENERAL_CHECKUP, exam_start=exam_start)
    print(result, message)
    
    
    #print the clinics with
    for clinic in list_of_clinics:
            print("=" * 50)
            print(f"Clinic ID: {clinic.clinic_id}")
            print(f"Operating Hours: {clinic.opening_hour.strftime('%H:%M')} - {clinic.closing_hour.strftime('%H:%M')}")
            print("-" * 50)

            if clinic.scheduled_exams:
             print("Scheduled Exams:")
             for idx, exam in enumerate(clinic.scheduled_exams, start=1):
                print(f"  {idx}. Exam Type: {exam['exam_type'].name}")
                print(f"     Start: {exam['start_time'].strftime('%H:%M')}")
                print(f"     End: {exam['end_time'].strftime('%H:%M')}")
            # Add employee details to the output
                employee = exam['employee']
                print(f"     Scheduled by: {employee.name}")
                print(f"     Employee DOB: {employee.date_of_birth.strftime('%Y-%m-%d')}")
                print(f"     Employee Email: {employee.email}")
                print()
            else:
                print("  No exams scheduled.")
            print("=" * 50)





if __name__ == "__main__":
    main()
