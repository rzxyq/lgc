from django import forms

class NewStudentForm(forms.Form):
    name = forms.CharField(max_length=35)
    netid = forms.CharField(max_length=10)
    hometown = forms.CharField(max_length=35)
    YEAR = (
        ('Freshman', 'Freshman'),
        ('Sophomore Transfer', 'Sophomore Transfer'),
        ('Junior Transfer', 'Junior Transfer'),
    )
    year = forms.ChoiceField(label=("Year"),
        choices=YEAR, widget=forms.Select(),)
    SCHOOL = (
        ('Arts & Sciences', 'Arts & Sciences'),
        ('Agriculture & Life Sciences', 'Agriculture & Life Sciences'),
        ('Architecture, Art & Planning','Architecture, Art & Planning'),
        ('Engineering','Engineering'),
        ('Hotel Administration','Hotel Administration'),
        ('Human Ecology','Human Ecology'),
        ('Industrial & Labor Relations','Industrial & Labor Relations'),
    )
    school = forms.ChoiceField(label=("College"),
        choices=SCHOOL, widget=forms.Select(),)
    MAJOR = (
        #First entry is an abbreviation, second is how it appears on the site
        ('Africana Studies','Africana Studies'),
        ('Agricultural Sciences','Agricultural Sciences'),
        ('American Studies','American Studies'),
        ('Animal Science','Animal Science'),
        ('Anthropology','Anthropology'),
        ('Applied Economics and Management','Applied Economics and Management'),
        ('Archaeology','Archaeology'),
        ('Architecture','Architecture'),
        ('Asian Studies','Asian Studies'),
        ('Astronomy','Astronomy'),
        ('Atmospheric Science','Atmospheric Science'),
        ('Biological Engineering','Biological Engineering'),
        ('Biological Sciences','Biological Sciences'),
        ('Biology and Society','Biology and Society'),
        ('Biometry and Statistics','Biometry and Statistics'),
        ('Chemical Engineering','Chemical Engineering'),
        ('Chemistry and Chemical Biology','Chemistry and Chemical Biology'),
        ('China and Asia-Pacific Studies','China and Asia-Pacific Studies'),
        ('Civil Engineering','Civil Engineering'),
        ('Classics','Classics'),
        ('Communication','Communication'),
        ('Comparative Literature','Comparative Literature'),
        ('Computer Science','Computer Science'),
        ('Design and Environmental Analysis','Design and Environmental Analysis'),
        ('Development Sociology','Development Sociology'),
        ('Economics','Economics'),
        ('Electrical and Computer Engineering','Electrical and Computer Engineering'),
        ('Engineering Physics','Engineering Physics'),
        ('English','English'),
        ('Entomology','Entomology'),
        ('Environmental Engineering','Environmental Engineering'),
        ('Environmental Science and Sustainability','Environmental Science and Sustainability'),
        ('Feminist, Gender and Sexuality Studies','Feminist, Gender and Sexuality Studies'),
        ('Fiber Science and Apparel Design','Fiber Science and Apparel Design'),
        ('Fine Arts','Fine Arts'),
        ('Food Science','Food Science'),
        ('French','French'),
        ('German Studies','German Studies'),
        ('Government','Government'),
        ('History','History'),
        ('History of Architecture','History of Architecture'),
        ('History of Art','History of Art'),
        ('Hotel Administration','Hotel Administration'),
        ('Human Biology, Health and Society','Human Biology, Health and Society'),
        ('Human Development','Human Development'),
        ('Industrial and Labor Relations','Industrial and Labor Relations'),
        ('Information Science','Information Science'),
        ('Information Science Systems and Technology','Information Science, Systems and Technology'),
        ('International Agriculture and Rural Development','International Agriculture and Rural Development'),
        ('Italian','Italian'),
        ('Landscape Architecture','Landscape Architecture'),
        ('Linguistics','Linguistics'),
        ('Materials Science and Engineering','Materials Science and Engineering'),
        ('Mathematics','Mathematics'),
        ('Mechanical Engineering','Mechanical Engineering'),
        ('Music','Music'),
        ('Near Eastern Studies','Near Eastern Studies'),
        ('Nutritional Sciences','Nutritional Sciences'),
        ('Operations Research and Engineering','Operations Research and Engineering'),
        ('Performing and Media Arts','Performing and Media Arts'),
        ('Philosophy','Philosophy'),
        ('Physics','Physics'),
        ('Plant Sciences','Plant Sciences'),
        ('Policy Analysis and Management','Policy Analysis and Management'),
        ('Psychology','Psychology'),
        ('Religious Studies','Religious Studies'),
        ('Science and Technology Studies','Science and Technology Studies'),
        ('Science of Earth Systems','Science of Earth Systems'),
        ('Sociology','Sociology'),
        ('Spanish','Spanish'),
        ('Statistics','Statistics'),
        ('Urban and Regional Planning','Urban and Regional Planning'),
        ('Viticulture and Enology','Viticulture and Enology'),
    )
    major = forms.ChoiceField(label=("Major"),
        choices=MAJOR, widget=forms.Select(),)

    MINOR = (
        #First entry is an abbreviation, second is how it appears on the site
        ('None', 'None'),
        ('Aerospace Engineering','Aerospace Engineering'),
        ('Africana Studies','Africana Studies'),
        ('Agribusiness Management','Agribusiness Management'),
        ('American Indian Studies','American Indian Studies'),
        ('Animal Science','Animal Science'),
        ('Anthropology','Anthropology'),
        ('Applied Economics','Applied Economics'),
        ('Applied Exercise Science','Applied Exercise Science'),
        ('Applied Mathematics','Applied Mathematics'),
        ('Archaeology','Archaeology'),
        ('Architecture','Architecture'),
        ('Asian American Studies','Asian American Studies'),
        ('Astronomy','Astronomy'),
        ('Atmospheric Science','Atmospheric Science'),
        ('Biological Engineering','Biological Engineering'),
        ('Biological Sciences','Biological Sciences'),
        ('Biomedical Engineering','Biomedical Engineering'),
        ('Biomedical Sciences','Biomedical Sciences'),
        ('Biometry and Statistics','Biometry and Statistics'),
        ('Business','Business'),
        ('Business for Engineering Students','Business for Engineering Students'),
        ('China and Asia-Pacific Studies','China and Asia-Pacific Studies'),
        ('Civil Infrastructure','Civil Infrastructure'),
        ('Classics','Classics'),
        ('Climate Change','Climate Change'),
        ('Cognitive Science','Cognitive Science'),
        ('Communication','Communication'),
        ('Computer Science','Computer Science'),
        ('Computing in the Arts','Computing in the Arts'),
        ('Creative Writing','Creative Writing'),
        ('Crop Management','Crop Management'),
        ('Dance','Dance'),
        ('Design and Environmental Analysis','Design and Environmental Analysis'),
        ('Development Sociology','Development Sociology'),
        ('East Asia Program','East Asia Program'),
        ('English','English'),
        ('Education','Education'),
        ('Electrical and Computer Engineering','Electrical and Computer Engineering'),
        ('Engineering Management','Engineering Management'),
        ('Engineering Statistics','Engineering Statistics'),
        ('Entomology','Entomology'),
        ('Environmental and Resource Economics','Environmental and Resource Economics'),
        ('Environmental Engineering','Environmental Engineering'),
        ('European Studies','European Studies'),
        ('Feminist, Gender and Sexuality Studies','Feminist, Gender and Sexuality Studies'),
        ('Fiber Science','Fiber Science'),
        ('Film','Film'),
        ('Fine Arts','Fine Arts'),
        ('Food Science','Food Science'),
        ('French Studies','French Studies'),
        ('Game Design','Game Design'),
        ('German Studies','German Studies'),
        ('Gerontology','Gerontology'),
        ('Global Health','Global Health'),
        ('Globalization, Ethnicity and Development','Globalization, Ethnicity and Development'),
        ('Health Policy','Health Policy'),
        ('History','History'),
        ('History of Art','History of Art'),
        ('Horticulture','Horticulture'),
        ('Human Biology','Human Biology'),
        ('Industrical Systems and Information Technology','Industrial Systems and Information Technology'),
        ('Inequality Studies','Inequality Studies'),
        ('Information Science','Information Science'),
        ('International Relations','International Relations'),
        ('International Development Studies','International Development Studies'),
        ('International Trade and Development','International Trade and Development'),
        ('Italian','Italian'),
        ('Jewish Studies','Jewish Studies'),
        ('Landscape Studies','Landscape Studies'),
        ('Latin American Studies','Latin American Studies'),
        ('Latino Studies','Latino Studies'),
        ('Law and Regulation','Law and Regulation'),
        ('Law and Society','Law and Society'),
        ('Lesbian, Gay, Bisexual and Transgender Studies','Lesbian, Gay, Bisexual and Transgender Studies'),
        ('Linguistics','Linguistics'),
        ('Marine Biology','Marine Biology'),
        ('Materials Science And Engineering','Materials Science and Engineering'),
        ('Mathematics','Mathematics'),
        ('Mechanical Engineering','Mechanical Engineering'),
        ('Medieval Studies','Medieval Studies'),
        ('Minority Indigenous and Third World Studies','Minority, Indigenous and Third World Studies'),
        ('Music','Music'),
        ('Natural Resources','Natural Resources'),
        ('Near Eastern Studies','Near Eastern Studies'),
        ('Nutrition and Health','Nutrition and Health'),
        ('Operations Research and Management Science','Operations Research and Management Science'),
        ('Physics','Physics'),
        ('Plant Sciences','Plant Sciences'),
        ('Policy Analysis and Management','Policy Analysis and Management'),
        ('Portugues and Brazilian Studies','Portuguese and Brazilian Studies'),
        ('Real Estate','Real Estate'),
        ('Religious Studies','Religious Studies'),
        ('Science and Technology Studies','Science and Technology Studies'),
        ('Science of Earth Systems','Science of Earth Systems'),
        ('Science of Natural and Environmental Systems','Science of Natural and Environmental Systems'),
        ('Soil Science','Soil Science'),
        ('South Asia Studies','South Asia Studies'),
        ('Southeast Asia Studies','Southeast Asia Studies'),
        ('Spanish','Spanish'),
        ('Sustainable Energy Systems','Sustainable Energy System'),
        ('Theatre','Theatre'),
        ('Urban and Regional Studies','Urban and Regional Studies'),
        ('Visual Studies','Visual Studies'),
        ('Viticulture and Enology','Viticulture and Enology'),
    )
    minor = forms.ChoiceField(label=("Minor"),
        choices=MINOR, widget=forms.Select(),)
    EXTRACURRICULARS = (
        #First entry is an abbreviation, second is how it appears on the site
        ('Acapella','Acapella'),
        ('Art','Art'),
        ('Club or Intramural Sports','Club or Intramural Sports'),
        ('Comedy','Comedy'),
        ('Community Service','Community Service'),
        ('Cultural','Cultural'),
        ('Dance','Dance'),
        ('Design and Graphics','Design and Graphics'),
        ('Entrepreneurship','Entrepreneurship'),
        ('Environmental Sustainability','Environmental Sustainability'),
        ('Event Planning','Event Planning'),
        ('Fashion','Fashion'),
        ('Greek Life','Greek Life'),
        ('Journalism','Journalism'),
        ('Languages','Languages'),
        ('Media','Media'),
        ('Music','Music'),
        ('Outdoor Recreation','Outdoor Recreation'),
        ('Partying','Partying'),
        ('Pre-Professional Organizations','Pre-Professional Organizations'),
        ('Project Team','Project Team'),
        ('Political Activism','Political Activism'),
        ('Science Research','Science Research'),
        ('Social Science Research','Social Science Research'),
        ('Travel','Travel'),
        ('Religious','Religious'),
        ('ROTC','ROTC'),
        ('Speech and Debate','Speech and Debate'),
        ('Student Government','Student Government'),
        ('Theatre','Theatre'),
        ('Varsity Sports','Varsity Sports'),
    )

    extracurriculars = forms.MultipleChoiceField(label=("Extracurriculars"),
        choices=EXTRACURRICULARS, widget=forms.CheckboxSelectMultiple())

    extra_sa = forms.CharField(label=("Feel free to list any other specific extracurricular activities"),
        widget=forms.Textarea, max_length=75, required=False)

    CAREER = (
        #First entry is an abbreviation, second is how it appears on the site
        ('Business and Finance','Business and Finance'),
        ('Computer and Technology','Computer and Technology'),
        ('Design','Design'),
        ('Education','Education'),
        ('Engineering','Engineering'),
        ('Entertainment','Entertainment'),
        ('Graduate Study','Grad
