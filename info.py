print("""==============================================================
        PHILIPPINE CITIZEN INFORMATION SYSTEM
==============================================================

Course  : BSCS
Version : 1.0
Developer : 

==============================================================""")

print("""PLEASE READ THE FOLLOWING:

• Enter all information correctly.
• Do not leave any field blank.
• Use complete names.
• Double-check your answers before pressing Enter.

Press Enter to begin...""")

#personal information
print("""PERSONAL INFORMATION
--------------------------------------------------------------\n""")

First_name = input("First Name: ")
Middle_name = input("Middle Name : ")
Last_name = input("Last Name  : ")
Suffix = input("Suffix  : ")
age = input("Age: ")
birth_date = input("Date of birth: ")
birth_place = input("Place of Birth: ")
sex = input("Sex : ")
civil_status = input("Civil Status  : ")
nationality = input("Nationality : ")
religion = input("Religion: ")

#contact information
print("""
CONTACT INFORMATION
--------------------------------------------------------------\n""")


house_number = input("House Number: ")
street = input("Street: ")
barangay = input("Barangay: ") 
municipality =input("Municipality: ")
province = input("Province : ")
region = input("Region  : ")
zip_code = input("Zip Code : ")
email_add = input("Email Address : ")
mobile_number = input("Mobile Number : ")
telephone_number = input("Telephone Number: ")

#government information
print("""
GOVERNMENT INFORMATION
--------------------------------------------------------------\n""")

national_id = input("National ID: ")
passport_num = input("Passport Number: ")
driverlicense_num = input("Driver's License Number: ")
votersID_num = input("Voter's ID Number: ")
philHealth_num = input("PhilHealth Number : ")
sss_num = input("SSS Number: ")
tin_num = input("TIN Number")

#education information 
print("""
EDUCATIONAL INFORMATION
--------------------------------------------------------------\n""")

elem_school = input("Elementary School                  : ")
high_school = input("High School                        : ")
sh_school = input("Senior High School                   : ")
college = input("College                                : ")
course = input("Course                                  : ")
yr_level= input("Year level                            : ")
student_num = input ("Student Number                    : ")

#employment information
print("""
EMPLOYMENT INFORMATION
--------------------------------------------------------------\n""")

occupation = input("Occupation                          : ")
company_name = input("Company Name                      : ")
yrs_of_experience = input("Years of Experience          : ")
monthly_salary = input("Monthly Salary                  : ")

#emergency contact
print("""
EMERGENCY CONTACT
--------------------------------------------------------------
\n""")

contact_person = input("Contact Person                  : ")
relationship = input("Relationship                      : ")
contact_number = input("Contact Number                  : ")
address = input("Address                                : ")
email = input("Email                                    : ")


# Personal Information
print("""
==============================================================
                  PERSONAL INFORMATION
==============================================================
""")

print(f"{'First Name':<26}: {First_name}")
print(f"{'Middle Name':<26}: {Middle_name}")
print(f"{'Last Name':<26}: {Last_name}")
print(f"{'Suffix':<26}: {Suffix}")
print(f"{'Age':<26}: {age}")
print(f"{'Birth Date':<26}: {birth_date}")
print(f"{'Birth Place':<26}: {birth_place}")
print(f"{'Sex':<26}: {sex}")
print(f"{'Civil Status':<26}: {civil_status}")
print(f"{'Nationality':<26}: {nationality}")
print(f"{'Religion':<26}: {religion}")

# Contact Information
print("""
==============================================================
                   CONTACT INFORMATION
==============================================================
""")

print(f"{'House Number':<26}: {house_number}")
print(f"{'Street':<26}: {street}")
print(f"{'Barangay':<26}: {barangay}")
print(f"{'Municipality':<26}: {municipality}")
print(f"{'Province':<26}: {province}")
print(f"{'Region':<26}: {region}")
print(f"{'ZIP Code':<26}: {zip_code}")
print(f"{'Email Address':<26}: {email_add}")
print(f"{'Mobile Number':<26}: {mobile_number}")
print(f"{'Telephone Number':<26}: {telephone_number}")


# Government Information
print("""
==============================================================
                  GOVERNMENT INFORMATION
==============================================================
""")

print(f"{'National ID':<26}: {national_id}")
print(f"{'Passport Number':<26}: {passport_num}")
print(f"{'Driver License':<26}: {driverlicense_num}")
print(f"{'Voter ID':<26}: {votersID_num}")
print(f"{'PhilHealth Number':<26}: {philHealth_num}")
print(f"{'SSS Number':<26}: {sss_num}")
print(f"{'TIN Number':<26}: {tin_num}")

# Educational Information
print("""
==============================================================
                  EDUCATIONAL INFORMATION
==============================================================
""")

print(f"{'Elementary School':<26}: {elem_school}")
print(f"{'High School':<26}: {high_school}")
print(f"{'Senior High School':<26}: {sh_school}")
print(f"{'College':<26}: {college}")
print(f"{'Course':<26}: {course}")
print(f"{'Year Level':<26}: {yr_level}")
print(f"{'Student Number':<26}: {student_num}")


# Employment Information
print("""
==============================================================
                   EMPLOYMENT INFORMATION
==============================================================
""")

print(f"{'Occupation':<26}: {occupation}")
print(f"{'Company Name':<26}: {company_name}")
print(f"{'Years of Experience':<26}: {yrs_of_experience}")
print(f"{'Monthly Salary':<26}: {monthly_salary}")


# Emergency Contact
print("""
==============================================================
                     EMERGENCY CONTACT
==============================================================
""")

print(f"{'Contact Person':<26}: {contact_person}")
print(f"{'Relationship':<26}: {relationship}")
print(f"{'Contact Number':<26}: {contact_number}")
print(f"{'Address':<26}: {address}")
print(f"{'Email':<26}: {email}")


