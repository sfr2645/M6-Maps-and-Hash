import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.courses = {}

    def add_entry(self, item):
        """Add ScheduleItem to dictionary"""
        self.courses[item.get_key()] = item

    def load_from_csv(self, filename):
        """Load CSV file"""
        with open(filename, encoding='utf-8-sig', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    item = ScheduleItem(
                        subject=row['Subject'],
                        catalog=row['Catalog'],
                        section=row['Section'],
                        component=row['Component'],
                        session=row['Session'],
                        units=int(row['Units']),
                        tot_enrl=int(row['TotEnrl']),
                        cap_enrl=int(row['CapEnrl']),
                        instructor=row['Instructor']
                    )
                    self.add_entry(item)
                except:
                    # Skip bad rows (like #REF! etc.)
                    continue

    def print_header(self):
        print(f"{'Subject':<6}{'Catalog':<8}{'Section':<8}"
              f"{'Component':<10}{'Session':<6}"
              f"{'Units':<6}{'TotEnrl':<8}{'CapEnrl':<8}"
              f"{'Instructor'}")

    def print(self, items=None):
        """Print all or filtered items"""
        self.print_header()

        if items is None:
            items = self.courses.values()

        for item in items:
            item.print()

    def find_by_subject(self, subject):
        return [c for c in self.courses.values()
                if c.subject.lower() == subject.lower()]

    def find_by_subject_catalog(self, subject, catalog):
        return [c for c in self.courses.values()
                if c.subject.lower() == subject.lower()
                and c.catalog == catalog]

    def find_by_instructor_last_name(self, last_name):
        return [c for c in self.courses.values()
                if c.instructor.split(',')[0].lower() == last_name.lower()]
