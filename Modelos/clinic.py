from uuid import UUID
from datetime import time
from typing import List
from Modelos.exam_type_enum import ExamTypeEnum

class Clinic:
    def __init__(self, clinic_id: UUID, opening_hour: time, closing_hour: time, exam_types: List[ExamTypeEnum]):
        self._clinic_id = clinic_id
        self._opening_hour = opening_hour
        self._closing_hour = closing_hour
        self._exam_types = exam_types
        self._scheduled_exams = []
    

    @property
    def clinic_id(self):
        return self._clinic_id

    @property
    def opening_hour(self):
        return self._opening_hour

    @property
    def closing_hour(self):
        return self._closing_hour

    @property
    def exam_types(self):
        return self._exam_types
    
    @property
    def scheduled_exams(self):
        return self._scheduled_exams
    
   


    



    