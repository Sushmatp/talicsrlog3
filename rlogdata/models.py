from django.db import models, migrations
from django_pandas.managers import DataFrameManager
from django.contrib.postgres.fields import HStoreField
#from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth.models import UserManager


class Client(models.Model):
    # ClientID = models.TextField(unique = True)
    ClientName = models.TextField(null = True)
    CreatedOn = models.DateField(null = True)
    ShortName = models.TextField(unique = True)



class Staging(models.Model):
    # sr_no = models.IntegerField(unique = True, null = True)
    recruiter = models.TextField(null = True)
    client = models.TextField(null = True)
    position = models.TextField(null = True)
    reqt_date = models.DateField(null = True)
    date_cv_submitted = models.DateField(null = True)
    candidate_name = models.TextField(null = True)
    current_status = models.IntegerField(null = True)
    current_status_desc = models.TextField(null = True)
    interview_date = models.DateField(blank = True, null = True)
    remarks = models.TextField(blank = True, null = True)
    skills = models.TextField(null = True)
    current_org = models.TextField(null = True)
    qualification = models.TextField(null = True)
    total_exp = models.FloatField(null = True)
    current_location = models.TextField(null = True)
    contact_details_mobile = models.IntegerField(null = True)
    contact_details_phone2 = models.IntegerField(null = True)
    email = models.EmailField(null = True)
    current_salary = models.FloatField(null = True)
    expected_salary_percentage = models.IntegerField(null = True)
    expected_salary_amt = models.FloatField(null = True)
    notice_period = models.FloatField(null = True)
    Int_Tele_Date = models.DateField(blank = True, null = True)
    Int_Tele_Result = models.TextField(blank = True, null = True)
    Int_p1_Date = models.DateField(blank = True, null = True)
    Int_p1_Result = models.TextField(blank = True, null = True)
    Int_p2_Date = models.DateField(blank = True, null = True)
    Int_p2_Result = models.TextField(blank = True, null = True)
    Int_p3_Date = models.DateField(blank = True, null = True)
    Int_p3_Result = models.TextField(blank = True, null = True)
    Int_Final_Date = models.DateField(blank = True, null = True)
    Int_Final_Result = models.TextField(blank = True, null = True)
    Int_HR_Date = models.DateField(blank = True, null = True)
    Int_HR_Result = models.TextField(blank = True, null = True)
    offer_date = models.DateField(blank = True, null = True)
    offer_amt = models.FloatField(blank = True, null = True)
    joining_date = models.DateField(blank = True, null = True)
    vacancy_code = models.TextField(blank = True, null = True)
    applicant_code = models.TextField(blank = True, null = True)
    DOB = models.DateField(blank = True, null = True)
    preferred_company = models.TextField(blank = True, null = True)
    preferred_location = models.TextField(blank = True, null = True)
    week_number = models.IntegerField(blank = True, null = True)
    wk_year = models.IntegerField(blank = True, null = True)
    reason = models.TextField(blank = True, null = True)

    objects = DataFrameManager()

    class Meta:
        managed = True

class GoodRecords(models.Model):
    # sr_no = models.IntegerField(unique = True)
    recruiter = models.ForeignKey('Usr_table', on_delete = models.RESTRICT)
    client = models.ForeignKey('Client', on_delete = models.RESTRICT)
    position = models.TextField(null = True)
    reqt_date = models.DateField(null = True)
    date_cv_submitted = models.DateField(null = True)
    candidate_name = models.TextField(null = True)
    current_status = models.IntegerField(null = True)
    current_status_desc = models.TextField(null = True)
    interview_date = models.DateField(blank = True, null = True)
    remarks = models.TextField(blank = True, null = True)
    skills = models.TextField(null = True)
    current_org = models.TextField(null = True)
    qualification = models.TextField(null = True)
    total_exp = models.FloatField(null = True)
    current_location = models.TextField(null = True)
    contact_details_mobile = models.IntegerField(null = True)
    contact_details_phone2 = models.IntegerField(null = True)
    email = models.EmailField(null = True)
    current_salary = models.FloatField(null = True)
    expected_salary_percentage = models.IntegerField(null = True)
    expected_salary_amt = models.FloatField(null = True)
    notice_period = models.FloatField(null = True)
    Int_Tele_Date = models.DateField(blank = True, null = True)
    Int_Tele_Result = models.TextField(blank = True, null = True)
    Int_p1_Date = models.DateField(blank = True, null = True)
    Int_p1_Result = models.TextField(blank = True, null = True)
    Int_p2_Date = models.DateField(blank = True, null = True)
    Int_p2_Result = models.TextField(blank = True, null = True)
    Int_p3_Date = models.DateField(blank = True, null = True)
    Int_p3_Result = models.TextField(blank = True, null = True)
    Int_Final_Date = models.DateField(blank = True, null = True)
    Int_Final_Result = models.TextField(blank = True, null = True)
    Int_HR_Date = models.DateField(blank = True, null = True)
    Int_HR_Result = models.TextField(blank = True, null = True)
    offer_date = models.DateField(blank = True, null = True)
    offer_amt = models.FloatField(blank = True, null = True)
    joining_date = models.DateField(blank = True, null = True)
    vacancy_code = models.TextField(blank = True, null = True)
    applicant_code = models.TextField(blank = True, null = True)
    DOB = models.DateField(blank = True, null = True)
    preferred_company = models.TextField(blank = True, null = True)
    preferred_location = models.TextField(blank = True, null = True)
    week_number = models.IntegerField(blank = True, null = True)
    wk_year = models.IntegerField(blank = True, null = True)

    objects = DataFrameManager()

    class Meta:
        managed = True

