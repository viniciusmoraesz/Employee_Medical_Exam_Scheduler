from datetime import datetime, time, timedelta
from uuid import uuid4
from typing import List

from Modelos.exam_type_enum import ExamTypeEnum
from Modelos.clinic import Clinic
from Modelos.exam_scheduler import ExamSchedulerClass

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

    scheduler = ExamSchedulerClass(list_of_clinics)

    #EXAM 1 IN CLINIC 1, IT SHOULD RETURN TRUE BECAUSE IT FOLLOWS ALL THE RULES
    exam_start = datetime(2025, 4, 27, 9, 0)
    result, message = scheduler.execute(employee_id=uuid4(), clinic_id=clinic1.clinic_id, exam_type=ExamTypeEnum.GENERAL_CHECKUP, exam_start=exam_start)
    print(result, message)
    
    #EXAM 1 IN CLINIC 2, IT SHOULD RETURN TRUE BECAUSE IT FOLLOWS ALL THE RULES
    exam_start = datetime(2025, 4, 27, 12, 0)
    result, message = scheduler.execute(employee_id=uuid4(), clinic_id=clinic2.clinic_id, exam_type=ExamTypeEnum.VISION_TEST, exam_start=exam_start)
    print(result, message)  

    #EXAM 2 IN CLINIC 1, IT SHOULD RETURN FALSE BECAUSE THERE'S A TIME CONFLICT WITH THE FIRST EXAM
    exam_start = datetime(2025, 4, 27, 9, 5)
    result, message = scheduler.execute(employee_id=uuid4(), clinic_id=clinic1.clinic_id, exam_type=ExamTypeEnum.GENERAL_CHECKUP, exam_start=exam_start)
    print(result, message)  
    
    #EXAM 3 IN CLINIC 1, IT SHOULD RETURN TRUE
    exam_start = datetime(2025, 4, 27, 10, 0)
    result, message = scheduler.execute(employee_id=uuid4(), clinic_id=clinic1.clinic_id, exam_type=ExamTypeEnum.GENERAL_CHECKUP, exam_start=exam_start)
    print(result, message)  


    
    #print the existing clinics and their respective exams
    print("\n")
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
            print()
        else:
          print("  No exams scheduled.")
    print("=" * 50)
    print()




if __name__ == "__main__":
    main()
