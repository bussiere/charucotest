from fpdf import FPDF


class ConventionParentale(FPDF):
    def __init__(self, format):
        super().__init__(format=format)
        self.document_font = "SourceCodeProBold"
        self.text_framework_title = """ CONVENTION PARENTALE """
        self.text_framework_content = """ ENTRE {{CIV_GUEST}} {{SURNAME_GUEST}} {{NAME_GUEST}} et {{CIV_OTHER}} {{SURNAME_OTHER}}  {{NAME_OTHER}}  """
        self.text_framework_date = """ {{DATE}} """
        self.text_framework_size = 6
        self.text_framework_font = "SourceCodeProBold"
        self.text_framework_cell_y = (self.text_framework_size / 2) + 1
        self.blue = [76.0, 32.0, 250.0]
        self.black = [0.0, 0.0, 0.0]
        self.text_parties_size = 6
        self.text_parties_cell_y = (self.text_parties_size / 2) + 1
        self.text_parties_opening = "ENTRE :"
        self.text_parties_guest = """{{CIV_GUEST}} {{SURNAME_GUEST}} {{NAME_GUEST}}, née le {{BIRTHDATE_GUEST}} à Ville {{BIRTHTOWN_GUEST}}, de nationalité {{NATIONALITY_GUEST}}, résidant {{ADRESS_GUEST}} {{TOWN_GUEST}} {{POSTALCODE_GUEST}}, exerçant la profession de {{JOB_GUEST}}, enregistrée auprès de la sécurité sociale sous le numéro {{SOCIALNUMBER_GUEST}}, résidante fiscale au sens de la règlementation française, {{PHONE_GUEST}}, {{MAIL_GUEST}}."""
        self.text_parties_middle = """ ET :"""
        self.text_parties_other = """{{CIV_OTHER}} {{SURNAME_OTHER}} {{NAME_OTHER}}, née le {{BIRTHDATE_OTHER}} à Ville {{BIRTHTOWN_OTHER}}, de nationalité {{NATIONALITY_OTHER}}, résidant {{ADRESS_OTHER}} {{TOWN_OTHER}} {{POSTALCODE_OTHER}}, exerçant la profession de {{JOB_OTHER}}, enregistrée auprès de la sécurité sociale sous le numéro {{SOCIALNUMBER_OTHER}}, résidante fiscale au sens de la règlementation française, {{PHONE_OTHER}}, {{MAIL_OTHER}}."""
        self.text_parties_conclusion = """ Les parties ont convenu ce qui suit :"""
        self.text_summary_size = 6
        self.text_summary_subpart_size = 6
        self.text_summary_subpart_subpart_size = 5
        self.text_summary_cell_y = (self.text_summary_size / 2) + 1
        self.text_summary_subpart_cell_y = (self.text_summary_subpart_size / 2) + 1
        self.text_summary_subpart_subpart_cell_y = (
            self.text_summary_subpart_subpart_size / 2
        ) + 1
        self.text_summary_title = """SOMMAIRE"""
        self.text_summary_chapter_one = """I - SUR LA SITUATION PARENTALE """
        self.text_summary_chapter_two = """II - SUR L'AUTORITÉ PARENTALE"""
        self.text_summary_chapter_two_a = """A – Sur le droit applicable"""
        self.text_summary_chapter_two_a_one = (
            """1 - Sur la définition de l'autorité parentale"""
        )
        self.text_summary_chapter_two_a_two = (
            """2 - Sur l'exercice conjoint de l'autorité parentale"""
        )
        self.text_summary_chapter_two_a_three = (
            """3 - Sur l'absence d'incidence de la séparation"""
        )
        self.text_summary_chapter_two_a_four = """4 - Sur la démocratie parentale"""
        self.text_summary_chapter_two_a_five = (
            """5 - Sur la contribution à l'entretien et à l'éducation de(s) enfant(s)"""
        )
        self.text_summary_chapter_two_a_six = """6 - Sur le maintien du lien parental"""
        self.text_summary_chapter_two_b = (
            """B - Sur les modalités d'exercice de l'autorité parentale"""
        )

    def framework(self):
        self.framework_rect()
        self.framework_title()
        self.framework_content()
        self.framework_date()

    def framework_rect(self):
        self.rect(30.0, 40.0, 150, 40)

    def framework_title(self):
        self.set_xy(90.0, 45.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.text_framework_font, "", self.text_framework_size)
        self.multi_cell(0, 10, self.text_framework_title)

    def framework_content(self):
        self.set_xy(40.0, 50.0)
        self.set_text_color(self.blue[0], self.blue[1], self.blue[2])
        self.set_font(self.text_framework_font, "", self.text_framework_size)
        self.multi_cell(0, 5, self.text_framework_content)

    def framework_date(self):
        self.set_xy(90.0, 55.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.text_framework_font, "", self.text_framework_size)
        self.multi_cell(0, 10, self.text_framework_date)

    def parties(self):
        self.parties_opening()
        self.parties_party_guest()
        self.parties_middle()
        self.parties_party_other()
        self.parties_conclusion()

    def parties_opening(self):
        self.set_xy(30, 20.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_parties_size)
        self.multi_cell(0, self.text_parties_cell_y, self.text_parties_opening)

    def parties_party_guest(self):
        self.set_xy(30, 30.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_parties_size)
        self.multi_cell(0, self.text_parties_cell_y, self.text_parties_guest)

    def parties_middle(self):
        self.set_xy(30, 50.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_parties_size)
        self.multi_cell(0, self.text_parties_cell_y, self.text_parties_middle)

    def parties_party_other(self):
        self.set_xy(30, 60.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_parties_size)
        self.multi_cell(0, self.text_parties_cell_y, self.text_parties_other)

    def parties_conclusion(self):
        self.set_xy(30, 80.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_parties_size)
        self.multi_cell(0, self.text_parties_cell_y, self.text_parties_conclusion)

    def summary(self):
        self.summary_rects()
        self.summary_title()
        self.summary_chapter_one()
        self.summary_chapter_two()
        self.summary_chapter_two_a()
        self.summary_chapter_two_a_one()
        self.summary_chapter_two_a_two()
        self.summary_chapter_two_a_three()
        self.summary_chapter_two_a_four()
        self.summary_chapter_two_a_five()
        self.summary_chapter_two_a_six()
        self.summary_chapter_two_b()

    def summary_rects(self):
        self.rect(30.0, 20.0, 150, 10)
        self.rect(31.0, 21.0, 148, 8)

    def summary_title(self):
        self.set_xy(105.0, 23.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_summary_size)
        self.multi_cell(0, self.text_summary_cell_y, self.text_summary_title)

    def summary_chapter_one(self):
        self.set_xy(30.0, 35.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "U", self.text_summary_size)
        self.multi_cell(0, self.text_summary_cell_y, self.text_summary_chapter_one)

    def summary_chapter_two(self):
        self.set_xy(30.0, 40.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "U", self.text_summary_size)
        self.multi_cell(0, self.text_summary_cell_y, self.text_summary_chapter_two)

    def summary_chapter_two_a(self):
        self.set_xy(30.0, 45.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "U", self.text_summary_subpart_size)
        self.multi_cell(
            0, self.text_summary_subpart_cell_y, self.text_summary_chapter_two_a
        )

    def summary_chapter_two_a_one(self):
        self.set_xy(40.0, 50.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_summary_subpart_subpart_size)
        self.multi_cell(
            0,
            self.text_summary_subpart_subpart_cell_y,
            self.text_summary_chapter_two_a_one,
        )

    def summary_chapter_two_a_two(self):
        self.set_xy(40.0, 55.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_summary_subpart_subpart_size)
        self.multi_cell(
            0,
            self.text_summary_subpart_subpart_cell_y,
            self.text_summary_chapter_two_a_two,
        )

    def summary_chapter_two_a_three(self):
        self.set_xy(40.0, 60.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_summary_subpart_subpart_size)
        self.multi_cell(
            0,
            self.text_summary_subpart_subpart_cell_y,
            self.text_summary_chapter_two_a_three,
        )

    def summary_chapter_two_a_four(self):
        self.set_xy(40.0, 65.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_summary_subpart_subpart_size)
        self.multi_cell(
            0,
            self.text_summary_subpart_subpart_cell_y,
            self.text_summary_chapter_two_a_four,
        )

    def summary_chapter_two_a_five(self):
        self.set_xy(40.0, 70.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_summary_subpart_subpart_size)
        self.multi_cell(
            0,
            self.text_summary_subpart_subpart_cell_y,
            self.text_summary_chapter_two_a_five,
        )

    def summary_chapter_two_a_six(self):
        self.set_xy(40.0, 75.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "", self.text_summary_subpart_subpart_size)
        self.multi_cell(
            0,
            self.text_summary_subpart_subpart_cell_y,
            self.text_summary_chapter_two_a_six,
        )

    def summary_chapter_two_b(self):
        self.set_xy(30.0, 85.0)
        self.set_text_color(self.black[0], self.black[1], self.black[2])
        self.set_font(self.document_font, "U", self.text_summary_subpart_size)
        self.multi_cell(
            0, self.text_summary_subpart_cell_y, self.text_summary_chapter_two_b
        )


pdf = ConventionParentale(format="A4")
pdf.add_font("SourceCodeProBold", "", "SourceCodePro-Bold.ttf", uni=True)
pdf.add_page()
pdf.framework()
pdf.add_page()
pdf.parties()
pdf.add_page()
pdf.summary()
pdf.output("test.pdf", "F")
