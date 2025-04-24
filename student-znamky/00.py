import json

class Student:
    def __init__(self, student_id, isic_id, first_name, last_name, class_name, email):
        self.__student_id = student_id
        self.__isic_id = isic_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__class_name = class_name
        self.__email = email
        self.__subjects = {}  # {"subject": [{"event_name": ..., "points": ..., "base": ...}, ...]}

    def addSubject(self, subject):
        if subject not in self.__subjects:
            self.__subjects[subject] = []
        print(f"Predmet '{subject}' bol pridaný.")

    def removeSubject(self, subject):
        if subject in self.__subjects:
            if self.__subjects[subject]:
                confirm = input(f"Predmet '{subject}' má hodnotenia. Určite ho chceš vymazať? (áno/nie): ")
                if confirm.lower() != "áno":
                    print("Zrušené.")
                    return
            del self.__subjects[subject]
            print(f"Predmet '{subject}' bol odstránený.")
        else:
            print(f"Predmet '{subject}' sa nenašiel.")

    def addGrade(self, subject, event_name, points, base):
        if subject not in self.__subjects:
            print(f"Chyba: Predmet '{subject}' neexistuje.")
            return
        self.__subjects[subject].append({
            "event_name": event_name,
            "points": points,
            "base": base
        })
        print(f"Známka pre '{event_name}' z predmetu '{subject}' bola pridaná.")

    def removeGrade(self, event_name):
        found = False
        for grades in self.__subjects.values():
            for grade in grades:
                if grade["event_name"] == event_name:
                    grades.remove(grade)
                    found = True
                    print(f"Hodnotenie '{event_name}' bolo odstránené.")
                    break
        if not found:
            print(f"Hodnotenie '{event_name}' sa nenašlo.")

    def printAllGrades(self, subject=None):
        if subject:
            if subject not in self.__subjects:
                print(f"Predmet '{subject}' neexistuje.")
                return
            self.__printSubjectGrades(subject, self.__subjects[subject])
        else:
            for subject, grades in self.__subjects.items():
                self.__printSubjectGrades(subject, grades)

    def __printSubjectGrades(self, subject, grades):
        print(f"\nPredmet: {subject}")
        if not grades:
            print("  Žiadne hodnotenia.")
            return
        total_points = 0
        total_base = 0
        for g in grades:
            print(f"  {g['event_name']}: {g['points']}/{g['base']}")
            total_points += g['points']
            total_base += g['base']
        avg = (total_points / total_base) * 100 if total_base else 0
        print(f"  Priemer: {avg:.2f}%")
        print(f"  Slovné hodnotenie: {self.__getVerbalGrade(avg)}")

    def __getVerbalGrade(self, avg):
        if avg >= 90:
            return "výborný"
        elif avg >= 75:
            return "chválitebný"
        elif avg >= 60:
            return "dobrý"
        elif avg >= 50:
            return "dostatočný"
        else:
            return "nedostatočný"

    def store(self, filename):
        data = {
            "student_id": self.__student_id,
            "isic_id": self.__isic_id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "class_name": self.__class_name,
            "email": self.__email,
            "subjects": self.__subjects
        }
        with open(f"{filename}.student", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Dáta uložené do súboru {filename}.student")

    def load(self, filename):
        with open(f"{filename}.student", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.__student_id = data["student_id"]
        self.__isic_id = data["isic_id"]
        self.__first_name = data["first_name"]
        self.__last_name = data["last_name"]
        self.__class_name = data["class_name"]
        self.__email = data["email"]
        self.__subjects = data["subjects"]
        print(f"Dáta načítané zo súboru {filename}.student")


if __name__ == "__main__":
    # Testovanie triedy Student
    s = Student(1, "ISIC123", "Janko", "Hrasko", "IV.A", "janko@example.com")
    s.addSubject("matematika")
    s.addGrade("matematika", "test_1", 8, 10)
    s.addGrade("matematika", "test_2", 6, 10)

    s.addSubject("programovanie")
    s.addGrade("programovanie", "du1", 3, 10)
    s.addGrade("programovanie", "test_1", 9, 10)

    s.printAllGrades()
    s.store("janko")

    # Načítanie z dátového súboru:
    s2 = Student(0, "", "", "", "", "")
    s2.load("janko")
    s2.printAllGrades("matematika")
