from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self):
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        print(f"{self.subject:<6}{self.catalog:<8}{self.section:<8}"
              f"{self.component:<10}{self.session:<6}"
              f"{self.units:<6}{self.tot_enrl:<8}{self.cap_enrl:<8}"
              f"{self.instructor}")
