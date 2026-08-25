class Patient:
    def __init__(
        self, 
        name=None, 
        age=None, 
        vitals=None, 
        symptoms=None, 
        medications=None, 
        allergies=None
    ):
        self.name = name
        self.age = age
        self.medications = medications
        self.vitals = vitals
        self.symptoms = symptoms
        self.allergies = allergies

    def __repr__(self):
        return(
            f"Patient("
            f"name={self.name!r},"
            f"age={self.age!r},"
            f"medications={self.medications!r},"
            f"vitals={self.vitals!r},"
            f"symptoms={self.symptoms!r},"
            f"allergies={self.allergies!r}"
            f")"
        )


    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")

        self.age = age