class BadRecords(models.Model):
    # sr_no = models.IntegerField(unique = True)
    recruiter = models.TextField(null = True)
    client = models.TextField(null = True)
    position = models.TextField(null = True)
    reqt_date = models.TextField(null = True)
    date_cv_submitted = models.TextField(null = True)
    candidate_name = models.TextField(null = True)
    current_status = models.IntegerField(null = True)
    current_status_desc = models.TextField(null = True)
    interview_date = models.TextField(blank = True, null = True)
    remarks = models.TextField(blank = True, null = True)
    skills = models.TextField(null = True)
    current_org = models.TextField(null = True)
    qualification = models.TextField(null = True)
    total_exp = models.TextField(null = True)
    current_location = models.TextField(null = True)
    contact_details_mobile = models.IntegerField(null = True)
    contact_details_phone2 = models.IntegerField(null = True)
    email = models.EmailField(null = True)
    current_salary = models.TextField(null = True)
    expected_salary_percentage = models.IntegerField(null = True)
    expected_salary_amt = models.TextField(null = True)
    notice_period = models.TextField(null = True)
    Int_Tele_Date = models.TextField(blank = True, null = True)
    Int_Tele_Result = models.TextField(blank = True, null = True)
    Int_p1_Date = models.TextField(blank = True, null = True)
    Int_p1_Result = models.TextField(blank = True, null = True)
    Int_p2_Date = models.TextField(blank = True, null = True)
    Int_p2_Result = models.TextField(blank = True, null = True)
    Int_p3_Date = models.TextField(blank = True, null = True)
    Int_p3_Result = models.TextField(blank = True, null = True)
    Int_Final_Date = models.TextField(blank = True, null = True)
    Int_Final_Result = models.TextField(blank = True, null = True)
    Int_HR_Date = models.TextField(blank = True, null = True)
    Int_HR_Result = models.TextField(blank = True, null = True)
    offer_date = models.TextField(blank = True, null = True)
    offer_amt = models.TextField(blank = True, null = True)
    joining_date = models.TextField(blank = True, null = True)
    vacancy_code = models.TextField(blank = True, null = True)
    applicant_code = models.TextField(blank = True, null = True)
    DOB = models.TextField(blank = True, null = True)
    preferred_company = models.TextField(blank = True, null = True)
    preferred_location = models.TextField(blank = True, null = True)
    week_number = models.TextField(blank = True, null = True)
    wk_year = models.TextField(blank = True, null = True)
    reason = models.TextField(blank = True, null = True)

    objects = DataFrameManager()

    class Meta:
        managed = True

class Mapping(models.Model):
    # MappingID = models.IntegerField(primary_key = True)
    UserID = models.ForeignKey('Usr_table', on_delete = models.RESTRICT)
    MappingFor = models.TextField(null = True)
    CreatedOn = models.DateField(auto_now_add = True, null = True)
    Mappings =  HStoreField(null=True)

class Mandates(models.Model):

    JDCode = models.TextField(unique = True)
    VacancyCode = models.TextField(null = True)
    Title = models.TextField(null = True)                                                  #Job Title
    Location = models.TextField(null = True)
    HiringManager = models.TextField(null = True)
    RequisitionManager = models.TextField(blank = True)
    KeySkills = models.TextField(null = True)
    Role = models.TextField(blank = True)
    DesiredExperience = models.TextField(blank = True)
    Education = models.TextField(null = True)
    MinExpRange = models.IntegerField(null = True)
    MaxExpRange = models.IntegerField(null = True)
    CTC = models.IntegerField(blank = True)
    NoticePeriod = models.IntegerField(blank = True)
    Status = models.TextField(max_length = 1)
    Openings = models.IntegerField(null = True)
    No_Filled = models.IntegerField(null = True)
    HiringMgrContact = models.IntegerField(null = True)
    HiringMgrEmail = models.TextField(null = True)
    #RecruiterAssignedTo = models.ForeignKey('Usr_table', on_delete = models.RESTRICT)
    AssignedDate = models.DateField(null = True)
    #ClientID = models.ForeignKey('Client', on_delete = models.RESTRICT)

class Usr_table(models.Model):
    # UserID = models.IntegerField(primary_key = True)
    #REQUIRED_FIELDS= []
    USERNAME_FIELD= 'UserName'
    UserName = models.TextField(null = True)
    UserType = models.TextField(null = True)
    UserDescription = models.TextField(null = True)
    UserCompany = models.TextField(null = True)
    UserStatus = models.TextField(max_length = 1, null = True)
    UserReportsTo = models.ForeignKey('self', null = True, on_delete = models.RESTRICT, blank = True)
    password = models.TextField(null = True)
    CreatedOn = models.DateField(auto_now_add = True, null = True)
    Role = models.TextField(null = True)
    Designation = models.TextField(null = True)
    Phone = models.IntegerField(null = True)
    EmailID = models.EmailField(null = True)
    Department = models.TextField(blank = True)
    ValidTill = models.DateField(null = True)
    

class CandidateStatus(models.Model):

    TYPE = [('SELECT', 'Select'),
            ('REJECT', 'Reject')]

    CompanyID = models.IntegerField(null = True)
    StageID = models.IntegerField(unique = True, null = True)
    StageName = models.TextField(null = True)
    StageType = models.CharField(null = True, choices = TYPE, max_length = 6)


class Agency(models.Model):
    AgencyName = models.TextField(null = True)
    Location = models.TextField(null = True)
    Website = models.TextField(null = True)
    ContractStartedOn = models.DateField(null = True)
    ContractValidTill = models.DateField(null = True)
    KCName = models.TextField(null = True)
    KCEmail = models.EmailField(null = True)
    KCPhone = models.IntegerField(null = True)

    def __str__(self):
        return self.AgencyName