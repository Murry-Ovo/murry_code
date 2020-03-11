def grade_converter(gpa):
  if gpa >= 4.0:
    grade = 'A'
  elif gpa >= 3.0:
    grade = 'B'
  elif gpa >= 2.0:
    grade = 'C'
  elif gpa >= 1.0:
    grade = 'D'
  else:
    grade = 'F'
  return grade



print(grade_converter(3.5))





or

def applicant_selector(gpa,ps_score,ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."