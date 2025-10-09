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

    def caluculate_age_group(self):
        if self.age < 18:
            return 'Child'
        elif self.age <= 65:
            return 'Adult'
        else:
            return 'Senior'
        
