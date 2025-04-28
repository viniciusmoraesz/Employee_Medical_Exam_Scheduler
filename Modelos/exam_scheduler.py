from datetime import datetime, time, timedelta
from uuid import UUID
from Modelos.employee import Employee

from Modelos.exam_type_enum import ExamTypeEnum
from Modelos.clinic import Clinic
from typing import List


class ExamSchedulerClass:
    def __init__(self, clinics: List[Clinic], employees : List[Employee]):
        self.clinics = clinics
        self.employees = employees 

    def execute(self, employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, exam_start: datetime) -> tuple[bool, str]:
        self.employee_id = employee_id
        self.clinic_id = clinic_id
        self.exam_start = exam_start
        self.exam_type = exam_type


        #1st Verification - Find the Clinic
        found_clinic = None

        for clinic in self.clinics:
            if clinic.clinic_id == clinic_id:
                  found_clinic = clinic 
                  break

        if not found_clinic:
            return False, "Clinic not Found!"
        
        #2nd Verification - Find the Employee
        found_employee = None

        for employee in self.employees:
            if employee.employee_id == employee_id:
                found_employee = employee
                break

        if not found_employee:
            return False, "Employee not Found!"    

        #3rd Verification - Is the Exam type in the list?
        if exam_type not in found_clinic.exam_types:
            return False, ", The type of the exam was not found!"
        
        #4th Verification - Scheduling an Exam Outside Clinic Hours
        exam_start_time = exam_start.time()
        exam_end_time = (datetime.combine(exam_start.date(), exam_start_time) + timedelta(hours=1)).time()


        if exam_start_time < found_clinic.opening_hour or exam_start_time >= found_clinic.closing_hour:
            return False, "Exam cannot be scheduled outside of opening hours"
       
        if exam_end_time > found_clinic.closing_hour:
            return False, "Exam cannot be scheduled outside of opening hours"
    
        
        #5th Verification - Scheduling a conflicting time (The exam lasts 1 hour)
        for scheduled_exam in found_clinic.scheduled_exams:
            scheduled_start = scheduled_exam['start_time']
            scheduled_end = scheduled_exam['end_time']

            if (exam_start_time < scheduled_end and exam_end_time > scheduled_start):
                return False, "Time conflict with another scheduled exam"



        # If passed all checks, the exam is successfully scheduled
        found_clinic.scheduled_exams.append({
            'start_time': exam_start_time,
            'end_time': exam_end_time,
            'exam_type': exam_type,
            'employee': found_employee
        })

        return True, "Exam was scheduled with sucess!"