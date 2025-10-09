class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self._medical_history = []

    def add_medical_record(self, date, diagnosis, treatment, doctor):
        record = {
            "date": date,
            "diagnosis": diagnosis,
            "treatment": treatment,
            "doctor": doctor
        }
        self._medical_history.append(record)
        return f"Medical report added successfully"

    def get_medical_history(self):
        return self._medical_history.copy()

    def calculate_age_group(self):
        if self.age < 18:
            return 'Child'
        elif self.age <= 65:
            return 'Adult'
        else:
            return 'Senior'
    
    def __str__(self):
        return f"{self.patient_id} -- {self.name} -- {self.age} -- {self.gender}"


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self._patients = []

    def assign_patient(self, patient):
        self._patients.append(patient)
        return f"Patient #{patient.patient_id} has been added successfully"

    def remove_patient(self, patient_id: str) -> str:
        for patient in self._patients:
            if patient.patient_id == patient_id:
                self._patients.remove(patient)
                return "Patient removed successfully"
        return "Patient not found"
    
    def list_patients(self):
        for patient in self._patients:
            print(patient)

    def get_patient_count(self):
        return len(self._patients)
    
    def __str__(self):
        return f"{self.doctor_id} -- {self.name} -- {self.specialization}"
    

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self._doctors = {}
        self._services = []

    def add_doctor(self, doctor):
        self._doctors[doctor.doctor_id] = doctor
        return f"Doctor #{doctor.doctor_id} has been added successfully"

    def remove_doctor(self, doctor_id):
        if doctor_id in self._doctors:
            self._doctors.pop(doctor_id)
            return True
        return False

    def find_doctor(self, doctor_id):
        if doctor_id in self._doctors:
            return True
        return False

    def get_doctors_by_specialization(self, specialization):
        doctors_by_specialization = [doctors for doctors in self._doctors.values() if doctors.specialization == specialization]
        return doctors_by_specialization
    

class Hospital:
    def __init__(self, name):
        self.name = name
        self._departments = {}
        self._patients = {}

    def admit_patient(self, patient, department_name, doctor_id):
        if department_name not in self._departments:
            return f"Department {department_name} not found"
        department = self._departments[department_name]
        doctor = department.find_doctor(doctor_id)

        if not doctor:
            return f"Doctor #{doctor_id} not found"
        
        self._patients[patient.patient_id] = patient

        doctor.assign_patient(patient)

        return f"Patient {patient.name} admitted to {department.name} under {doctor.name}"
    
    def discharge_patient(self, patient_id):

        if patient_id not in self._patients:
            return f"Patient {patient_id} was not found"
        
        patient = self._patients[patient_id]

        patient_removed = False
        for department in self._departments.values():
            for doctor in department._doctors.values():
                doctor.remove_patient(patient_id)
                return "Removed successfully"
            
        patient.add_medical_record(
            date="Today", 
            diagnosis="Discharged", 
            treatment="Patient discharged from hospital", 
            doctor="Hospital System"
            )
        
        self._patients.pop(patient_id)
        return f"Patient {patient.name} was discharged successfully"
    
    def transfer_patient(self, patient_id, from_dept, to_dept):
        
                        


        
        
        
        

        